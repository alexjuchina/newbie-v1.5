# 默认配置文件

import os

# =============================================================================
# 1. 通用配置
# =============================================================================
# 从环境变量获取API密钥
API_KEY = os.getenv('ARK_API_KEY')

# 版本信息
VERSION = "v1.5"
APP_NAME = "火山方舟豆包大模型调用工具"
FULL_VERSION = f"{APP_NAME} {VERSION}"

# =============================================================================
# 2. EP推理配置
# =============================================================================
# EP推理专用配置
EP_CONFIG = {
    'api_key': API_KEY,
    'model_ep': 'doubao-seed-1-8-251228', # 默认ep
    'temperature': 0.8,
    'top_p': 0.7,
    'max_tokens': 4094,
    'thinking_mode': 'disabled',
}

# EP模型端点清单（可选,数量不限）
MODEL_EP_OPTIONS = {
    "doubao-seed-1-8-251228": "Doubao-seed-1-8/251228",
    "ep-m-20251218160703-8vltr": "Doubao-seed-1-8/251215",
    "doubao-seed-1-6-251015": "Doubao-seed-1-6/251015",
    "doubao-seed-1-6-250615": "Doubao-seed-1-6/250615",
    "doubao-seed-1-6-flash-250828": "Doubao-seed-1-6-flash/250828",
    "doubao-seed-1-6-flash-250715": "Doubao-Seed-1.6-flash/250715",
    "doubao-seed-1-6-flash-250615": "Doubao-Seed-1.6-flash/250615",
    "doubao-1-5-pro-32k-250115": "Doubao-1.5-pro-32k/250115",
    "doubao-1-5-vision-pro-32k-250115": "Doubao-1.5-vision-pro-32k/250115",
    "deepseek-r1-250528": "DeepSeek-R1/250528"
}

# =============================================================================
# 3. 联网问答agent配置
# =============================================================================
# 从环境变量获取Bearer Token
NETWORK_QA_BEARER_TOKEN = os.getenv('NETWORK_QA_BEARER_TOKEN')
NETWORK_QA_BOT_ID = os.getenv('NETWORK_QA_BOT_ID')

NETWORK_QA_CONFIG = {
    'base_url': 'https://open.feedcoopapi.com/agent_api/agent/chat/completion',
    'bearer_token': NETWORK_QA_BEARER_TOKEN,
    'bot_id': NETWORK_QA_BOT_ID,
    'system_prompt': """你是一个AI助手。"""
}


# =============================================================================
# 5. 通用配置
# =============================================================================
# System Prompt（可选）
SYSTEM_PROMPT = """
```你的名字是豆包，有很强的专业性。用户在电脑上和你进行互动。

### 在回答知识类问题时，请遵照以下要求
1. 在细节程度上：
    - 围绕问题主体和用户需求，全面、深入地回答问题。
    - 提供详尽的背景信息和细节解释，对于复杂概念可使用案例、类比或示例来充分说明，目标是让用户深入理解和掌握相关概念。
    - 如果问题回答内容涉及范围较广、或者用户需求较为宽泛和不明确，可先提供一个概览性的回答，再将问题拆解为多个方面回答。 
    - 适当提供与问题主题相关的延伸内容，帮助用户获取更多有用信息。
2. 在格式上，使用markdown格式排版回复内容，包括但不限于：
     - 加粗：标题及关键信息加粗。
     - 列表：
        - 表达顺序关系时使用有序列表（1. 2. 3. ）。
        - 表达并列关系时使用无序列表（- xxx）。
        - 如果存在明确的上下层级关系，可以搭配使用标题（###）与列表甚至嵌套列表。
   - 表格：当对比多个维度时，使用表格进行排版，以便更清晰地呈现信息。
   - 灵活使用其他格式，以提高文本的可读性：
      - 引用：用于突出重要引用或参考内容。
      - 下划线：用于强调特定术语或短语。
      - 斜体：用于强调次要信息或表达语气。
      - 链接：用于提供外部参考资料或相关内容。
      
### 在写文案或进行内容创作时，请遵照以下要求：
1. 在篇幅长度上：
    - 围绕用户需求进行高质量的创作，提供丰富的描述，适度延展。
2. 在格式上
    - 默认情况下，使用自然段进行回复，除非用户有特殊要求。
    - 在需要排版的创作体裁中，使用markdown格式，合理使用分级标题、分级列表等排版。
    - 对标题、关键信息及关键句子适当使用加粗，以突出重点。

请注意，以上要求仅限于回答知识问答类和创作类的问题，对于数理逻辑、阅读理解等需求，或当提问涉及安全敏感时，请按照你习惯的方式回答。如果用户提问中明确指定了回复风格，也请优先满足用户需求。

### 当用户表达不满，提出投诉或补偿要求时，请遵照以下要求：
你不能向用户承诺任何形式的现金补偿、实物奖励、视频生成次数增加、专属特权，也不能表示工作人员会主动联系或在固定时间内响应。如用户表达不满、提出投诉或反馈请求，应以理解和引导为主，避免作出不符合产品政策的承诺。请坚持真实、中立、合规的表述方式。
  
### 知识截止日期说明
- 你的知识截止日期是2024年5月。
- 当用户询问当前事件或最新新闻时，你将根据截至2024年5月的知识为用户提供信息，并明确告知自该日期以来情况可能已发生变化。
- 对于2024年5月之后发生的任何说法，你既不会表示同意，也不会进行否认。
- 除非你的知识截止日期与用户的问题明确相关，否则你不会主动提及此截止日期。

"""

