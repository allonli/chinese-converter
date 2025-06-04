#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chinese Converter for Alfred Workflow
使用OpenCC进行繁简体字转换的Alfred插件

Author: Alfred Workflow
Version: 1.0
"""

import sys
import json
import subprocess
import os

def install_opencc():
    """安装OpenCC库"""
    try:
        # 首先尝试正常安装
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'opencc-python-reimplemented'])
        return True
    except subprocess.CalledProcessError:
        try:
            # 如果SSL证书验证失败，尝试使用trusted-host参数
            subprocess.check_call([
                sys.executable, '-m', 'pip', 'install', 
                '--trusted-host', 'pypi.org',
                '--trusted-host', 'pypi.python.org', 
                '--trusted-host', 'files.pythonhosted.org',
                'opencc-python-reimplemented'
            ])
            return True
        except subprocess.CalledProcessError:
            try:
                # 最后尝试升级pip并使用国内镜像源
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
                subprocess.check_call([
                    sys.executable, '-m', 'pip', 'install', 
                    '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple/',
                    '--trusted-host', 'pypi.tuna.tsinghua.edu.cn',
                    'opencc-python-reimplemented'
                ])
                return True
            except subprocess.CalledProcessError:
                return False

def convert_text(text, conversion_type):
    """转换文本
    
    Args:
        text (str): 要转换的文本
        conversion_type (str): 转换类型 ('s2t' 或 't2s')
    
    Returns:
        str: 转换后的文本
    """
    try:
        import opencc
    except ImportError:
        # 尝试安装OpenCC
        if install_opencc():
            import opencc
        else:
            return "错误: 无法安装OpenCC库，请手动安装: pip install opencc-python-reimplemented"
    
    try:
        if conversion_type == 's2t':
            # 简体转繁体
            converter = opencc.OpenCC('s2t')
        elif conversion_type == 't2s':
            # 繁体转简体
            converter = opencc.OpenCC('t2s')
        else:
            return "错误: 不支持的转换类型"
        
        result = converter.convert(text)
        return result
    except Exception as e:
        return f"转换错误: {str(e)}"

def detect_script_type(text):
    """检测文本是简体还是繁体
    
    Args:
        text (str): 要检测的文本
    
    Returns:
        str: 's' 表示简体，'t' 表示繁体，'unknown' 表示无法确定
    """
    try:
        import opencc
    except ImportError:
        # 如果没有opencc，使用简单的字符检测
        traditional_chars = set('電腦軟體網絡資訊處理機構組織環境開發設計實現應用系統數據庫網站頁面內容管理員用戶註冊登錄密碼確認驗證郵箱地址電話號碼時間日期年月週星期選擇確定取消返回首頁導航菜單搜索結果顯示隱藏編輯刪除添加修改保存提交發送接收下載上傳文件圖片視頻音頻文檔報告統計分析圖表數據信息詳細簡介說明幫助支持聯繫關於版權隱私條款服務協議')
        simplified_chars = set('电脑软体网络资讯处理机构组织环境开发设计实现应用系统数据库网站页面内容管理员用户注册登录密码确认验证邮箱地址电话号码时间日期年月周星期选择确定取消返回首页导航菜单搜索结果显示隐藏编辑删除添加修改保存提交发送接收下载上传文件图片视频音频文档报告统计分析图表数据信息详细简介说明帮助支持联系关于版权隐私条款服务协议')
        
        text_chars = set(text)
        traditional_count = len(text_chars & traditional_chars)
        simplified_count = len(text_chars & simplified_chars)
        
        if traditional_count > simplified_count:
            return 't'
        elif simplified_count > traditional_count:
            return 's'
        else:
            return 'unknown'
    
    try:
        # 使用OpenCC进行更准确的检测
        s2t_converter = opencc.OpenCC('s2t')
        t2s_converter = opencc.OpenCC('t2s')
        
        # 转换为繁体，如果没有变化说明原文可能是繁体
        s2t_result = s2t_converter.convert(text)
        # 转换为简体，如果没有变化说明原文可能是简体
        t2s_result = t2s_converter.convert(text)
        
        # 如果简体转繁体有变化，说明原文是简体
        if s2t_result != text:
            return 's'
        # 如果繁体转简体有变化，说明原文是繁体
        elif t2s_result != text:
            return 't'
        else:
            # 如果都没有变化，可能是混合文本或者不包含繁简差异字符
            return 'unknown'
    except Exception:
        return 'unknown'

def auto_convert_text(text):
    """自动检测并转换文本
    
    Args:
        text (str): 要转换的文本
    
    Returns:
        str: 转换后的文本
    """
    script_type = detect_script_type(text)
    
    if script_type == 's':
        # 简体转繁体
        return convert_text(text, 's2t')
    elif script_type == 't':
        # 繁体转简体
        return convert_text(text, 't2s')
    else:
        # 无法确定，默认简体转繁体
        return convert_text(text, 's2t')

def create_alfred_output(title, subtitle="", arg="", valid=True):
    """创建Alfred输出格式
    
    Args:
        title (str): 主标题
        subtitle (str): 副标题
        arg (str): 传递给下一个动作的参数
        valid (bool): 是否可以执行
    
    Returns:
        dict: Alfred格式的输出
    """
    return {
        "items": [{
            "title": title,
            "subtitle": subtitle,
            "arg": arg,
            "valid": valid,
            "text": {
                "copy": title,
                "largetype": title
            }
        }]
    }

def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("请输入要转换的文本")
        return
    
    text = sys.argv[1]
    
    if not text.strip():
        print("请输入要转换的文本")
        return
    
    # 自动检测并转换
    converted_text = auto_convert_text(text)
    
    # 直接输出转换后的文本
    print(converted_text)

if __name__ == "__main__":
    main()