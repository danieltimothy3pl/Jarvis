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
4. Add the required secrets

## Files

- `deploy.py`: Main deployment script that handles deployments to Zapier MCP and Jarvis
- `config.json`: Configuration file for Zapier MCP endpoint and automation settings
- `ARCHITECTURE.md`: Detailed system architecture documentation
- `README.md`: This file

## Customization

You can customize the deployment logic in `deploy.py` to fit your specific needs:

- Add API calls to Zapier Functions
- Integrate with Jarvis endpoints
- Add notifications to Teams or Slack
- Implement custom deployment logic

## Testing Locally

You can test the deployment script locally by setting the environment variables:

```bash
export ZAPIER_API_KEY="your-zapier-api-key"
export JARVIS_TOKEN="your-jarvis-token"
python deploy.py
```
