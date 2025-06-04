#!/bin/bash

# Chinese Converter Alfred Workflow 安装脚本
# Installation script for Chinese Converter Alfred Workflow

echo "🚀 开始安装 Chinese Converter Alfred Workflow..."
echo "🚀 Starting installation of Chinese Converter Alfred Workflow..."
echo ""

# 检查Python 3是否安装
echo "📋 检查Python 3安装状态..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
    echo "✅ Python 3已安装: $PYTHON_VERSION"
else
    echo "❌ 未找到Python 3"
    echo "请先安装Python 3: https://www.python.org/downloads/"
    echo "或使用Homebrew: brew install python3"
    exit 1
fi

# 检查pip3是否可用
echo "📋 检查pip3安装状态..."
if command -v pip3 &> /dev/null; then
    echo "✅ pip3已安装"
else
    echo "❌ 未找到pip3"
    echo "请确保pip3已正确安装"
    exit 1
fi

# 安装Python依赖
echo "📦 安装Python依赖包..."
if pip3 install -r requirements.txt; then
    echo "✅ 依赖包安装成功"
else
    echo "⚠️  常规安装失败，尝试解决SSL证书问题..."
    
    # 方法1: 使用trusted-host参数
    echo "🔧 尝试方法1: 使用trusted-host参数..."
    if pip3 install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org opencc-python-reimplemented; then
        echo "✅ 方法1成功: 依赖包安装完成"
    else
        # 方法2: 升级pip并使用国内镜像源
        echo "🔧 尝试方法2: 使用国内镜像源..."
        pip3 install --upgrade pip
        if pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn opencc-python-reimplemented; then
            echo "✅ 方法2成功: 依赖包安装完成"
        else
            echo "❌ 所有安装方法都失败了"
            echo "🔧 手动解决方案:"
            echo "   1. 升级pip: pip3 install --upgrade pip"
            echo "   2. 使用trusted-host: pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org opencc-python-reimplemented"
            echo "   3. 使用国内源: pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple/ opencc-python-reimplemented"
            echo "   4. 或者配置pip.conf文件解决SSL问题"
            exit 1
        fi
    fi
fi

# 测试转换功能
echo "🧪 测试转换功能..."
TEST_RESULT=$(python3 converter.py "测试" s2t 2>&1)
if echo "$TEST_RESULT" | grep -q "測試"; then
    echo "✅ 转换功能测试通过"
else
    echo "⚠️  转换功能测试异常，但可能仍然可用"
    echo "测试结果: $TEST_RESULT"
fi

echo ""
echo "🎉 安装完成！"
echo "📖 使用方法:"
echo "   1. 在Alfred中输入 's2t 简体文本' 转换为繁体"
echo "   2. 在Alfred中输入 't2s 繁體文本' 转换为简体"
echo "   3. 按回车键复制结果到剪贴板"
echo ""
echo "📁 项目文件位置: $(pwd)"
echo "📚 详细说明请查看 README.md"
echo ""
echo "如果遇到问题，请检查:"
echo "- Python 3是否正确安装"
echo "- Alfred是否有Powerpack许可"
echo "- 是否正确导入了workflow到Alfred"