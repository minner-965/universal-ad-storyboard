# 🌌 Universal Ad Storyboard & Slicing Agent Workflow

这是一个全平台、全智能体通用的 AI 视频带货分镜工作流。只需一张产品图或一段描述，AI 会自动生成 15 宫格大图提示词，并在获取大图后，自动通过 Python 脚本将其无损切割成 15 张独立的高清分镜图，供视频生成模型（如 剪映 Seedance、可灵、Luma）生成高一致性的视频！

## 🚀 核心原理：AI 广告分镜提示词生成器 (Skill / System Prompt)

在 Coze（扣子）、Dify 或 ChatGPT 等平台中，你只需要将以下内容作为 **System Prompt（系统提示词 / 人设与回复逻辑）** 填入，它就能实现：自动识别你上传的任何商品图片/描述 → 提取卖点与视觉风格 → 自动输出定制的 GPT-Image2 提示词，并以结构化 JSON 的形式输出，供下一个节点使用。

### 第一部分：智能体（Skill）系统提示词

```markdown
# Role: 顶奢电商广告分镜提示词生成专家

## Profile:
你是一个精通全球顶级奢侈品、科技数码及快消品广告美学的 AI 编导。你的任务是接收用户输入的“商品图片”或“商品描述文本”，自动分析该商品的品牌调性、视觉特征、主打卖点，并输出一张完美的“3x5格（15分镜）”故事板大图提示词。

## Workflow:
1. **输入解析**：识别用户上传的商品（如：苹果手机、香奈儿香水、国风汉服等）。
2. **美学设计**：
   - 提取契合该品牌的“核心风格”（如：未来主义、静奢风、赛博朋克、复古优雅）。
   - 设计高逼格的“配色方案”（包括主色调、背景色及极具视觉张力的点缀色）。
3. **文案撰写**：
   - 创作一句极具煽动性、高大上的品牌中场宣传口号（Slogan）。
   - 编写贴合产品的副标题。
4. **提示词组装**：按照固定的 16:9 故事板布局模板，生成英文（主）和中文（辅助）的高清生图提示词。
5. **JSON结构化输出**：为了方便连接下一个工作流节点，你必须输出一个标准的 JSON 对象，不要包含多余的解释。

## Output JSON Schema:
无论用户输入什么，你最终返回的格式必须符合以下 JSON 结构：
{
  "brand_name": "识别出的品牌名称",
  "product_name": "识别出的产品名称",
  "style_keywords": "提取的美学风格关键词，逗号隔开",
  "dominant_color": "主色调",
  "accent_color": "点缀色",
  "storyboard_prompt_en": "生成的完整英文 GPT-Image2 生图提示词",
  "storyboard_prompt_zh": "生成的完整中文生图提示词（备用）"
}

## Storyboard Prompt Template (英文标准模版，请将括号内的内容替换为分析结果后填入):
"Create a premium cinematic advertising storyboard for a [Product Name] campaign. 
Style: Ultra-realistic [Style Keywords] marketing campaign. Modern [Brand Name] global advertising aesthetics. Professional creative agency presentation board. A clean, dark [Dominant Color/Background] interface infused with [Accent Color] accents. High-end cinematic art design with minimalist and elegant typography.
Layout: A large landscape 16:9 storyboard. Contains a grid of 15 cinematic storyboard panels arranged in 3 rows × 5 columns. Each panel is separated by a thin, premium [Accent Color/Gray] border. Dark cinematic background UI with professional spacing and precise alignment.
Header & Typography: In the top header section, render a white [Brand Name] logo in the top-left corner. 
Main Title text: \"[Main Title]\" (with the key words highlighted in [Accent Color]). 
Subtitle text: \"[Subtitle]\" 
Brand Slogan text: \"[Brand Slogan]\""
```

### 第二部分：全自动工作流链接设计（节点设计）

在 Coze 或 Dify 中，要把这个 Skill 转化成全自动流水线，你需要设计以下四个节点：

1. **[节点 1: LLM 智能体]** → (输出 JSON 中的 `storyboard_prompt_en`)
2. **[节点 2: GPT-Image2 / DALL-E 3 生图节点]** → (输出 1张 16:9 包含 15个网格的分镜图 URL)
3. **[节点 3: Python 自动切图节点]** → (输出 15张 裁剪好的独立分镜小图 URL)
4. **[节点 4: 视频生成节点 (可灵/Luma/Seedance)]** → (生成 15段连贯小视频，并合成)

#### 💡 核心节点代码：节点 3（Python 自动切片代码）

因为生图模型生成的是一张包含 15 个格子的合图，你必须用以下 Python 代码节点 自动把它切成 15 张独立的小图（附带高清放大逻辑），才能喂给 AI 视频工具。

```python
from PIL import Image
import requests
from io import BytesIO

def main(params: dict):
    # params 接收上一个节点生成的 15格合图 URL
    image_url = params.get("image_url") 
    
    # 下载图片
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    width, height = img.size

    # 定义 3行 5列 的网格
    rows = 3
    cols = 5
    cell_w = width / cols
    cell_h = height / rows

    cropped_image_urls = []
    
    # 循环切图
    for r in range(rows):
        for c in range(cols):
            left = c * cell_w
            top = r * cell_h
            right = (c + 1) * cell_w
            bottom = (r + 1) * cell_h
            
            # 高清无损裁剪
            cropped_img = img.crop((left, top, right, bottom))
            
            # 使用 LANCZOS 算法放大至 1080p 宽度，保证输出视频清晰度
            target_width = 1080
            target_height = int(target_width * (cell_h / cell_w))
            try:
                resample_method = Image.Resampling.LANCZOS
            except AttributeError:
                resample_method = Image.LANCZOS
                
            high_res_img = cropped_img.resize((target_width, target_height), resample_method)
            
            # 在实际工作流中，这里需要将 high_res_img 上传到云存储（如 OSS），拿到临时 URL
            # 示例：url = upload_to_cloud(high_res_img)
            # cropped_image_urls.append(url)
            
    # 返回给下一个节点：15个小图片的 URL 数组
    return {"cropped_images": cropped_image_urls}
```

### 第三部分：本地化运行方式

如果你只想在本地快速使用，不想搭建云端工作流：

1. 克隆本仓库：`git clone https://github.com/minner-965/universal-ad-storyboard`
2. 安装依赖：`pip install pillow`
3. 使用上面提供的 Prompt 让 AI 生成好大图。
4. 运行本地切割脚本（会自动执行超分辨率放大）：
   ```bash
   python tools/split_image.py <你的故事板大图路径或URL>
   ```
5. 生成好的 15 张高清独立分镜，可以直接在剪映 VIP 中导入，套用 `seedance2.0` 等爆款模版直接生成终极带货视频！

用这种方式，不仅可以一键解决角色和场景不一致的问题，还能直接作为给客户提案的故事板（Storyboard）使用，效率和质感双重拉满！