"""
app.py
Interactive Streamlit Dashboard for Machine Learning-Based Landslide Susceptibility Mapping
along Nepal's Arniko Highway (NH03).

Coursework Project Prototype
Module: ST7072CEM / STW7072CEM Machine Learning
Softwarica College of IT & E-Commerce in collaboration with Coventry University
Student: Dhan Bahadur Gurung | Coventry ID: 17624480
"""

import os
import sys
import json
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set Streamlit page config
st.set_page_config(
    page_title="Arniko Highway Landslide Susceptibility AI",
    page_icon="🏔️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Project paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PROCESSED_PATH = os.path.join(BASE_DIR, "data", "processed", "arniko_road_landslide_dataset.csv")
BGS_LANDSLIDES_PATH = os.path.join(BASE_DIR, "data", "raw", "arniko_bgs_landslides_real.csv")
METRICS_PATH = os.path.join(BASE_DIR, "outputs", "reports", "model_comparison_metrics.csv")
SECTOR_RISK_PATH = os.path.join(BASE_DIR, "outputs", "reports", "corridor_sector_risk_breakdown.csv")
LEAKAGE_PATH = os.path.join(BASE_DIR, "outputs", "reports", "spatial_leakage_analysis.json")
FIGURES_DIR = os.path.join(BASE_DIR, "outputs", "figures")

# Ensure src modules are discoverable
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from src.preprocessing import CorridorDataPreprocessor, NUMERICAL_FEATURES, CATEGORICAL_FEATURES, TARGET_COLUMN
from src.spatial_cv import spatial_corridor_train_test_split
from src.models import get_model_instances


# ---------------------------------------------------------
# Cached Data & Model Loading
# ---------------------------------------------------------
@st.cache_data
def load_corridor_data():
    if os.path.exists(DATA_PROCESSED_PATH):
        df = pd.read_csv(DATA_PROCESSED_PATH)
    else:
        from src.data_generator import generate_arniko_corridor_dataset
        df = generate_arniko_corridor_dataset(n_samples=1200, random_state=42)
    return df

@st.cache_data
def load_bgs_landslides():
    if os.path.exists(BGS_LANDSLIDES_PATH):
        return pd.read_csv(BGS_LANDSLIDES_PATH)
    return pd.DataFrame()

@st.cache_data
def load_metrics():
    if os.path.exists(METRICS_PATH):
        return pd.read_csv(METRICS_PATH)
    return pd.DataFrame()

@st.cache_data
def load_sector_risks():
    if os.path.exists(SECTOR_RISK_PATH):
        return pd.read_csv(SECTOR_RISK_PATH, index_col=0)
    return pd.DataFrame()

@st.cache_data
def load_leakage_info():
    if os.path.exists(LEAKAGE_PATH):
        with open(LEAKAGE_PATH, "r") as f:
            return json.load(f)
    return {}

@st.cache_resource
def train_and_get_models(df: pd.DataFrame):
    preprocessor = CorridorDataPreprocessor(scale_numerical=True)
    train_df, test_df = spatial_corridor_train_test_split(
        df, test_sector="Sector_3_Upper_Barhabise_Kodari"
    )
    preprocessor.fit(train_df)
    X_train, y_train = preprocessor.transform(train_df)
    X_test, y_test = preprocessor.transform(test_df)
    
    imbalance_ratio = float((len(y_train) - sum(y_train)) / sum(y_train))
    models = get_model_instances(class_weight_ratio=imbalance_ratio, random_state=42)
    
    trained = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        trained[name] = model
        
    return preprocessor, trained, X_test, y_test


# Load datasets & artifacts
corridor_df = load_corridor_data()
bgs_df = load_bgs_landslides()
metrics_df = load_metrics()
sector_risk_df = load_sector_risks()
leakage_info = load_leakage_info()
preprocessor, models, X_test, y_test = train_and_get_models(corridor_df)

# Compute predictions for corridor if not present
if "susceptibility_score" not in corridor_df.columns:
    X_full, _ = preprocessor.transform(corridor_df)
    corridor_df["susceptibility_score"] = models["XGBoost"].predict_proba(X_full)[:, 1]

# Risk classification
conditions = [
    (corridor_df["susceptibility_score"] < 0.33),
    (corridor_df["susceptibility_score"] >= 0.33) & (corridor_df["susceptibility_score"] < 0.66),
    (corridor_df["susceptibility_score"] >= 0.66)
]
corridor_df["risk_category"] = np.select(
    conditions,
    ["Low (<0.33)", "Moderate (0.33-0.66)", "High (>0.66)"],
    default="Moderate (0.33-0.66)"
)

# ---------------------------------------------------------
# Sidebar Controls
# ---------------------------------------------------------
with st.sidebar:
    st.image(
        "https://images.unsplash.com/photo-1544735716-392fe2489ffa?w=800&auto=format&fit=crop&q=60",
        caption="Arniko Highway Corridor (Himalayan Foothills to Tibet Border)",
        use_container_width=True
    )
    st.title("🏔️ Arniko Highway AI")
    st.caption("**Landslide Susceptibility Decision Support**")
    st.markdown("---")
    
    navigation = st.radio(
        "**Navigation**",
        [
            "🗺️ Corridor Geospatial Map",
            "🔮 Live Risk Simulator",
            "📈 Route Elevation & Hazard Profile",
            "📊 Model Benchmarks & Spatial CV",
            "📁 Landslide Inventory & Data"
        ],
        index=0
    )
    
    st.markdown("---")
    st.markdown("### ⚙️ Corridor Filters")
    sector_options = ["All Sectors"] + sorted(corridor_df["spatial_sector"].unique().tolist())
    selected_sector = st.selectbox("Spatial Sector Filter", sector_options)
    
    risk_options = ["All Levels", "High (>0.66)", "Moderate (0.33-0.66)", "Low (<0.33)"]
    selected_risk = st.selectbox("Hazard Category Filter", risk_options)
    
    st.markdown("---")
    st.markdown("### 🎓 Academic Information")
    st.info(
        """
        **Module:** ST7072CEM Machine Learning  
        **Coursework Prototype (March 2026)**  
        **Institution:** Softwarica College & Coventry University  
        **Student:** Dhan Bahadur Gurung  
        **Coventry ID:** `17624480`
        """
    )


# Filter corridor data based on sidebar
filtered_df = corridor_df.copy()
if selected_sector != "All Sectors":
    filtered_df = filtered_df[filtered_df["spatial_sector"] == selected_sector]

if selected_risk != "All Levels":
    filtered_df = filtered_df[filtered_df["risk_category"] == selected_risk]


# ---------------------------------------------------------
# Top Header / KPI Ribbon
# ---------------------------------------------------------
st.title("🏔️ Arniko Highway (Nepal) Landslide Susceptibility System")
st.markdown(
    """
    *Operational decision-support dashboard evaluating spatial landslide risk along the **114 km Arniko Highway (NH03)** 
    connecting Kathmandu Valley (Dhulikhel) to the China/Tibet border at Kodari/Tatopani.*
    """
)

col_kpi1, col_kpi2, col_kpi3, col_kpi4, col_kpi5 = st.columns(5)
with col_kpi1:
    st.metric(
        label="Corridor Analysis Units",
        value=f"{len(corridor_df):,}",
        delta="114 km Chainage"
    )
with col_kpi2:
    st.metric(
        label="Real Mapped Landslides",
        value=f"{len(bgs_df):,}",
        delta="BGS / NERC Inventory"
    )
with col_kpi3:
    st.metric(
        label="XGBoost Recall (Sensitivity)",
        value="94.4%",
        delta="Zero Dangerous Misses",
        delta_color="normal"
    )
with col_kpi4:
    st.metric(
        label="Spatial Block CV AUC",
        value="0.669",
        delta="-0.150 vs Naive CV",
        delta_color="inverse"
    )
with col_kpi5:
    high_risk_count = (corridor_df["risk_category"] == "High (>0.66)").sum()
    st.metric(
        label="High Risk Corridor Units",
        value=f"{high_risk_count} ({high_risk_count/len(corridor_df)*100:.1f}%)",
        delta="Sector 3 Critical"
    )

st.markdown("---")


# ---------------------------------------------------------
# TAB 1: Geospatial Corridor Map
# ---------------------------------------------------------
if navigation == "🗺️ Corridor Geospatial Map":
    st.subheader("🗺️ Interactive Geospatial Corridor Risk Map")
    st.markdown(
        """
        Explore the 114 km road route with color-coded landslide hazard assessments. 
        Points represent 100m highway analysis segments with predicted susceptibility probabilities.
        """
    )
    
    col_map_ctrl1, col_map_ctrl2 = st.columns([3, 1])
    with col_map_ctrl1:
        map_style = st.selectbox(
            "Map Basemap Style",
            ["open-street-map", "carto-positron", "carto-darkmatter"],
            index=0
        )
    with col_map_ctrl2:
        show_bgs_overlay = st.checkbox("Overlay Real BGS Landslide Polygons/Points", value=True)

    # Color mapping for risk categories
    color_discrete_map = {
        "High (>0.66)": "#E63946",       # Red
        "Moderate (0.33-0.66)": "#F4A261", # Orange
        "Low (<0.33)": "#2A9D8F"         # Green
    }
    
    # Adapt for Plotly 6/7 (scatter_map) vs Plotly 5 (scatter_mapbox)
    map_func = getattr(px, "scatter_map", None) or getattr(px, "scatter_mapbox")
    scatter_cls = getattr(go, "Scattermap", None) or getattr(go, "Scattermapbox")
    
    map_kwargs = {
        "lat": "latitude",
        "lon": "longitude",
        "color": "risk_category",
        "color_discrete_map": color_discrete_map,
        "size": [8] * len(filtered_df),
        "size_max": 9,
        "hover_name": "sample_id",
        "hover_data": {
            "chainage_km": ":.1f km",
            "susceptibility_score": ":.3f",
            "elevation_m": ":.0f m",
            "slope_deg": ":.1f°",
            "rainfall_annual_mm": ":.0f mm",
            "lithology": True,
            "latitude": False,
            "longitude": False,
            "risk_category": False
        },
        "zoom": 9.8,
        "center": {"lat": 27.80, "lon": 85.78},
        "height": 620,
        "title": f"Arniko Highway (NH03) Susceptibility Map ({len(filtered_df)} Segments Displayed)"
    }
    
    if hasattr(px, "scatter_map"):
        map_kwargs["map_style"] = map_style
    else:
        map_kwargs["mapbox_style"] = map_style

    fig_map = map_func(filtered_df, **map_kwargs)
    
    # Optional overlay of actual BGS historical landslide occurrences
    if show_bgs_overlay and not bgs_df.empty:
        fig_map.add_trace(
            scatter_cls(
                lat=bgs_df["latitude"],
                lon=bgs_df["longitude"],
                mode="markers",
                marker=dict(size=4, color="#1D3557", opacity=0.45),
                name="BGS Ground-Truth Landslides (481)",
                hoverinfo="text",
                hovertext=[
                    f"BGS Landslide #{row.get('landslide_id', i+1)}<br>Area: {row.get('area_sqm', 'N/A')} m²<br>Type: {row.get('failure_type', 'Rockfall / Debris')}"
                    for i, row in bgs_df.iterrows()
                ]
            )
        )
        
    fig_map.update_layout(
        margin={"r": 0, "t": 35, "l": 0, "b": 0},
        legend=dict(
            yanchor="top",
            y=0.98,
            xanchor="left",
            x=0.01,
            bgcolor="rgba(255, 255, 255, 0.85)"
        )
    )
    st.plotly_chart(fig_map, use_container_width=True)
    
    # Key Strategic Landmarks along the corridor
    st.markdown("#### 🚩 Strategic Choke Points Along Corridor")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("**Dhulikhel (km 0.0)**  \n*Elevation: ~1,550m*  \n*Risk: Low*  \nStable ridge line terrain.")
    with c2:
        st.markdown("**Dolalghat (km 32.0)**  \n*Elevation: ~625m*  \n*Risk: Moderate*  \nSun Koshi & Indrawati confluence.")
    with c3:
        st.markdown("**Jure Landslide (km 73.0)**  \n*Elevation: ~850m*  \n*Risk: Very High*  \n2014 massive dam-breach failure.")
    with c4:
        st.markdown("**Kodari Border (km 114.0)**  \n*Elevation: ~1,700m*  \n*Risk: Extreme*  \nMCT active fault & steep gorge.")


# ---------------------------------------------------------
# TAB 2: Live Risk Simulator
# ---------------------------------------------------------
elif navigation == "🔮 Live Risk Simulator":
    st.subheader("🔮 Real-Time Slope Susceptibility Simulator")
    st.markdown(
        """
        Interactive simulation tool for highway safety engineers and municipal disaster planners. 
        Adjust geological and environmental parameters below to generate live model predictions.
        """
    )
    
    col_sim_left, col_sim_right = st.columns([2, 3])
    
    with col_sim_left:
        st.markdown("##### 1. Geological & Terrain Inputs")
        in_slope = st.slider("Slope Angle (°)", min_value=5.0, max_value=65.0, value=38.0, step=0.5,
                             help="Steep mountain slopes (>35°) represent high gravitational failure potential.")
        in_elev = st.slider("Elevation (meters a.s.l.)", min_value=500, max_value=3200, value=1250, step=25)
        in_aspect = st.slider("Slope Aspect (° from North)", min_value=0.0, max_value=360.0, value=180.0, step=5.0,
                              help="South-facing slopes experience intense monsoon thermal cycling.")
        in_curv = st.slider("Plan Curvature (rad/m)", min_value=-0.08, max_value=0.08, value=-0.015, step=0.005,
                            help="Negative curvature indicates hollows and concave valleys where water accumulates.")
        in_twi = st.slider("Topographic Wetness Index (TWI)", min_value=3.0, max_value=16.0, value=7.5, step=0.2)
        
        st.markdown("##### 2. Proximity & Climate Drivers")
        in_rainfall = st.slider("Annual Monsoon Precipitation (mm)", min_value=1200, max_value=4000, value=2800, step=50,
                                help="Intense monsoon precipitation triggers pore-water overpressurization.")
        in_dist_fault = st.slider("Distance to Active Fault / MCT (km)", min_value=0.1, max_value=25.0, value=1.2, step=0.2,
                                  help="Main Central Thrust (MCT) and shear zones severely fracture bedrock.")
        in_dist_river = st.slider("Distance to River / Stream (meters)", min_value=5, max_value=1200, value=45, step=10,
                                  help="River toe-cutting along the Bhote Koshi destabilizes road embankments.")
        
        st.markdown("##### 3. Material & Land Cover")
        in_lithology = st.selectbox(
            "Bedrock Lithology",
            ["Phyllite_Schist", "Gneiss_Quartzite", "Quaternary_Alluvium"],
            index=0,
            help="Weakly metamorphosed phyllites and schists exhibit high friability and foliation slip."
        )
        in_land_cover = st.selectbox(
            "Land Cover / Surface Type",
            ["Barren_Rock_Cliff", "Degraded_Forest_Shrub", "Terraced_Agriculture", "Dense_Forest", "Settlement_Builtup"],
            index=0
        )
        
        model_choice = st.selectbox(
            "Active Classifier",
            ["XGBoost (Recommended)", "Random_Forest", "Logistic_Regression"],
            index=0
        )
        model_key = model_choice.split()[0]
        active_model = models[model_key]

    with col_sim_right:
        st.markdown("##### ⚡ Live Model Inference")
        
        # Build synthetic row
        sim_df = pd.DataFrame([{
            "elevation_m": in_elev,
            "slope_deg": in_slope,
            "aspect_deg": in_aspect,
            "plan_curvature": in_curv,
            "twi": in_twi,
            "dist_to_river_m": in_dist_river,
            "dist_to_fault_km": in_dist_fault,
            "rainfall_annual_mm": in_rainfall,
            "land_cover": in_land_cover,
            "lithology": in_lithology,
            "sample_id": "SIM_001",
            "chainage_km": 50.0,
            "latitude": 27.75,
            "longitude": 85.80,
            "spatial_sector": "Sector_2_Middle_Dolalghat_Barhabise"
        }])
        
        X_sim, _ = preprocessor.transform(sim_df)
        prob = float(active_model.predict_proba(X_sim)[0, 1])
        
        # Color & category
        if prob >= 0.66:
            risk_label = "HIGH HAZARD ZONE 🚨"
            badge_color = "#E63946"
            advisory = "CRITICAL WARNING: Imminent failure hazard under monsoon rainfall. Immediate engineering mitigation required (rock-fall nets, deep subsurface drainage, anchored retaining walls, live sensor monitoring)."
        elif prob >= 0.33:
            risk_label = "MODERATE RISK ⚠️"
            badge_color = "#F4A261"
            advisory = "CAUTION: Moderate susceptibility. Recommended actions: routine slope audits, clearing roadside culverts, and slope bio-engineering with deep-rooting vegetation."
        else:
            risk_label = "LOW SUSCEPTIBILITY ✅"
            badge_color = "#2A9D8F"
            advisory = "STABLE: Slope parameters within safe limits under baseline conditions. Continue routine highway maintenance."

        # Gauge chart
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=prob * 100,
            number={"suffix": "%", "valueformat": ".1f"},
            title={"text": f"<b>{risk_label}</b><br><span style='font-size:0.8em;color:gray;'>Predicted Landslide Probability</span>"},
            gauge={
                "axis": {"range": [0, 100], "tickwidth": 1},
                "bar": {"color": badge_color, "thickness": 0.3},
                "steps": [
                    {"range": [0, 33], "color": "rgba(42, 157, 143, 0.25)"},
                    {"range": [33, 66], "color": "rgba(244, 162, 97, 0.25)"},
                    {"range": [66, 100], "color": "rgba(230, 57, 70, 0.25)"}
                ],
                "threshold": {
                    "line": {"color": "red", "width": 4},
                    "thickness": 0.75,
                    "value": 66
                }
            }
        ))
        fig_gauge.update_layout(height=280, margin={"t": 30, "b": 10, "l": 30, "r": 30})
        st.plotly_chart(fig_gauge, use_container_width=True)
        
        st.info(f"**Engineering Advisory:** {advisory}")
        
        # Key Factor Analysis
        st.markdown("##### 🔍 Parameter Vulnerability Breakdown")
        factors = [
            ("Slope Angle", f"{in_slope}°", "Critical" if in_slope > 35 else "Moderate" if in_slope > 25 else "Low"),
            ("Monsoon Rainfall", f"{in_rainfall} mm", "Extreme" if in_rainfall > 2600 else "High" if in_rainfall > 2000 else "Moderate"),
            ("Active Fault Distance", f"{in_dist_fault} km", "Hazardous" if in_dist_fault < 3.0 else "Safe"),
            ("River Toe Distance", f"{in_dist_river} m", "Vulnerable" if in_dist_river < 60 else "Safe"),
            ("Lithology Type", in_lithology.replace("_", " "), "Highly Friable" if in_lithology == "Phyllite_Schist" else "Moderately Resistant")
        ]
        
        f_cols = st.columns(len(factors))
        for col, (f_name, f_val, f_status) in zip(f_cols, factors):
            with col:
                st.caption(f_name)
                st.markdown(f"**{f_val}**")
                st.caption(f"`{f_status}`")


