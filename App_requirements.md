Create a NextJS social media API inegestor aggregator SaaS application to generate passive income.

Coded on Github / Codespaces

Requirements:
User SM Oauth login
Ability to add 5-10 competitors
cron aggregator runs hourly to build metrics
Dashboard
UI dashboard
Charts
Login
Channel management -? needs defining
YouTube API calls
data processing
database queries
scheduler jobs
database
dashboard
user accounts
billing
sqllite - for initial sample for capture of data

- users
- channels
- tracked_channels
- daily_metrics
- videos

Every 24 or hourly depending on costs
What features to use to intice membership to generate passive income

Pull channel metrics
Save to database

Example project structure - ?
youtube-intelligence/ - ? what is this?

frontend/
nextjs-app/

backend/
api/
collectors/
scheduler/

database/

Example Data Flow
Next.js
↓
GET /api/channels
↓
FastAPI
↓
PostgreSQL
↓
Return JSON
↓
React renders charts

SaaS Stack
Next.js
PostgreSQL
Stripe
Python workers
