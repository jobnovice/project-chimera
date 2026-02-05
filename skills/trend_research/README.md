# Skill: Trend Research

## Purpose
Find viral topics and trending content for the influencer to create posts about.

## Input Contract
```json
{
  "platforms": ["twitter", "tiktok", "instagram"],
  "topics": ["fashion", "tech", "lifestyle"],
  "time_range": "last_24_hours",
  "max_results": 10
}
```

## Output Contract
```json
{
  "trends": [
    {
      "topic": "Summer Fashion 2026",
      "volume": 15000,
      "growth": 0.45,
      "platforms": ["tiktok", "instagram"],
      "key_influencers": ["@fashionista", "@styleguide"],
      "recommended_angle": "How to style summer outfits"
    }
  ],
  "confidence_score": 0.85
}
```

## MCP Tools Used
- `twitter.get_trends`
- `tiktok.trending_topics`
- `news.aggregate`
- `sentiment.analyze`

## Notes
- Runs every 4 hours automatically
- Flags sudden spikes in topic volume
- Combines data from multiple platforms
- Stores trends in memory for future reference
