*** Settings ***
Documentation     微信完整自动化流程 (Windows版本)
...               自动搜索联系人并发送消息
Library           Process
Library           OperatingSystem
Library           Collections
Library           DateTime
Library           String
Library           PyAutoGUI

*** Variables ***
${LOG_FILE}       ${CURDIR}/wechat_windows_log.txt
${MESSAGE}        123    # 默认消息内容
${CONTACT}        文件传输助手    # 默认联系人
${DEBUG_MODE}     True    # 开启更详细的日志记录
${SCRIPTS_DIR}    ${CURDIR}    # 脚本目录

*** Tasks ***
完整微信Windows自动化工作流
    创建日志文件
    ${scripts_ok}=    检查并安装依赖
    Run Keyword If    ${scripts_ok}    执行基于PyAutoGUI的微信自动化    ${CONTACT}    ${MESSAGE}
    ...    ELSE    Log To Console    \n无法执行自动化：缺少必要的依赖项\n
    记录完成信息

*** Keywords ***
检查并安装依赖
    记录日志    检查自动化依赖工具
    
    # 检查PyAutoGUI是否已安装
    ${py_result}=    Run Process    python -c "import sys, pkgutil; sys.exit(0 if pkgutil.find_loader('pyautogui') else 1)"    shell=True
    ${has_pyautogui}=    Evaluate    ${py_result.rc} == 0
    
    IF    not ${has_pyautogui}
        记录日志    PyAutoGUI未安装，尝试安装...
        ${install_result}=    Run Process    pip install pyautogui    shell=True
        ${install_success}=    Evaluate    ${install_result.rc} == 0
        IF    not ${install_success}
            记录日志    错误: 无法安装PyAutoGUI: ${install_result.stderr}
            Log To Console    \n错误: 无法安装PyAutoGUI，请手动安装: pip install pyautogui\n
            RETURN    ${False}
        END
        记录日志    成功安装PyAutoGUI
    ELSE
        记录日志    已安装PyAutoGUI，可以继续自动化
    END
    
    # 检查企业微信是否已安装 (简化检查，仅检查默认安装路径)
    ${wechat_path}=    Set Variable    C:\\Program Files (x86)\\WXWork\\WXWork.exe
    ${wechat_exists}=    Run Keyword And Return Status    File Should Exist    ${wechat_path}
    
    IF    not ${wechat_exists}
        记录日志    警告: 未在默认路径找到企业微信，请确保已正确安装企业微信
        Log To Console    \n警告: 未在默认路径找到企业微信，请确保已正确安装企业微信\n
    ELSE
        记录日志    企业微信已安装在默认路径
    END
    
    RETURN    ${True}
    
创建日志文件
    ${timestamp}=    Get Current Date    result_format=%Y-%m-%d %H:%M:%S
    Create File    ${LOG_FILE}    # 微信自动化工作流日志 (Windows版本)\n# 开始时间: ${timestamp}\n\n

记录日志
    [Arguments]    ${message}
    ${timestamp}=    Get Current Date    result_format=%Y-%m-%d %H:%M:%S
    ${log_entry}=    Catenate    SEPARATOR=\n    [${timestamp}] ${message}
    Append To File    ${LOG_FILE}    ${log_entry}\n
    Log To Console    ${log_entry}

执行基于PyAutoGUI的微信自动化
    [Arguments]    ${target_contact}=文件传输助手    ${custom_message}=123
    记录日志    步骤1: 启动企业微信
    记录日志    联系人: "${target_contact}"
    记录日志    将发送的消息内容: "${custom_message}"
    
    # 启动企业微信
    ${result1}=    Run Process    start "C:\\Program Files (x86)\\WXWork\\WXWork.exe"    shell=True
    Sleep    3s    # 等待企业微信启动
    
    记录日志    步骤2: 搜索联系人 "${target_contact}"
    TRY
        # 点击搜索框
        记录日志    点击搜索框
        Import Library    PyAutoGUI
        PyAutoGUI.Click    x=200    y=50
        Sleep    0.5s
        
        # 输入联系人
        记录日志    输入联系人名称: ${target_contact}
        PyAutoGUI.Write    ${target_contact}
        Sleep    1s
        PyAutoGUI.Press    enter
        Sleep    1s
        
        记录日志    步骤3: 输入消息
        # 点击输入框
        PyAutoGUI.Click    x=400    y=500
        Sleep    0.5s
        
        # 输入消息
        记录日志    输入消息内容: ${custom_message}
        PyAutoGUI.Write    ${custom_message}
        Sleep    0.5s
        
        记录日志    步骤4: 发送消息
        PyAutoGUI.Press    enter
        Sleep    0.5s
        
        记录日志    消息发送完成
        RETURN    ${True}
    EXCEPT    AS    ${error}
        记录日志    错误: 自动化执行失败: ${error}
        Log To Console    \n错误: 自动化执行失败\n
        RETURN    ${False}
    END

记录完成信息
    ${timestamp}=    Get Current Date    result_format=%Y-%m-%d %H:%M:%S
    记录日志    自动化流程完成。结束时间: ${timestamp}
    记录日志    --------------------------------------------------
    
    # 显示日志文件位置
    ${log_path}=    Normalize Path    ${LOG_FILE}
    Log    日志文件已保存至: ${log_path}
    Log To Console    \n日志文件已保存至: ${log_path} 