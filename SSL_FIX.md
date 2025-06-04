# SSL证书验证失败解决方案

如果你遇到以下错误信息：
```
WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1028)'))': /simple/opencc-python-reimplemented/
```

这是由于SSL证书验证失败导致的，以下是几种解决方案：

## 方案1: 使用trusted-host参数（推荐）

```bash
pip3 install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org opencc-python-reimplemented
```

## 方案2: 使用国内镜像源

```bash
# 清华大学镜像源
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn opencc-python-reimplemented

# 或者使用阿里云镜像源
pip3 install -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com opencc-python-reimplemented

# 或者使用豆瓣镜像源
pip3 install -i https://pypi.douban.com/simple/ --trusted-host pypi.douban.com opencc-python-reimplemented
```

## 方案3: 升级pip和证书

```bash
# 升级pip到最新版本
pip3 install --upgrade pip

# 在macOS上更新证书
/Applications/Python\ 3.x/Install\ Certificates.command

# 然后重新安装
pip3 install opencc-python-reimplemented
```

## 方案4: 配置pip.conf文件（永久解决）

创建或编辑pip配置文件：

```bash
# 创建配置目录
mkdir -p ~/.pip

# 创建配置文件
cat > ~/.pip/pip.conf << EOF
[global]
trusted-host = pypi.org
               pypi.python.org
               files.pythonhosted.org
               pypi.tuna.tsinghua.edu.cn
index-url = https://pypi.tuna.tsinghua.edu.cn/simple/
EOF
```

## 方案5: 临时禁用SSL验证（不推荐）

⚠️ **注意：此方法存在安全风险，仅在其他方法都失败时使用**

```bash
pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org --cert /dev/null opencc-python-reimplemented
```

## macOS特定解决方案

如果你使用的是macOS，可能需要安装或更新证书：

```bash
# 方法1: 运行Python证书安装脚本
/Applications/Python\ 3.x/Install\ Certificates.command

# 方法2: 使用brew安装ca-certificates
brew install ca-certificates

# 方法3: 更新macOS系统证书
sudo /usr/bin/security update-ca-trust
```

## 企业网络环境

如果你在企业网络环境中，可能需要配置代理：

```bash
# 设置HTTP代理
export http_proxy=http://proxy.company.com:8080
export https_proxy=http://proxy.company.com:8080

# 然后安装
pip3 install opencc-python-reimplemented
```

## 验证安装

安装完成后，可以验证是否成功：

```python
# 测试导入
python3 -c "import opencc; print('OpenCC安装成功!')"

# 测试转换
python3 -c "import opencc; cc = opencc.OpenCC('s2t'); print(cc.convert('简体中文'))"
```

## 自动化脚本

项目中的 `install.sh` 脚本已经包含了这些解决方案，会自动尝试不同的安装方法：

```bash
./install.sh
```

## 如果问题仍然存在

1. 检查网络连接
2. 确认Python和pip版本
3. 尝试重启终端
4. 检查防火墙设置
5. 联系网络管理员（企业环境）

## 相关链接

- [pip官方文档](https://pip.pypa.io/en/stable/)
- [Python证书问题解决](https://stackoverflow.com/questions/25981703/pip-install-fails-with-connection-error-ssl-certificate-verify-failed-certi)
- [OpenCC项目主页](https://github.com/BYVoid/OpenCC)