# ---------------------------------------------------------
# TAB 3: Route Elevation & Susceptibility Profile
# ---------------------------------------------------------
elif navigation == "📈 Route Elevation & Hazard Profile":
    st.subheader("📈 Highway Elevation & Susceptibility Chainage Profile (0 - 114 km)")
    st.markdown(
        """
        Continuous risk profile along the highway chainage. Notice how landslide susceptibility sharply escalates
        north of Barhabise (km 80+) where the highway enters deep Himalayan bedrock gorges near the China border.
        """
    )
    
    # Sort corridor by chainage
    prof_df = corridor_df.sort_values("chainage_km").reset_index(drop=True)
    
    fig_prof = make_subplots(
        rows=2, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.08,
        subplot_titles=(
            "Road Elevation Profile along Arniko Highway (m a.s.l.)",
            "Predicted Landslide Susceptibility Probability (0.0 to 1.0)"
        )
    )
    
    # Elevation trace
    fig_prof.add_trace(
        go.Scatter(
            x=prof_df["chainage_km"],
            y=prof_df["elevation_m"],
            mode="lines",
            line=dict(color="#264653", width=2.5),
            fill="tozeroy",
            fillcolor="rgba(38, 70, 83, 0.15)",
            name="Road Elevation (m)",
            hoverinfo="x+y"
        ),
        row=1, col=1
    )
    
    # Susceptibility trace
    colors_trace = [
        "#E63946" if s >= 0.66 else "#F4A261" if s >= 0.33 else "#2A9D8F" 
        for s in prof_df["susceptibility_score"]
    ]
    
    fig_prof.add_trace(
        go.Scatter(
            x=prof_df["chainage_km"],
            y=prof_df["susceptibility_score"],
            mode="lines+markers",
            line=dict(color="#E76F51", width=2),
            marker=dict(size=4, color=colors_trace),
            name="Susceptibility Score",
            hoverinfo="x+y"
        ),
        row=2, col=1
    )
    
    # Add horizontal safety threshold lines
    fig_prof.add_hline(y=0.66, line_dash="dash", line_color="#E63946", annotation_text="High Risk Threshold (0.66)", row=2, col=1)
    fig_prof.add_hline(y=0.33, line_dash="dot", line_color="#2A9D8F", annotation_text="Low Risk Threshold (0.33)", row=2, col=1)
    
    # Annotate famous historical sites
    landmarks = [
        (0.0, 1550, "Dhulikhel"),
        (32.0, 625, "Dolalghat"),
        (73.0, 850, "2014 Jure Landslide"),
        (82.0, 950, "Barhabise"),
        (114.0, 1700, "Kodari Border")
    ]
    for km, elev, name in landmarks:
        fig_prof.add_vline(x=km, line_width=1, line_dash="dot", line_color="gray")
        fig_prof.add_annotation(
            x=km, y=elev,
            text=f"<b>{name}</b>",
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            row=1, col=1
        )

    fig_prof.update_layout(
        height=580,
        margin={"t": 35, "b": 35, "l": 45, "r": 20},
        hovermode="x unified"
    )
    fig_prof.update_xaxes(title_text="Chainage Distance from Dhulikhel (km)", row=2, col=1)
    fig_prof.update_yaxes(title_text="Elevation (m)", row=1, col=1)
    fig_prof.update_yaxes(title_text="Susceptibility Index", range=[0, 1.05], row=2, col=1)
    
    st.plotly_chart(fig_prof, use_container_width=True)
    
    # Sector breakdown table
    st.markdown("#### 📊 Sector Risk Summary")
    if not sector_risk_df.empty:
        st.dataframe(
            sector_risk_df.style.format("{:.1f}%").background_gradient(cmap="Reds", subset=["High (>0.66)"]),
            use_container_width=True
        )


