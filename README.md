# 火山方舟野生应用 - 多模型 API 调用工具

这是一款基于火山方舟平台构建的野生应用，提供简洁高效的多模型 API 调用体验。

## 核心功能

### 🔹 文本推理
- 支持 Doubao-pro/lite、DeepSeek-R1 等主流模型
- 多模态交互（文本+图片理解）
- 流式输出、思考模式、并发控制

### 🔹 多模型对比
- 同时调用多个文本/图像模型进行实时对比
- 多路流式输出，直观比较响应速度与质量

### 🔹 图像生成
- 集成 Seedream 和即梦 AI 生图能力
- 支持文生图、图生图，批量生成与导出

### 🔹 视频生成
- 文生视频、图生视频支持
- 自定义时长、比例、分辨率

### 🔹 联网问答
- 基于 FeedCoop API 的智能搜索问答
- 支持自定义 Bot 配置

## 技术栈

- **后端**：Python 3.12+, FastAPI
- **前端**：HTML/CSS/JS + Jinja2
- **核心依赖**：requests, pillow, openpyxl

## 快速开始

### 1. 安装依赖
```bash
pip install fastapi uvicorn requests pillow openpyxl jinja2 python-multipart
```

### 2. 配置环境变量
```bash
# 火山方舟 API Key (必需)
export ARK_API_KEY="your-ark-api-key"

# 可选配置
# export JIMENG_ACCESS_KEY="your-jimeng-access-key"
# export NETWORK_QA_BEARER_TOKEN="your-token"
```

### 3. 启动服务
```bash
python -m uvicorn server:app --host 0.0.0.0 --port 8000 --reload
```

访问：`http://localhost:8000`

## 项目结构

```
.
├── server.py     # FastAPI 服务入口
├── config.py     # 配置文件
├── templates/    # HTML 模板
└── static/       # 静态资源
```

## 注意事项

- 临时文件自动清理（1小时过期）
- 内置 QPS 控制与并发管理
- 新模型需在 `config.py` 中配置
