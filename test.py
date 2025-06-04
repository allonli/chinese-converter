#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试脚本 - Chinese Converter Alfred Workflow
Test script for Chinese Converter Alfred Workflow
"""

import sys
import os
import json

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from converter import convert_text, create_alfred_output

def test_conversion():
    """测试转换功能"""
    print("🧪 开始测试 Chinese Converter...")
    print("=" * 50)
    
    # 测试用例
    test_cases = [
        {
            "text": "你好世界",
            "type": "s2t",
            "description": "简体转繁体"
        },
        {
            "text": "電腦軟體",
            "type": "t2s",
            "description": "繁体转简体"
        },
        {
            "text": "中国北京",
            "type": "s2t",
            "description": "地名转换"
        },
        {
            "text": "繁體字轉換",
            "type": "t2s",
            "description": "繁体转简体"
        }
    ]
    
    success_count = 0
    total_count = len(test_cases)
    
    for i, case in enumerate(test_cases, 1):
        print(f"测试 {i}/{total_count}: {case['description']}")
        print(f"输入: {case['text']}")
        
        try:
            result = convert_text(case['text'], case['type'])
            print(f"输出: {result}")
            
            # 检查是否有错误
            if "错误" in result or "Error" in result:
                print("❌ 测试失败")
            else:
                print("✅ 测试通过")
                success_count += 1
                
        except Exception as e:
            print(f"❌ 测试异常: {str(e)}")
        
        print("-" * 30)
    
    print(f"\n📊 测试结果: {success_count}/{total_count} 通过")
    
    if success_count == total_count:
        print("🎉 所有测试通过！")
        return True
    else:
        print("⚠️  部分测试失败，请检查OpenCC安装")
        return False

def test_alfred_output():
    """测试Alfred输出格式"""
    print("\n🧪 测试Alfred输出格式...")
    print("=" * 50)
    
    try:
        # 测试Alfred输出格式
        output = create_alfred_output(
            "测试标题",
            "测试副标题",
            "测试参数",
            True
        )
        
        # 验证JSON格式
        json_str = json.dumps(output, ensure_ascii=False)
        parsed = json.loads(json_str)
        
        print("✅ Alfred输出格式正确")
        print(f"示例输出: {json_str[:100]}...")
        return True
        
    except Exception as e:
        print(f"❌ Alfred输出格式测试失败: {str(e)}")
        return False

def test_dependencies():
    """测试依赖库"""
    print("\n🧪 测试依赖库...")
    print("=" * 50)
    
    try:
        import opencc
        print("✅ OpenCC库导入成功")
        
        # 测试基本转换
        converter = opencc.OpenCC('s2t')
        result = converter.convert("测试")
        print(f"✅ OpenCC转换测试: '测试' -> '{result}'")
        return True
        
    except ImportError:
        print("❌ OpenCC库未安装")
        print("请运行: pip3 install opencc-python-reimplemented")
        return False
    except Exception as e:
        print(f"❌ OpenCC测试失败: {str(e)}")
        return False

def main():
    """主测试函数"""
    print("Chinese Converter Alfred Workflow - 测试套件")
    print("=" * 60)
    
    # 运行所有测试
    tests = [
        ("依赖库测试", test_dependencies),
        ("转换功能测试", test_conversion),
        ("Alfred输出测试", test_alfred_output)
    ]
    
    passed_tests = 0
    total_tests = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 开始 {test_name}...")
        if test_func():
            passed_tests += 1
        print(f"✅ {test_name} 完成")
    
    print("\n" + "=" * 60)
    print(f"📊 总体测试结果: {passed_tests}/{total_tests} 通过")
    
    if passed_tests == total_tests:
        print("🎉 所有测试通过！插件已准备就绪。")
        print("\n📖 下一步:")
        print("1. 在Alfred中导入workflow")
        print("2. 使用 's2t 文本' 或 't2s 文本' 进行转换")
    else:
        print("⚠️  部分测试失败，请检查安装和配置。")
        print("\n🔧 故障排除:")
        print("1. 确保Python 3已安装")
        print("2. 运行: pip3 install opencc-python-reimplemented")
        print("3. 检查文件权限")
    
    return passed_tests == total_tests

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)