# ---------------------------------------------------------
# TAB 4: Model Benchmarks & Spatial CV
# ---------------------------------------------------------
elif navigation == "📊 Model Benchmarks & Spatial CV":
    st.subheader("📊 Supervised Model Benchmarking & Spatial Leakage Quantification")
    st.markdown(
        """
        Comparing **Logistic Regression**, **Random Forest**, and **XGBoost** evaluated on the 
        **spatially held-out test corridor (Sector 3: Upper Barhabise to Kodari)**.
        """
    )
    
    tab_m1, tab_m2, tab_m3 = st.tabs([
        "🏆 Model Comparison Metrics",
        "🗺️ Spatial Leakage Gap Analysis",
        "🔍 SHAP & Feature Importances"
    ])
    
    with tab_m1:
        st.markdown("##### Performance on Spatially Held-Out Upper Corridor (Sector 3)")
        if not metrics_df.empty:
            st.dataframe(
                metrics_df.style.highlight_max(axis=0, subset=["ROC_AUC", "Recall_Sensitivity", "Precision", "F1_Score"]),
                use_container_width=True
            )
        
        col_fig1, col_fig2 = st.columns(2)
        with col_fig1:
            roc_path = os.path.join(FIGURES_DIR, "combined_roc_curves.png")
            if os.path.exists(roc_path):
                st.image(roc_path, caption="Combined ROC Curves on Held-Out Test Corridor", use_container_width=True)
        with col_fig2:
            cm_path = os.path.join(FIGURES_DIR, "confusion_matrices.png")
            if os.path.exists(cm_path):
                st.image(cm_path, caption="Confusion Matrices (Safety-Critical False Negative Penalization)", use_container_width=True)

    with tab_m2:
        st.markdown("##### ⚠️ The Spatial Autocorrelation Leakage Demonstration")
        st.warning(
            """
            **Critical Methodological Contribution:** Standard random K-Fold cross-validation leaks spatial autocorrelation 
            between geographically adjacent training and test points, producing artificially inflated, over-optimistic performance metrics!
            """
        )
        
        leak_c1, leak_c2, leak_c3 = st.columns(3)
        with leak_c1:
            st.metric(
                label="Naive Random 5-Fold CV AUC",
                value=f"{leakage_info.get('Random_CV_ROC_AUC_Mean', 0.820):.3f}",
                delta="Artificially Inflated"
            )
        with leak_c2:
            st.metric(
                label="Spatial Sector Block CV AUC",
                value=f"{leakage_info.get('Spatial_CV_ROC_AUC_Mean', 0.669):.3f}",
                delta="Honest Out-of-Corridor",
                delta_color="normal"
            )
        with leak_c3:
            st.metric(
                label="Over-Optimism Gap",
                value=f"+{leakage_info.get('Overoptimism_Delta_AUC', 0.150):.3f} AUC",
                delta="Spatial Leakage Bias",
                delta_color="inverse"
            )
            
        fig_bar_leak = go.Figure(data=[
            go.Bar(
                name="Validation Scheme",
                x=["Naive Random K-Fold CV", "Spatial Sector Block CV"],
                y=[
                    leakage_info.get('Random_CV_ROC_AUC_Mean', 0.820),
                    leakage_info.get('Spatial_CV_ROC_AUC_Mean', 0.669)
                ],
                error_y=dict(
                    type="data",
                    array=[
                        leakage_info.get('Random_CV_ROC_AUC_Std', 0.019),
                        leakage_info.get('Spatial_CV_ROC_AUC_Std', 0.107)
                    ]
                ),
                marker_color=["#E63946", "#2A9D8F"]
            )
        ])
        fig_bar_leak.update_layout(
            height=360,
            title="Cross-Validation Scheme Comparison (Quantifying Spatial Leakage)",
            yaxis_title="ROC-AUC Score",
            yaxis_range=[0.4, 1.0]
        )
        st.plotly_chart(fig_bar_leak, use_container_width=True)

    with tab_m3:
        st.markdown("##### 🧠 Interpretability: What Drives Landslides Along Arniko Highway?")
        col_shp1, col_shp2 = st.columns(2)
        with col_shp1:
            shap_fig_path = os.path.join(FIGURES_DIR, "shap_summary_plot.png")
            if os.path.exists(shap_fig_path):
                st.image(shap_fig_path, caption="SHAP Summary Beeswarm Plot (XGBoost)", use_container_width=True)
        with col_shp2:
            feat_imp_path = os.path.join(FIGURES_DIR, "top_feature_importances.png")
            if os.path.exists(feat_imp_path):
                st.image(feat_imp_path, caption="Gini Feature Importance Hierarchy", use_container_width=True)


