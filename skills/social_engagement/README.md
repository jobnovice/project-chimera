# Skill: Social Engagement

## Purpose
Respond to comments, analyze engagement, and interact with audience.

## Input Contract
```json
{
  "platform": "twitter | instagram | tiktok",
  "interaction_type": "comment | message | mention",
  "user_message": "string",
  "context": "previous_conversation_history"
}
```

## Output Contract
```json
{
  "action": "reply | like | share | ignore",
  "sentiment_analysis": "positive | negative | neutral",
  "escalate_to_human": true | false
}
```

## MCP Tools Used
- `twitter.reply_to_tweet`
- `instagram.comment_on_post`
- `sentiment.analyze`
- `safety.check_content`
- `engagement.predict`
