# Chinese Converter Alfred Workflow

一个用于在简体中文和繁体中文之间转换的Alfred插件，基于OpenCC库实现。

## 功能特性

- 🤖 智能识别简体/繁体，自动转换
- 🔄 简体中文 ⇄ 繁体中文 双向转换
- ⚡ 快速响应，实时转换
- 🎯 支持自定义快捷键（推荐 Command+P）
- 🛠 自动安装依赖库

## 安装要求

- macOS
- Alfred 4+ (需要Powerpack)
- Python 3.6+
- OpenCC库 (插件会自动安装)

## 安装步骤

1. **下载插件**
   - 下载整个项目文件夹
   - 或者克隆仓库: `git clone <repository-url>`

2. **安装依赖**
   ```bash
   cd chinese-converter
   pip3 install -r requirements.txt
   ```

3. **导入Alfred**
   - 双击 `info.plist` 文件
   - 或者在Alfred Preferences中导入workflow

## 使用方法

### 智能自动转换
脚本会自动检测输入文本的字体类型，并转换为相应的目标字体：

- **输入简体** → 自动转换为繁体
- **输入繁体** → 自动转换为简体

```
# 简体转繁体示例
电脑软件 → 電腦軟件

# 繁体转简体示例
電腦軟體 → 电脑软体
```

## 使用示例

1. **选中任意中文文本**
2. **按 Command+P** (或你设置的快捷键)
3. **转换结果自动上屏替换原文本**

> 💡 **提示**: 推荐在Alfred设置中配置Command+P作为快捷键，可以快速转换选中的文本并自动替换。

## 技术实现

- **核心库**: OpenCC (Open Chinese Convert)
- **语言**: Python 3
- **智能检测**: 自动识别简体/繁体字符
- **输出格式**: 纯文本输出，支持直接替换
- **自动化**: 支持快捷键触发和文本替换

## 文件结构

```
chinese-converter/
├── info.plist          # Alfred workflow配置文件
├── converter.py        # 主要转换脚本
├── requirements.txt    # Python依赖
├── install.sh          # 自动安装脚本
├── test.py            # 测试脚本
├── SSL_FIX.md         # SSL问题解决方案
└── README.md          # 说明文档
```

## 故障排除

### 常见问题

1. **SSL证书验证失败**
   ```
   WARNING: Retrying after connection broken by 'SSLError(SSLCertVerificationError...)'
   ```
   **解决方案**:
   - 使用trusted-host参数: `pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org opencc-python-reimplemented`
   - 使用国内镜像源: `pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn opencc-python-reimplemented`
   - 详细解决方案请查看: [SSL_FIX.md](SSL_FIX.md)

2. **"错误: 无法安装OpenCC库"**
   - 手动安装: `pip3 install opencc-python-reimplemented`
   - 检查Python 3是否正确安装
   - 尝试使用不同的安装方法（见SSL_FIX.md）

3. **"python3: command not found"**
   - 安装Python 3: `brew install python3`
   - 或从官网下载: https://www.python.org/downloads/

4. **转换结果不正确**
   - 确保输入的是中文文本
   - 检查OpenCC库是否正确安装

### 调试模式

在终端中直接运行脚本进行调试:
```bash
cd /path/to/chinese-converter
python3 converter.py "测试文本"
```

脚本会自动检测文本类型并进行转换。

## 自定义配置

### 设置快捷键

推荐在Alfred中设置快捷键以便快速转换选中文本：
1. 打开Alfred Preferences
2. 进入Workflows，找到Chinese Converter
3. 设置Hotkey为 `Command+P` 或其他你喜欢的组合键
4. 配置为处理选中文本并自动替换

### 添加更多转换选项

OpenCC支持多种转换配置:
- `s2t.json` - 简体到繁体
- `t2s.json` - 繁体到简体
- `s2tw.json` - 简体到台湾正体
- `s2hk.json` - 简体到香港繁体
- `t2tw.json` - 繁体到台湾正体
- `t2hk.json` - 繁体到香港繁体

## 版本历史

- **v2.0** - 智能版本
  - 🆕 智能识别简体/繁体，自动转换
  - 🆕 支持快捷键触发和文本替换
  - 🆕 纯文本输出，无需手动指定转换方向
  - ✅ 移除s2t/t2s命令，简化使用

- **v1.0** - 初始版本
  - 支持简繁转换
  - 自动复制到剪贴板
  - 自动安装依赖

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request来改进这个插件。

## 相关链接

- [Alfred官网](https://www.alfredapp.com/)
- [OpenCC项目](https://github.com/BYVoid/OpenCC)
- [OpenCC Python实现](https://github.com/yichen0831/opencc-python)