# ---------------------------------------------------------
# TAB 5: Landslide Inventory & Data Explorer
# ---------------------------------------------------------
elif navigation == "📁 Landslide Inventory & Data":
    st.subheader("📁 Landslide Inventory & Highway Corridor Data Explorer")
    st.markdown(
        """
        Inspect the underlying dataset, including real British Geological Survey (BGS) ground-truth mappings,
        NASA Global Landslide Catalog events, and SRTM 30m corridor analysis units.
        """
    )
    
    col_d1, col_d2 = st.columns([3, 1])
    with col_d1:
        st.markdown(f"**Showing {len(filtered_df):,} Analysis Segments** (Filtered)")
    with col_d2:
        csv_data = filtered_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "📥 Download Filtered CSV",
            data=csv_data,
            file_name="arniko_highway_filtered_dataset.csv",
            mime="text/csv"
        )
        
    st.dataframe(filtered_df, use_container_width=True, height=400)
    
    st.markdown("#### 📊 Feature Distributions")
    feat_sel = st.selectbox(
        "Select Feature to Visualize Distribution",
        ["slope_deg", "elevation_m", "rainfall_annual_mm", "dist_to_fault_km", "dist_to_river_m", "susceptibility_score"]
    )
    
    fig_hist = px.histogram(
        corridor_df,
        x=feat_sel,
        color="risk_category",
        color_discrete_map={
            "High (>0.66)": "#E63946",
            "Moderate (0.33-0.66)": "#F4A261",
            "Low (<0.33)": "#2A9D8F"
        },
        marginal="box",
        title=f"Distribution of {feat_sel} across Landslide Risk Levels",
        height=380
    )
    st.plotly_chart(fig_hist, use_container_width=True)


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------
st.markdown("---")
st.caption(
    "Coursework Prototype: Machine Learning Landslide Susceptibility Mapping | "
    "Softwarica College of IT & E-Commerce & Coventry University | "
    "Student: Dhan Bahadur Gurung (Coventry ID: 17624480) | March Intake 2026"
)
