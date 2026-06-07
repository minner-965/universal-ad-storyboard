# 🌌 Universal Ad Storyboard Agent Skill
这是一个全平台、全智能体通用的 AI 视频带货分镜工作流。

只需一张产品图或一段描述，AI 会自动生成 15 宫格大图提示词，并在获取大图后，自动通过本地 Python 脚本将其无损切割为 15 张独立分镜图，供视频生成模型（如 Seedance、可灵、Luma）生成高一致性的视频。

## 🤖 兼容平台
- Google Antigravity / Claude Code / Cursor / Windsurf / GitHub Copilot
- Coze (扣子) / Dify (可直接复制 SKILL.md 作为 System Prompt，切片脚本作为 Code Node)

## 📦 本地快速使用
1. 安装依赖: `pip install pillow`
2. 运行切图: `python tools/split_image.py <你的故事板大图路径或URL>`

分镜文件会自动生成在 `./output/sliced_images/` 目录下。
