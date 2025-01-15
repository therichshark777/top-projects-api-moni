SELECT 
    links.mentioned_twitter_user_id,
    COUNT(*) AS cnt,
	accounts.username,
    accounts.name,
    accounts.profile_image_url
FROM 
    public.observed_mention_new links
JOIN 
    public.observed accounts
ON 
    links.mentioned_twitter_user_id = accounts.twitter_user_id
WHERE 
    links.mention_created_at >= NOW() - INTERVAL '1 day'
GROUP BY 
    links.mentioned_twitter_user_id,
	accounts.username,
    accounts.name,
    accounts.profile_image_url
ORDER BY 
    cnt DESC
LIMIT 50;