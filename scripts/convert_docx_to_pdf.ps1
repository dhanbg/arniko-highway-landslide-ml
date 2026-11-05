$ErrorActionPreference = "Stop"

$baseDir = "C:\Users\Administrator\Documents\college"
$sourceDocx = Join-Path $baseDir "submission\DhanBahadurGurung_17624480.docx"
$targetPdfRoot = Join-Path $baseDir "DhanBahadurGurung_17624480.pdf"
$targetPdfSub = Join-Path $baseDir "submission\DhanBahadurGurung_17624480.pdf"

Write-Output "Converting Word Document to PDF via Microsoft Word COM..."
Write-Output "Source: $sourceDocx"

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.ScreenUpdating = $false

try {
    $doc = $word.Documents.Open($sourceDocx, $false, $true) # Open ReadOnly
    
    # 17 = wdExportFormatPDF
    Write-Output "Exporting to $targetPdfRoot..."
    $doc.ExportAsFixedFormat($targetPdfRoot, 17)
    
    Write-Output "Exporting to $targetPdfSub..."
    $doc.ExportAsFixedFormat($targetPdfSub, 17)
    
    $doc.Close([ref]$false)
    Write-Output "SUCCESS: PDF successfully generated!"
}
catch {
    Write-Error "Conversion failed: $_"
}
finally {
    $word.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
    [System.GC]::Collect()
    [System.GC]::WaitForPendingFinalizers()
}

