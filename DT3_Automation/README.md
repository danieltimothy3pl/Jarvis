# DT3 Automation

This directory contains the automation scripts that are automatically deployed when changes are pushed to GitHub.

## How It Works

1. When you push changes to this directory, the GitHub Actions workflow (`.github/workflows/dt3_agent.yml`) is triggered
2. The workflow sets up a Python environment and installs dependencies
3. The `deploy.py` script is executed with the configured secrets
4. Deploys to Zapier MCP endpoint and Jarvis platform

## Zapier MCP Integration

This automation integrates with Zapier's Model Context Protocol (MCP) endpoint:
- **Endpoint**: `https://mcp.zapier.com/api/mcp/a/20284927/mcp`
- **Purpose**: Enable structured communication between DT3 and Zapier platform
- **Features**: Deploy functions, sync configurations, manage triggers/actions

## Setup

To use this automation, you need to configure the following secrets in your GitHub repository:

1. **ZAPIER_API_KEY**: Your Zapier API key for deploying to Zapier Functions
2. **JARVIS_TOKEN**: Your Jarvis authentication token

### Adding Secrets

1. Go to your GitHub repository
2. Navigate to Settings > Secrets and variables > Actions
3. Click "New repository secret"
4. Add the required secrets:
   - `ZAPIER_API_KEY`: Your Zapier API key for deploying to Zapier Functions
   - `JARVIS_TOKEN`: Your Jarvis authentication token
   - `ZAPIER_MCP_ENDPOINT` (optional): Override the MCP endpoint from config.json

## Files

- `deploy.py`: Main deployment script that handles deployments to Zapier MCP and Jarvis
- `config.json`: Configuration file for Zapier MCP endpoint and automation settings
- `ARCHITECTURE.md`: Detailed system architecture documentation
- `README.md`: This file

## Customization

⚠️ **Important**: The deployment logic in `deploy.py` contains placeholder code that needs to be customized for your specific deployment needs.

You should customize the deployment logic in `deploy.py` to fit your specific needs:

- **Zapier Deployment** (lines 56-66): Add actual API calls to deploy to Zapier Functions using the MCP endpoint
- **Jarvis Deployment** (lines 77-80): Add actual API calls or deployment commands for Jarvis platform
- Add notifications to Teams or Slack
- Implement custom deployment logic
- Add error handling and retry logic

### Example Customization

To implement actual Zapier deployment:
```python
import requests

response = requests.post(
    mcp_endpoint,
    headers={"Authorization": f"Bearer {zapier_api_key}"},
    json={"action": "deploy", "automation": "DT3"}
)
response.raise_for_status()
```

## Testing Locally

You can test the deployment script locally by setting the environment variables:

```bash
export ZAPIER_API_KEY="your-zapier-api-key"
export JARVIS_TOKEN="your-jarvis-token"
python deploy.py
```
