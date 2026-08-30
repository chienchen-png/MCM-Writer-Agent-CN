# 阶段一执行前/后文件状态快照脚本
param(
    [string]$OutFile = "$env:TEMP\mcm_stage1_before.txt"
)
$root = 'E:\项目\开发\MCM agent'
$lines = Get-ChildItem $root -Recurse -File | Where-Object { $_.FullName -notmatch '\\\.venv\\' } | ForEach-Object {
    $rel = $_.FullName.Substring($root.Length + 1)
    $h = (Get-FileHash $_.FullName -Algorithm MD5).Hash.Substring(0, 8)
    "$rel|$h|$($_.Length)"
}
$lines | Sort-Object | Set-Content $OutFile -Encoding UTF8
Write-Host "快照已保存: $OutFile (共 $($lines.Count) 个文件)"