# =============================================================================
# 6. 图片生成配置
# =============================================================================
PICTURE_GENERATION_CONFIG = {
    'api_endpoint': 'https://ark.cn-beijing.volces.com/api/v3/images/generations',
    'api_key': API_KEY,  # 复用EP的api_key
    'default_size': '4K',  # 默认尺寸
    'default_i2i_size': '4K',  # 图生图默认尺寸
    'models': {
        "doubao-seedream-4-5-251128": "doubao-seedream-4-5-251128",
        "doubao-seedream-4-0-250828": "doubao-seedream-4-0-250828"
    },
    'sizes': {
        "1K(不支持4.5)": "1K",
        "2K": "2K",
        "4K": "4K",
        "1:1 (2048x2048)": "2048x2048",
        "1:1 (4096x4096)": "4096x4096",
        "4:3 (2304x1728)": "2304x1728",
        "3:4 (1728x2304)": "1728x2304",
        "16:9 (2560x1440)": "2560x1440",
        "9:16 (1440x2560)": "1440x2560",
        "3:2 (2496x1664)": "2496x1664",
        "2:3 (1664x2496)": "1664x2496",
        "21:9 (3024x1296)": "3024x1296"
    },
    'input_modes': {
        "文生图": "text_to_image",
        "图生图": "image_to_image"
    },
    # 图片提示词优化系统提示词
    'system_prompt': '''你是一个专业的图像提示词优化器，擅长把用户随意、简短、模糊的描述，扩展成专业、细致、结构化且可直接用于文本生成图像模型的提示词。
你不会改变用户描述的主体、风格方向或核心意图，只会在以下维度进行强化：
•	增加专业细节（材质、部件、装饰、结构、服饰、背景、灯光、氛围等）
•	保持语义明确，不做不必要的抽象延展
•	风格上可根据语境自动判断（现实、写实、手绘、科幻、古风、机械等），但不偏题
•	输出语言与用户输入一致
•	不出现模型名、参数、咒语式词汇
•	不改变人物身份与设定，只做专业化细化

当用户输入例如：
一个战士头部特写

你应该优化为：
一个战士的头部特写，佩戴兜鍪，红缨高束，凤翅眉庇张扬，肩吞紧贴盔甲，盾项护在颈后，细节清晰，极具武备感。

无论用户输入多简单，你都要始终保持专业、自然、细腻但不啰嗦的优化风格。

你的输出永远是：优化后的提示词文本本身，不解释，不分析，不分点，不多说一句废话。'''
}

# =============================================================================
# 7. 视频生成配置
# =============================================================================
VIDEO_GENERATION_CONFIG = {
    'api_endpoint': 'https://ark.cn-beijing.volces.com/api/v3/contents/generations/tasks',
    'api_key': API_KEY,  # 复用EP的api_key
    'default_ratio': '16:9',  # 默认比例
    'default_i2v_ratio': 'adaptive',  # 图生视频默认自适应比例
    'models': {
        "doubao-seedance-1-5-pro-251215": "doubao-seedance-1-5-pro-251215",
        "doubao-seedance-1-0-pro-fast-251015": "doubao-seedance-1-0-pro-fast-251015",
        "doubao-seedance-1-0-pro-250528": "doubao-seedance-1-0-pro-250528",
        "doubao-seedance-1-0-lite-t2v-250428": "doubao-seedance-1-0-lite-t2v-250428",
        "doubao-seedance-1-0-lite-i2v-250428": "doubao-seedance-1-0-lite-i2v-250428"
    },
    'durations': {
        "5秒": 5,
        "10秒": 10
    },
    'ratios': {
        "自适应": "adaptive",
        "16:9": "16:9",
        "9:16": "9:16",
        "1:1": "1:1",
        "4:3": "4:3",
        "3:4": "3:4"
    },
    'example_prompts': [
        "A girl is holding a fox. The girl opens her eyes and looks gently at the camera. The fox hugs her kindly. The camera slowly pulls back, and the girl's hair is blown by the wind. --ratio adaptive --dur 10",
        "未来城市，高楼大厦，飞行汽车，霓虹灯，赛博朋克风格，夜晚，下雨，反射，电影感，动态模糊 --ratio 16:9 --dur 10",
        "一只可爱的猫咪在草地上追逐蝴蝶，阳光明媚，微风轻拂，花朵摇曳，温馨治愈的画面 --ratio adaptive --dur 8",
        "山水画，中国古典，小桥流水，亭台楼阁，云雾缭绕，意境深远，水墨风格 --ratio 16:9 --dur 12"
    ]
}

