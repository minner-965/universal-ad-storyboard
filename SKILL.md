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
1. Determine the brand, product name, and aesthetic style.
2. Run the `generate_image` tool using the prompt above.
3. Run `python tools/split_image.py <image_path>` which will automatically:
   - Perform a 4% inner crop to remove borders.
   - Upscale each frame to 1024x576 using LANCZOS.
   - Apply a Sharpen filter for maximum clarity.
4. Deliver the 9 sliced images to the user.