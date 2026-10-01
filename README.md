# Tutorial
## Files in this repo
- *Dockerfile* -> Dockerfile in your /openclaw folder
- *openclaw.json* -> in your openclaw config directory (default should be ~/.openclaw)
- *AGENTS.md* -> inside /workspace in the openclaw config (default ~/.openclaw/workspace)

## Getting the docker containers ready
- Git clone the openclaw repo
- Navigate to the openclaw folder
- run ```export OPENCLAW_IMAGE="ghcr.io/openclaw/openclaw:latest"
./scripts/docker/setup.sh
docker compose up -d```


## After building/running Containers
*Follow along the openclaw onboarding*

Some additional things you should get ready first
### Preferred AI API Key
If using Gemini -> Google AI Studio
### Google Calendar API Setup
1. Visit [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project 
3. Configure consent screen (Audience: External)
4. Enable Google Calendar API
5. Navigate to `OAuth Consent screen` -> `Data access`
6. Add `.../auth/calendar` scope
7. Go to `Audience`
  - User Type: External
  - Add a test user (your own email) (Note: With test user, you have to re-auth every 7 days)

#### Credentials
1. Navigate to `Credentials`
2. Add a new OAuth Client ID and donwload the credentials file
  - Application type: Desktop

### gog
1. Install [gogcli](https://gogcli.sh/install.html#windows)
2. run `gog auth credentials <path-to-credential-file>`
3. run `gog auth add <your-email>`
4. After 7 days if token expires, rerun `gog auth add` again