# =============================================================================
# 8. 即梦AI配置
# =============================================================================
JIMENG_AI_CONFIG = {
    # 优先从环境变量获取，环境变量不存在则使用默认值
    'access_key': os.getenv('JIMENG_ACCESS_KEY'),
    'secret_key': os.getenv('JIMENG_SECRET_KEY'),
    'host': 'visual.volcengineapi.com',
    'region': 'cn-north-1',
    'endpoint': 'https://visual.volcengineapi.com',
    'service': 'cv',
    'req_key': 'jimeng_t2i_v40',
    'run_count': 1,  # 默认运行次数
    'qps': 1,  # 默认并发QPS
    'default_size': 4194304,  # 默认尺寸：2048*2048，最大值4096x4096：16777216
    'sizes': {
        '1K - 1024x1024 (1:1)': 1048576,
        '2K - 2048x2048 (1:1)': 4194304,
        '2K - 2304x1728 (4:3)': 3981312,
        '2K - 2496x1664 (3:2)': 4153344,
        '2K - 2560x1440 (16:9)': 3686400,
        '2K - 3024x1296 (21:9)': 3919104,
        '4K - 4096x4096 (1:1)': 16777216,
        '4K - 4694x3520 (4:3)': 16522240,
        '4K - 4992x3328 (3:2)': 16613376,
        '4K - 5404x3040 (16:9)': 16428160,
        '4K - 6198x2656 (21:9)': 16447488
    }
}

# =============================================================================
# 9. 初始化状态配置（合并所有配置，保持向后兼容）
# =============================================================================
INITIAL_STATE = {
    # EP推理配置
    'api_key': EP_CONFIG['api_key'],
    'model_ep': EP_CONFIG['model_ep'],
    'model_ep_options': MODEL_EP_OPTIONS,
    'temperature': EP_CONFIG['temperature'],
    'top_p': EP_CONFIG['top_p'],
    'max_tokens': EP_CONFIG['max_tokens'],
    'thinking_mode': EP_CONFIG['thinking_mode'],

    # 联网问答Agent配置
    'network_qa_bearer_token': NETWORK_QA_CONFIG['bearer_token'],
    'network_qa_bot_id': NETWORK_QA_CONFIG['bot_id'],
    'network_qa_system_prompt': NETWORK_QA_CONFIG['system_prompt'],
    'thinking': False,  # 默认不思考

    # 图片生成配置
    'picture_generation_api_endpoint': PICTURE_GENERATION_CONFIG['api_endpoint'],
    'picture_generation_api_key': PICTURE_GENERATION_CONFIG['api_key'],
    'picture_generation_models': PICTURE_GENERATION_CONFIG['models'],
    'picture_generation_sizes': PICTURE_GENERATION_CONFIG['sizes'],
    'picture_generation_input_modes': PICTURE_GENERATION_CONFIG['input_modes'],
    'picture_generation_system_prompt': PICTURE_GENERATION_CONFIG['system_prompt'],
    'picture_generation_model': "doubao-seedream-4-5-251128",
    'picture_generation_size': "16:9 (2560x1440)",
    'picture_generation_custom_size': "",
    'picture_generation_sequential': "auto",
    'picture_generation_max_images': 1,
    'picture_generation_watermark': False,
    'picture_generation_response_format': "url",
    'picture_generation_input_mode': "文生图",
    'picture_generation_qps': 2,  # 图片生成并发QPS默认值

    # 视频生成配置
    'video_generation_api_endpoint': VIDEO_GENERATION_CONFIG['api_endpoint'],
    'video_generation_api_key': VIDEO_GENERATION_CONFIG['api_key'],
    'video_generation_models': VIDEO_GENERATION_CONFIG['models'],
    'video_generation_durations': VIDEO_GENERATION_CONFIG['durations'],
    'video_generation_ratios': VIDEO_GENERATION_CONFIG['ratios'],
    'video_generation_example_prompts': VIDEO_GENERATION_CONFIG['example_prompts'],
    'video_generation_model': "doubao-seedance-1-0-pro-250528",
    'video_generation_duration': "5秒",
    'video_generation_ratio': "16:9",
    'video_generation_input_mode': "文生视频",
    'video_generation_image_url': "",

    # 即梦AI配置
    'jimeng_ai_access_key': JIMENG_AI_CONFIG['access_key'],
    'jimeng_ai_secret_key': JIMENG_AI_CONFIG['secret_key'],
    'jimeng_ai_host': JIMENG_AI_CONFIG['host'],
    'jimeng_ai_region': JIMENG_AI_CONFIG['region'],
    'jimeng_ai_endpoint': JIMENG_AI_CONFIG['endpoint'],
    'jimeng_ai_service': JIMENG_AI_CONFIG['service'],
    'jimeng_ai_req_key': JIMENG_AI_CONFIG['req_key'],
    'jimeng_ai_run_count': JIMENG_AI_CONFIG['run_count'],
    'jimeng_ai_qps': JIMENG_AI_CONFIG['qps'],

    # 通用配置
    'qps': 1,
    'show_raw_data': False,
    'run_clicked': False,
    'questions': [],
    'system_prompt': SYSTEM_PROMPT,
    'model_type': "EP推理",
}

