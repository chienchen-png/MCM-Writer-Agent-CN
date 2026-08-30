# VS Code Webview 修复脚本
# 请在关闭所有 VS Code 窗口后运行此脚本

$codeData = "$env:APPDATA\Code"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  VS Code Webview 缓存清理工具" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 检查 VS Code 是否还在运行
$vsRunning = Get-Process code -ErrorAction SilentlyContinue
if ($vsRunning) {
    Write-Host "⚠ VS Code 仍在运行！请关闭所有 VS Code 窗口后重试。" -ForegroundColor Red
    Write-Host "进程列表:" -ForegroundColor Yellow
    $vsRunning | Format-Table Id, StartTime
    Write-Host ""
    $answer = Read-Host "是否强制关闭所有 VS Code 进程？(Y/N)"
    if ($answer -eq 'Y' -or $answer -eq 'y') {
        $vsRunning | Stop-Process -Force
        Write-Host "已关闭所有 VS Code 进程。" -ForegroundColor Green
        Start-Sleep -Seconds 2
    } else {
        Write-Host "请手动关闭后重新运行此脚本。" -ForegroundColor Yellow
        exit
    }
}

# 要清理的目录列表
$dirsToClean = @(
    "Service Worker",
    "Cache",
    "CachedData",
    "GPUCache",
    "DawnGraphiteCache",
    "DawnWebGPUCache",
    "Code Cache",
    "WebStorage"
)

foreach ($dir in $dirsToClean) {
    $fullPath = Join-Path $codeData $dir
    if (Test-Path $fullPath) {
        try {
            Remove-Item -Path $fullPath -Recurse -Force -ErrorAction Stop
            Write-Host "✓ 已清理: $dir" -ForegroundColor Green
        } catch {
            Write-Host "✗ 清理失败: $dir - $_" -ForegroundColor Red
        }
    } else {
        Write-Host "- 跳过（不存在）: $dir" -ForegroundColor Gray
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  清理完成！请重新打开 VS Code" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan

Read-Host "按 Enter 退出"
