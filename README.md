# Bu-ICPX - ICP查询工具

## 项目介绍
Bu-ICPX 是一个基于 Python 开发的 ICP 查询工具，支持手动查询和批量查询域名的 ICP 备案信息，并将结果保存为 CSV 文件。

## 功能特性
- ✅ 手动查询单个域名的 ICP 信息
- ✅ 批量查询多个域名的 ICP 信息
- ✅ 自动去重域名列表
- ✅ 结果保存为 CSV 文件
- ✅ 友好的命令行界面
- ✅ 彩色输出
- ✅ 错误处理和异常捕获
- ✅ 自动创建 targets.txt 文件

## 环境要求
- Python 3.6+
- 依赖库：
  - requests
  - rich

## 快速使用（下载Release）

如果您不想配置 Python 环境，可以直接下载 Release 版本的压缩包：

1. 进入 [Releases](https://github.com/Bu7terf1y/Bu-ICPX/releases) 页面
2. 下载最新版本的 `Bu-ICPX.zip` 压缩包
3. 解压到任意目录
4. 双击运行 `Bu-ICPX.exe`
5. 开始使用！

> 注意：首次运行可能会出现安全提示，点击"仍要运行"即可。

## 安装步骤（源码运行）

### 1. 克隆项目
```bash
git clone https://github.com/Bu7terf1y/Bu-ICPX.git
cd Bu-ICPX
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 运行工具
```bash
python Bu-ICPX.py
```

## 使用方法

### 手动查询
1. 运行工具后，选择 `1.手动查询`
2. 输入要查询的域名（例如：baidu.com）
3. 查看查询结果

### 批量查询
1. 在 `targets.txt` 文件中添加要查询的域名，每行一个
2. 运行工具后，选择 `2.批量查询`
3. 工具会自动查询所有域名的 ICP 信息
4. 结果会保存到 `results` 目录下的 CSV 文件中

## 目标文件格式
`targets.txt` 文件格式示例：
```
baidu.com
tencent.com
alibaba.com
example.com
```

## 结果文件
批量查询的结果会保存为 CSV 文件，路径为 `results/YYYY-MM-DD_HH-MM-SS.csv`，包含以下字段：
- 类型：网站类型
- ICP：ICP 备案号
- 单位：备案单位名称
- 域名：查询的域名
- 时间：备案时间

## 注意事项
1. 本工具使用第三方 API 进行 ICP 查询，请确保网络连接正常
2. 请勿频繁查询，以免触发 API 限制
3. 仅用于合法用途，遵守相关法律法规

## 技术实现
- 使用 `requests` 库进行网络请求
- 使用 `rich` 库实现彩色输出
- 使用 `csv` 库保存查询结果
- 使用 `os` 库进行文件操作
- 使用 `datetime` 库生成时间戳

## 项目结构
```
Bu-ICPX/
├── Bu-ICPX.py        # 主程序
├── targets.txt       # 目标域名文件
├── results/          # 结果保存目录
├── requirements.txt  # 依赖文件
└── README.md         # 项目说明
```

## 依赖文件
创建 `requirements.txt` 文件：
```
requests
rich
```

## 常见问题

### Q: 运行时提示缺少依赖库？
A: 请运行 `pip install -r requirements.txt` 安装所需依赖。

### Q: 批量查询结果为空？
A: 检查 `targets.txt` 文件是否为空，或域名格式是否正确。

### Q: 查询失败？
A: 可能是网络问题或 API 限制，请稍后重试。

## 许可证
本项目采用 MIT 许可证，详见 LICENSE 文件。

## 作者
- 作者：Bu7terf1y
- 项目地址：https://github.com/Bu7terf1y/Bu-ICPX

## 更新日志
- v1.0.0 (2026-04-13)：初始版本，支持手动查询和批量查询功能
