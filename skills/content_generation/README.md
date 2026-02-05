# Skill: Content Generation

## Purpose
Create social media posts with text, images, or videos.

## Input Contract
```json
{
  "platform": "twitter | instagram | tiktok",
  "topic": "string",
  "style": "funny | serious | educational",
  "hashtags": ["string"],
  "media_needed": true | false
}
```

## Output Contract
```json
{
  "content": {
    "text": "string",
    "image_url": "string | null",
    "video_url": "string | null",
    "caption": "string"
  },
  "confidence": 0.0-1.0,
  "cost_estimate": "number in USD"
}
```

## MCP Tools Used
- `text_generation.create` (Gemini/Claude)
- `image_generation.create` (Midjourney/Stable Diffusion)
- `video_generation.create` (Runway/Luma)
- `character_consistency.check`
  "response": "string",
