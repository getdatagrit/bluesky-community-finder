# Bluesky Community Finder: Starter Packs & Feeds

Find Bluesky starter packs, custom feeds and curated lists by topic, with join counts, feed likes and full member lists with follower counts.

[![Run on Apify](https://img.shields.io/badge/Run%20on-Apify-0f9f74)](https://apify.com/datagrit/bluesky-community-finder) [![Docs](https://img.shields.io/badge/docs-getdatagrit.github.io-0e1726)](https://getdatagrit.github.io/bluesky-community-finder/)

**from $3.50 per 1,000 results + $10 per run (pay per result; the rate depends on your Apify plan).** Export as JSON, CSV or Excel, call it through the API, or schedule it on Apify.

## What it does

Bluesky Community Finder builds a catalog of the communities on Bluesky: starter packs, custom feeds and curated lists. Search by topic or point it at specific accounts, and every starter pack, feed or list comes back as one clean row with its creator, dates, size and popularity. Starter packs carry all-time and weekly join counts and the member count. Feeds carry likes and, if you ask for it, a live check of whether the feed is still online and valid. Lists carry their purpose (curate, moderation or reference) and member count. Turn on members and every pack or list is followed by one row per account, with followers, follows, posts and verification status. It reads Bluesky's public API, needs no login or API key, and exports to JSON, CSV or Excel.

## Quick start

1. Open [Bluesky Community Finder: Starter Packs & Feeds on Apify Store](https://apify.com/datagrit/bluesky-community-finder) and click **Try for free**.
2. Fill in the input form (or paste the JSON below) and run it.
3. Download the dataset, or fetch it from the API.

```json
{
  "mode": "starterPacks",
  "queries": [
    "journalists",
    "science"
  ],
  "maxItems": 30
}
```

## Input

| Field | Type | What it does |
|---|---|---|
| `mode` | string | Starter packs: curated follow-packs you can search by topic. Feeds: custom feed generators you can search by topic. Lists: curated, moderation or reference lists published by the accounts in Handles. |
| `queries` | array | Topics to search, for example journalists, science or birds. Each term is searched separately. Works for starter packs and feeds. Lists cannot be searched by topic: use Handles. Leave Search terms and Handles empty to get a free example of up to 10 results. |
| `handles` | array | Bluesky handles, for example bsky.app, or profile URLs such as https://bsky.app/profile/bsky.app. Returns the starter packs, feeds or lists that these accounts created, depending on the mode. |
| `maxItems` | integer | Stop after this many starter packs, feeds or lists in total across all search terms and handles. Member rows are not counted here; they come on top when Include members is on. |
| `textContains` | array | Keep only results whose name or description contains at least one of these words (case-insensitive). |
| `minJoinedAllTime` | integer | Starter packs only: keep packs that at least this many people joined through, all time. Ignored for feeds and lists. |
| `minMembers` | integer | Starter packs and lists only: keep communities with at least this many accounts. Ignored for feeds. |
| `minLikes` | integer | Feeds only: keep feeds with at least this many likes. Ignored for starter packs and lists. |
| `publishedAfter` | string | Keep communities created or first indexed on or after this date, for example 2025-06-01. Starter packs use their creation date; feeds and lists use the date Bluesky indexed them. |
| `listPurpose` | string | Lists only: curate lists group accounts worth following, mod lists are moderation lists, reference lists are general collections. Ignored for starter packs and feeds. |
| `checkFeedHealth` | boolean | Feeds only: ask Bluesky whether each feed is online and valid, one extra request per feed. Without it, isOnline and isValid stay null. |
| `onlyOnlineFeeds` | boolean | Feeds only: drop feeds that are offline or invalid. Turns on the health check automatically. |
| `includeMembers` | boolean | Starter packs and lists only: add one row per member account after each community. Each member row is a separate billed result. |
| `maxMembersPerCommunity` | integer | Cap on member rows per starter pack or list when Include members is on. |
| `includeMemberStats` | boolean | When Include members is on, look up followers, follows, posts and verification for every member (one request per 25 members). |
| `onlyNewSinceLastRun` | boolean | Skip starter packs, feeds and lists already returned by an earlier run with the same search terms, handles and filters. Only delivered results are remembered. |
| `proxyConfiguration` | object | Optional proxy. Bluesky's public API needs none; leave disabled unless you have a reason. |

## Output

| Field | Type | Description |
|---|---|---|
| `type` | string | What the row is: starterPack, feed, list or member. On the status row it is the type you searched for. |
| `query` | string | The search term or handle this row came from. Member rows carry the query of their starter pack or list. |
| `uri` | string | Permanent AT Protocol address of the starter pack, feed or list. Null on member rows and the status row. |
| `url` | string | Link to the starter pack, feed, list or member profile on bsky.app. Null on the status row. |
| `name` | string | Name of the starter pack, feed or list. Null on member rows and the status row. |
| `description` | string | Description written by the creator, or for a member the profile bio. Null when empty. |
| `creatorHandle` | string | Handle of the account that created the community. Null on member rows and the status row. |
| `creatorDisplayName` | string | Display name of the creator. Null when the creator has none. |
| `creatorDid` | string | Permanent identifier of the creator account. Null on member rows and the status row. |
| `createdAt` | string | Starter packs only: when the creator made the pack (ISO 8601). Null for feeds, lists and members. |
| `updatedAt` | string | Starter packs only: last edit by the creator (ISO 8601). Null when never edited. |
| `indexedAt` | string | When Bluesky indexed the community (ISO 8601). Null for members. |
| `joinedAllTimeCount` | integer | Starter packs only: how many people joined through the pack, all time. Null for feeds and lists. |
| `joinedWeekCount` | integer | Starter packs only: joins in the last 7 days. Null for feeds and lists. |
| `memberCount` | integer | Starter packs and lists: number of accounts in it. Null for feeds and members. |
| `feedCount` | integer | Starter packs only: how many custom feeds the pack recommends. Null for feeds, lists and members. |
| `feedUris` | array | Starter packs only: AT URIs of the feeds the pack recommends. Null for feeds, lists and members. |
| `likeCount` | integer | Feeds only: number of likes. Null for starter packs and lists. |
| `acceptsInteractions` | boolean | Feeds only: whether the feed takes like and reply signals from users. Null for starter packs and lists. |
| `contentMode` | string | Feeds only: unspecified (posts) or video. Null when Bluesky does not say. |
| `serviceDid` | string | Feeds only: identifier of the server that generates the feed. Null for other types. |
| `isOnline` | boolean | Feeds only, when Check feed health is on: whether the feed server answers. Null when health was not checked. |
| `isValid` | boolean | Feeds only, when Check feed health is on: whether the feed returns valid posts. Null when health was not checked. |
| `purpose` | string | Lists only: curate, mod or reference. Null for other types. |
| `communityType` | string | Members only: starterPack or list the member belongs to. Null on community rows. |
| `communityUri` | string | Members only: AT URI of the starter pack or list. Null on community rows. |
| `communityName` | string | Members only: name of the starter pack or list. Null on community rows. |
| `did` | string | Members only: permanent identifier of the account. Null on community rows. |
| `handle` | string | Members only: handle of the account. Null on community rows. |
| `displayName` | string | Members only: display name. Null when the account has none. |
| `accountCreatedAt` | string | Members only: when the account was created (ISO 8601). Null when unknown. |
| `followersCount` | integer | Members only: follower count. Null when Add follower counts is off or the account was deactivated. |
| `followsCount` | integer | Members only: how many accounts the member follows. Null when stats are off or unavailable. |
| `postsCount` | integer | Members only: number of posts. Null when stats are off or unavailable. |
| `isVerified` | boolean | Members only: whether Bluesky verified the account. Null when stats are off or unavailable. |
| `avatar` | string | Members only: profile picture URL. Null when the account has none. |
| `scrapedAt` | string | ISO 8601 timestamp of extraction. |
| `found` | boolean | False only on the single status row emitted when a search term or handle returns nothing. |

Sample record:

```json
{
  "type": "starterPack",
  "query": "journalists",
  "uri": "at://did:plc:ab12cd34ef56/app.bsky.graph.starterpack/3kabcdefgh2",
  "url": "https://bsky.app/starter-pack/example.bsky.social/3kabcdefgh2",
  "name": "Bluesky for Journalists",
  "description": "Journalists worth following on Bluesky.",
  "creatorHandle": "example.bsky.social",
  "creatorDisplayName": "Example Creator",
  "creatorDid": "did:plc:ab12cd34ef56",
  "createdAt": "2024-06-25T05:30:27.442Z",
  "updatedAt": "2024-07-01T10:00:00.000Z",
  "indexedAt": "2024-06-25T05:30:28.000Z",
  "joinedAllTimeCount": 37,
  "joinedWeekCount": 2,
  "memberCount": 150,
  "feedCount": 3,
  "feedUris": [
    "at://did:plc:ab12cd34ef56/app.bsky.feed.generator/news"
  ],
  "likeCount": 23983,
  "acceptsInteractions": true,
  "contentMode": "unspecified",
  "serviceDid": "did:web:feed.example.com",
  "isOnline": true,
  "isValid": true,
  "purpose": "curate",
  "communityType": "starterPack",
  "communityUri": "at://did:plc:ab12cd34ef56/app.bsky.graph.starterpack/3kabcdefgh2",
  "communityName": "Bluesky for Journalists",
  "did": "did:plc:zz99yy88xx77",
  "handle": "reporter.bsky.social",
  "displayName": "Example Reporter",
  "accountCreatedAt": "2023-05-01T12:00:00.000Z",
  "followersCount": 1200,
  "followsCount": 340,
  "postsCount": 5600,
  "isVerified": false,
  "avatar": "https://cdn.bsky.app/img/avatar/plain/did:plc:zz99yy88xx77/abc@jpeg",
  "scrapedAt": "2026-10-01T08:00:00.000Z",
  "found": true
}
```

## Call it from code

Runnable examples are in [`examples/`](examples). Replace `YOUR_APIFY_TOKEN` with the token from your Apify account settings.

```bash
curl -X POST "https://api.apify.com/v2/acts/datagrit~bluesky-community-finder/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"mode":"starterPacks","queries":["journalists","science"],"maxItems":30}'
```

## FAQ

**Does it need a Bluesky account?**  
No. It uses the public API without login.

**Can I search lists by topic?**  
Bluesky has no search for lists. Give the handles of the accounts whose lists you want.

**How do I get only new packs each day?**  
Schedule the Actor with the same input and switch on "Only communities not seen before".

**Something looks wrong in the data.**  
Open an issue on the Actor page with the input you used and the run link.

## More from datagrit

- [Bilibili Anime Catalog, Rankings & Calendar](https://github.com/getdatagrit/bilibili-anime-series-tracker) - Bilibili anime, Chinese animation, film, documentary and TV series: filterable catalog, Top 100 rankings, release calendar and season details with ratings and follower counts.
- [Medium Publication Finder: Subscribers & Activity](https://github.com/getdatagrit/medium-publication-finder) - Find Medium publications by keyword and score each one: subscribers, posting cadence, claps per post, paywalled share and top authors.
- [Substack Newsletter Sponsorship Prospect Finder](https://github.com/getdatagrit/substack-sponsor-prospector) - Substack publications ranked for sponsorship: subscriber count, paid-tier size, plan prices, posting cadence and engagement per 1,000 subscribers.
- [Telegram Channel Analytics: Growth and Reach](https://github.com/getdatagrit/telegram-channel-growth-analytics) - One row per public Telegram channel: subscribers and growth since your last run, median views, view rate, posting cadence, reactions and forward sources.
- [TED Contract Expiry Radar - Recompete Leads](https://github.com/getdatagrit/ted-contract-expiry-radar) - Find EU public contracts approaching expiry from TED award notices: incumbent, buyer, value, end date and renewal options.

All Actors: [https://getdatagrit.github.io/](https://getdatagrit.github.io/) · [Apify Store](https://apify.com/datagrit)

---

This repository holds documentation and usage examples. Questions, bug reports and feature requests: use the **Issues** tab of the Actor page on [Apify Store](https://apify.com/datagrit/bluesky-community-finder). Examples are MIT licensed.
