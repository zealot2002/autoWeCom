@echo off
setlocal EnableDelayedExpansion

:: 帮助信息
if "%1"=="-h" goto :help
if "%1"=="--help" goto :help
goto :main

:help
echo 使用方法: send_wechat_message.bat [联系人] [消息内容]
echo 例子:
echo   send_wechat_message.bat                             # 使用默认联系人和消息
echo   send_wechat_message.bat "张三"                      # 给张三发送默认消息
echo   send_wechat_message.bat "张三" "你好啊"            # 给张三发送自定义消息
echo   send_wechat_message.bat "" "只想修改消息内容"       # 使用默认联系人但自定义消息
exit /b 0

:main
:: 设置默认值
set "CONTACT=文件传输助手"
set "MESSAGE=123"

:: 处理联系人参数
if not "%1"=="" (
    set "CONTACT=%~1"
)

:: 处理消息内容参数
if not "%2"=="" (
    set "MESSAGE=%~2"
) else (
    if not "%1"=="" (
        if not "%1"=="-c" (
            if not "%1"=="--contact" (
                :: 如果只提供了一个参数且不是联系人标志，默认为消息内容
                set "MESSAGE=%~1"
                set "CONTACT=文件传输助手"
            )
        )
    )
)

echo 联系人: %CONTACT%
echo 消息内容: %MESSAGE%

:: 获取脚本所在目录
set "SCRIPT_DIR=%~dp0"
echo 脚本目录: %SCRIPT_DIR%

:: 运行Robot Framework脚本，并传递变量
python -m robot --variable CONTACT:"%CONTACT%" --variable MESSAGE:"%MESSAGE%" "%SCRIPT_DIR%\wechat_automation_workflow.robot"

echo 消息已发送完成!
exit /b 0 