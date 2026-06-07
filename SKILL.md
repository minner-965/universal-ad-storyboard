---
name: universal-ad-storyboard
description: An end-to-end AI commercial video agent skill that converts product references into a 12-panel cinematic storyboard, automatically slices and upscales them using Python, generates Image-to-Video (I2V) prompts, and prepares them for tools like Seedance/Runway.
---

# 🎥 AI Universal Ad Storyboard & Video Generator (Skill)

This skill enables users or AI agents to perfectly transform a single product reference image into a highly consistent, 12-panel Hollywood-style commercial video storyboard, and then slices them into high-res ready-to-animate assets.

## 🌟 The 5-Step Commercial Workflow

### Step 1: Product Reference (商品参考图)
The user must provide/upload their product image (e.g. clothing, bag, tech gadget). This is the `Reference Image` used to lock the product design and prevent AI hallucinations.

### Step 2: Generate Storyboard (故事板生图)
Use an Image Generation tool (MUST support Image Reference / IP-Adapter / Midjourney `--cref`) using the **12-Panel Universal Prompt** below AND the user's original product image to lock product consistency.

> ⚠️ **CRITICAL E-COMMERCE RULE (Product Consistency)**
> Text-to-image models (like DALL-E 3) will hallucinate product details, leading to false advertising. 
> To guarantee the generated product matches the original uploaded image exactly, the Image Generation node MUST use the uploaded image as a reference:
> - **Midjourney**: Use `--cref <image_url> --cw 100` to lock the character/product.
> - **Stable Diffusion**: Use **IP-Adapter** to extract and apply the exact product graphic.

**[12-Panel Universal Prompt Template]**
```text
A 12-panel cinematic advertising storyboard arranged in a 4x3 grid (4 rows by 3 columns), landscape 16:9 ratio overall. 

**Global Style:** High-end [Style, e.g., gritty streetwear / luxury minimalist] commercial campaign, cinematic photography, dramatic [Lighting, e.g., high-contrast moody] lighting, [Atmosphere, e.g., volumetric smoke] and dark atmospheric tones. Elegant thin [Border Color, e.g., gold] borders separate each rectangular panel. Strictly DO NOT show any panel numbers, text overlays, titles, or UI elements on the image.

**Character & Product Consistency:**
Every panel featuring the clothing must show the exact same "[Brand Name]" [Product Type, e.g., heavyweight cotton t-shirt].
- Front design: [Front Description].
- Back/Main design: [Back Description].
The main character is a [Model Description].

**Panel-by-Panel Sequence:**
Panel 1: [Scene 1]
Panel 2: [Scene 2]
Panel 3: [Scene 3]
Panel 4: [Scene 4]
Panel 5: [Scene 5]
Panel 6: [Scene 6]
Panel 7: [Scene 7]
Panel 8: [Scene 8]
Panel 9: [Scene 9]
Panel 10: [Scene 10]
Panel 11: [Scene 11]
Panel 12: [Scene 12]
```

### Step 3: Auto-Slice & Upscale (自动化切片)
Pass the generated 12-grid image to the provided Python script. It automatically crops out 4% of borders and uses LANCZOS algorithms to upscale to 1080p.
```bash
python tools/split_image.py <image_path>
```

### Step 4: Generate I2V Prompts (生成动效指令)
Ask the LLM to generate independent Image-to-Video (I2V) English prompts for each of the 12 sliced frames. The prompt must include:
- Subject Action
- Camera Motion (e.g., Macro close-up, Slow pull-back)
- Lighting & Atmosphere

### Step 5: Final Video Assembly (Seedance / Luma)
Provide the following 3 elements to your AI Video Generator (like Seedance, Kling, or Runway):
1. **The Reference Image** (From Step 1)
2. **The Sliced Frame** (From Step 3)
3. **The I2V Action Prompt** (From Step 4)

Boom! You have a highly-consistent, commercial-grade short video!