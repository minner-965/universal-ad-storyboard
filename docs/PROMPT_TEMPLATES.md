# 🎬 高阶玩法与核心提示词库 (Advanced Playbook & Prompts)

本指南基于头部创作者（如【胖胖喵AI】与【阿拉赛博蕾】）的顶级工作流经验提取并优化，专注于 **GPT Image 2 + Seedance 2.0 (或可灵等其他I2V模型)** 的强强联合玩法。

## 💡 一、 核心工作流底层原理

这套工作流的底层逻辑是：**“生图模型锁死一致性，视频模型展开时间轴”**。它彻底解决了 AI 视频创作中“人物/产品忽隐忽现、画风突变”的痛点。

1. **生图端锁死一致性 (GPT Image 2)**：利用其强大的跨图一致性与多宫格排版能力，在同一个画布上直接画出 12 或 15 宫格故事板。这样主角（如汽车、人物）在光影、颜色、结构上就能达到 100% 的物理级一致性。
2. **视频端时间轴延展 (Seedance 2.0 等)**：将无损切片后的独立分镜喂给视频大模型，利用强大的单图转视频（I2V）能力赋予画面动态。
3. **黄金动作法则——“一个镜头只做一件事”**：在 AI 视频生成中，**切忌**同时安排复杂的复合动作（例如：车子漂移的同时车门打开、镜头还要剧烈旋转）。正确的做法是让每个分镜只专注于 **“1 个微动态（如车轮转 / 尾灯亮 / 眨眼） + 1 个推拉摇移运镜”**，让模型在 3 秒内精确渲染，这样出片成功率最高，画面最不容易崩。

---

## 🏎️ 二、 汽车 TVC 专属故事板模板 (参考: 胖胖喵AI)

**适用阶段**：生图大图阶段 (GPT Image 2 / DALL-E 3)
**用途**：生成极具电影感、高一致性的 12 宫格汽车广告大片分镜。你只需将 `[ ]` 内的内容替换为你的车型和风格设定。

```text
A 12-panel cinematic automotive storyboard arranged in a 4x3 grid (4 rows by 3 columns), landscape 16:9 ratio overall.

**Global Style:** High-end premium car TVC, cinematic professional automotive photography, dramatic high-contrast moody lighting, atmospheric smoke, neon reflections. Thin [边框颜色，如：gold / gray] borders separate each rectangular panel. Strictly DO NOT show any panel numbers, text overlays, titles, or UI elements on the image.

**Product Consistency:**
Every panel featuring the vehicle must show the exact same [车型描述，例如：cyberpunk electric sports car in matte cherry red, with glowing cyan LED headlights and carbon fiber details]. The environment must maintain a gritty urban night atmosphere with wet streets.

**Panel-by-Panel Sequence:**
Panel 1: Close-up of the glowing cyan LED headlight turning on in a dark, moody garage.
Panel 2: Extreme close-up of the glossy carbon fiber texture on the hood, catching rain drops.
Panel 3: Close-up of the tire accelerating, spinning smoothly and leaving a trace of white smoke on the wet tarmac.
Panel 4: Intimate interior shot. The driver's hand in leather gloves gripping the steering wheel, ambient neon light inside the cabin.
Panel 5: Low-angle wide shot of the car speeding down a wet neon-lit city street at night, neon lights reflecting on the car body.
Panel 6: Dynamic panning shot. The car drifting around a sharp street corner, kicking up water spray and smoke.
Panel 7: Close-up of the futuristic exhaust pipe emitting glowing vapor.
Panel 8: High-angle bird's eye view. The car racing through an empty concrete bridge under the moonlight.
Panel 9: Flat lay product showcase: the sleek key fob of the car resting on a dark carbon fiber surface next to a high-end watch.
Panel 10: Close-up of the car's wheel hub and glowing brake calipers spinning to a stop.
Panel 11: The car seen from behind, driving away into a dark, foggy concrete tunnel with strong white light at the exit.
Panel 12: A wide heroic shot of the car parked under a single street lamp in the rain, looking majestic, powerful, and ready to launch.
```

---

## 🎬 三、 影视提案级排版与动作流控制 (参考: 阿拉赛博蕾)

此玩法的核心在于 **“专业级影视前期排版感”** 结合 **“微表情/精确动作控制”**。

### 1. 提案级排版设定 (生图阶段)
用于生成极具专业影视感的故事板（例如电影预告、漫剧设定等）：

```text
请根据我提供的剧本文案，生成一张 16:9 横版故事版设定图，不需要任何参考图。

整体要求：浅色高级信息图风格，浅蓝+白色版式，冰蓝边框，半透明卡片，排版干净统一，像专业影视前期故事板。

故事内容风格（真人现代都市）：
Panel 1: 男主站在细雨中的电话亭旁，神色落寞，冷色调。
Panel 2: 男主特写，眼神流露出悲伤，眼角有泪水。
Panel 3: 女主站在马路对面，手里撑着伞，暖黄色街灯打在身上。
Panel 4: 双人特写，雨水在半空中被霓虹灯折射，画面情绪张力拉满。
```

### 2. 精确动作/镜头控制指令 (I2V 视频渲染阶段)
通过本仓库的切片脚本拿到独立分镜后，将单张图喂给 Seedance 2.0 等视频生成模型，并配合以下 **“微动态 + 经典运镜”** 的提示词（Prompt），实现神级精准控制：

#### 🚗 汽车类微动态控制
- **启动预备 (Turn on & Rumble):**
  > `Cinematic close-up. The headlights suddenly turn on and glow. The engine rumbles, causing subtle realistic vibrations on the car body. Volumetric exhaust steam rises from the back. Slow zoom-in.`
- **极速疾驰 (Speeding & Blur):**
  > `High-speed action shot. The car speeds forward along the wet road. Wheels are spinning rapidly with realistic motion blur. Rain drops fly across the windshield. Dynamic camera pan.`
- **漂移过弯 (Drift & Splash):**
  > `Cinematic action. The car drifts smoothly around a wet city corner. Tires kick up realistic water spray and thick white smoke. The camera tilts slightly to follow the motion.`

#### 👤 人物类微表情控制
- **高冷蔑视 (Arrogant Glance):**
  > `Subtle character action. The character slowly blinks and narrows their eyes with a cold, arrogant expression. The camera slowly dollies in towards the eyes. Natural hair movement.`
- **惊恐回头 (Startled Turn):**
  > `Realistic motion. The character suddenly but smoothly turns their head slightly to the left, eyes widening in shock. Volumetric shadow shifts on the face. Slow-motion, 4k.`
