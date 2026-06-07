---
name: Ad Storyboard & Slicing Agent
description: Generates a 9-panel cinematic storyboard for products and automatically slices them into 9 high-res individual images for video generation.
---

# Ad Storyboard & Slicing Agent Workflow

## 1. Description
This skill takes a user's product image or description, generates a 9-grid storyboard prompt, generates the storyboard image, and uses `tools/split_image.py` to upscale and slice it into 9 high-quality individual frames.

## 2. 远端万能公式模版

你可以直接使用下面的“万能模版”。只需修改括号内的部分，就能瞬间帮你自己的产品（如：手机、包包、香水、国风潮牌等）直出 9 宫格高清无字故事板：

```text
Create a premium cinematic advertising storyboard for a [Product Name] campaign. 
Style: Ultra-realistic [Style Keywords] marketing campaign. Modern [Brand Name] global advertising aesthetics. Strictly DO NOT show any UI, logos, branding text, presentation titles, headers, or text labels on the image. Focus 100% of the canvas on the storyboard frames. 
Layout: A large landscape 16:9 storyboard. Contains a seamless grid of 9 cinematic storyboard panels arranged in a 3 rows × 3 columns grid. Panels are separated only by ultra-thin dark gray borders. High-end cinematic art design, with masterfully rendered composition in every single panel.
```

## 3. Workflow Steps
> ⚠️ **CRITICAL E-COMMERCE RULE (Product Consistency)**
> Text-to-image models (like DALL-E 3) will hallucinate product details, leading to false advertising. 
> To guarantee the generated t-shirt/product matches the original uploaded image exactly, the Image Generation node MUST use the uploaded image as a reference:
> - **Midjourney**: Use `--cref <image_url> --cw 100` to lock the character/product.
> - **Stable Diffusion**: Use **IP-Adapter** to extract and apply the exact product graphic.
1. Determine the brand, product name, and aesthetic style.
2. Run an Image Generation tool (MUST support Image Reference / IP-Adapter / Midjourney --cref) using the prompt above AND the user's original product image to lock product consistency.
3. Run `python tools/split_image.py <image_path>` which will automatically:
   - Perform a 4% inner crop to remove borders.
   - Upscale each frame to 1024x576 using LANCZOS.
   - Apply a Sharpen filter for maximum clarity.
4. Deliver the 9 sliced images to the user.
## 4. Video Script & I2V Generation (Optional but Recommended)
After generating and slicing the 9 or 16 frames, you can use the following universal prompt to generate a cohesive video storyboard and Image-to-Video (I2V) prompts for tools like Runway Gen-3, Luma, or Kling.

```text
I have generated high-res storyboard frames for [Product Name]. 
To turn these static frames into a high-conversion commercial video, provide a two-step packaging:
1. 15-Second Commercial Video Storyboard (Table): Create a table with columns: Scene #, Duration (s), Visual Action, Camera Motion, Voiceover, Audio & BGM.
2. I2V Prompts: For each core scene, write a highly detailed English I2V prompt optimized for video generation AI. Must include subject action, camera movement (e.g., Macro close-up), and lighting/atmosphere.
```