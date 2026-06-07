# Universal Ad Storyboard Workflow (AI 广告分镜与带货视频自动化工作流)

This project provides a complete, 5-step automated workflow to turn any product image into a high-conversion, cinematic AI commercial video.

## 核心工作流大纲 (The 5-Step Commercial Workflow)

### Step 1: 准备商品参考图 (Product Reference)
上传你的商品原图（如：衣服、包包、球鞋）。这是保证后续 AI 生成不出现“虚假宣传”的核心基准图（Reference Image）。

### Step 2: 故事板生图 (Generate Storyboard)
使用以下 **12宫格“万能生图”模板**。将括号 `[ ]` 内的内容替换为你的商品信息，并配合 **Midjourney (`--cref`)** 或 **Stable Diffusion (IP-Adapter)** 锁定商品原图进行生成。

> ⚠️ **【电商避坑核心警告：拒绝虚假宣传！】**
> 在生图时，绝对不能只输入文字！必须将 Step 1 的原商品图作为**垫图（Image Prompt / IP-Adapter）**输入，100% 锁死服装款式与印花！

**【12宫格万能生图模板】**
```text
A 12-panel cinematic advertising storyboard arranged in a 4x3 grid (4 rows by 3 columns), landscape 16:9 ratio overall. 

**Global Style:** High-end [视觉风格，如：gritty streetwear / luxury minimalist / techwear cyber] commercial campaign, cinematic photography, dramatic [光影，如：high-contrast moody / soft natural] lighting, [环境元素，如：volumetric smoke / natural sunlight] and dark atmospheric tones. Elegant thin [边框颜色，如：gold / gray] borders separate each rectangular panel. Strictly DO NOT show any panel numbers, text overlays, titles, or UI elements on the image.

**Character & Product Consistency:**
Every panel featuring the clothing must show the exact same "[品牌名]" [产品类别，如：heavyweight cotton t-shirt].
- Front design: [正面设计描述，如：minimalist small logo on the chest].
- Back/Main design: [主视觉/背面设计描述，如：a massive printed graphic of...].
The main character is a [模特特征描述，如：tough-looking athletic male model with a buzz cut].

**Panel-by-Panel Sequence:**
Panel 1: [分镜1：氛围引入，如：Front view of the model standing in a moody studio]
Panel 2: [分镜2：展示主卖点，如：Back view showing the detailed graphic]
Panel 3: [分镜3：核心材质特写，如：Macro close-up shot of the texture]
Panel 4: [分镜4：人像特写，如：Close-up of the model's intense gaze]
Panel 5: [分镜5：上身外景，如：The model walking down a wet, neon-lit alley]
Panel 6: [分镜6：侧面/版型展示，如：Low-angle shot showing the relaxed fit]
Panel 7: [分镜7：情绪场景，如：The model sitting on stairs looking thoughtful]
Panel 8: [分镜8：大远景/剪影，如：Wide shot silhouette walking into a tunnel]
Panel 9: [分镜9：商用静物平铺，如：High-end flat lay product showcase]
Panel 10: [分镜10：局部特写，如：Close-up of the chest embroidered logo]
Panel 11: [分镜11：副模穿搭，如：A female model wearing the same product]
Panel 12: [分镜12：群像收尾，如：A group of models walking down the street]
```

### Step 3: 自动化极速切片 (Split Image)
使用提供的 Python 脚本，将生成的 12 宫格大图自动进行 4% 去边、LANCZOS 1080p 超分锐化，完美切分为 12 张独立的高清分镜图。
```bash
python tools/split_image.py <你的故事板图片路径>
```

### Step 4: 生成独立动效提示词 (Generate I2V Prompts)
让大模型为切好的每一张分镜图生成独立的 **I2V 英文提示词**（必须包含：主体动作 Subject Action、镜头运动 Camera Motion、光影环境 Lighting）。

### Step 5: 最终视频合成 (Seedance / Kling / Runway)
最后，也是最激动人心的一步。将以下三样素材一同喂给 AI 视频大模型（如 Seedance）：
1. **参考图** (Step 1 的原商品图，保证细节不走样)
2. **分镜图** (Step 3 切出来的单张动作预演图)
3. **提示词** (Step 4 生成的专属动效镜头指令)

一键组合，你就能得到具有超强一致性、运镜丰富且质感爆炸的高级带货短视频！

## 📚 高阶玩法与工作流总结 (Advanced Guide & Workflows)
想要探索更专业的工作流、查看完整操作步骤，请参考：
👉 [🚀 从图到片：全链路 AI 视频自动化工作流闭环总结 (END_TO_END_WORKFLOW.md)](docs/END_TO_END_WORKFLOW.md)
👉 [高级提示词与核心原理指南 (PROMPT_TEMPLATES.md)](docs/PROMPT_TEMPLATES.md)
