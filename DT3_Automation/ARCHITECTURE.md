# DT3 System Architecture Documentation

## System Overview

**Project:** DT3 Event-Driven Automation Framework  
**Owner:** Dayo Odutayo (President & CEO, Daniel Timothy)  
**Purpose:** Unified orchestrator between OpenAI Assistants, Jarvis, and Zapier

## Core Components

### 1. main_dispatcher.py
Central event-driven orchestrator that handles:
- Automation routing
- Retry logic with exponential backoff
- Logging and monitoring
- Error handling

### 2. router.py
Thin router for webhooks and API entry points:
- Receives incoming webhooks
- Forwards requests to dispatcher
- Handles initial request validation

### 3. relay_config.json
Configuration file that maps automation keys to their handlers:
- Maps `automation_key` → `assistant_id` / `zap_url`
- Defines function-to-assistant relationships
- Stores webhook URLs and API endpoints

### 4. gpt_oss (GitHub Integration Layer)
Integration layer for deployment and training synchronization:
- GitHub Actions workflows
- Automated deployment to Jarvis/Zapier Functions
- CI/CD pipeline management

## Architecture Principles

### Event-Driven Design
- **Asynchronous processing**: All automations run asynchronously
- **Event-based triggers**: Webhooks and API calls trigger automation flows
- **Decoupled components**: Loose coupling between dispatcher, router, and handlers

### Multi-Agent Orchestration
- **OpenAI Assistants**: AI-powered automation tasks
- **Jarvis**: Internal automation platform
- **Zapier Functions**: Third-party integration and automation

### Key Concepts

#### Automation Key
Each automation is identified by an `automation_key` (e.g., `"prospecting_auto_approver"`):
```json
{
  "automation_key": "prospecting_auto_approver",
  "assistant_id": "asst_xxxxx",
  "webhook_url": "https://hooks.zapier.com/..."
}
```

#### Execution Flow
1. Webhook/API call received by `router.py`
2. Router forwards to `main_dispatcher.py`
3. Dispatcher looks up handler in `relay_config.json`
4. Executes via `run_assistant` (OpenAI) or webhook (Zapier)
5. Returns result with logging and error handling

## Runtime Characteristics

- **Event-driven**: Triggered by external events
- **Async**: Non-blocking execution
- **Resilient**: Exponential backoff for retries
- **Monitored**: Comprehensive logging and error tracking

## Integration Points

### OpenAI Assistants
- Custom AI agents for specific automation tasks
- Configured via assistant_id in relay_config.json
- Executed via OpenAI API

### Jarvis Platform
- Internal automation and workflow management
- Deployment target for production automations
- Token-based authentication

### Zapier Functions
- Third-party integrations
- Webhook-based execution
- API key authentication
- **MCP Integration**: Model Context Protocol endpoint at `https://mcp.zapier.com/api/mcp/a/20284927/mcp`
  - Structured communication with Zapier platform
  - Deploy functions programmatically
  - Sync automation configurations
  - Manage triggers and actions

## Development Workflow

1. Define automation in `relay_config.json`
2. Implement handler logic in dispatcher
3. Deploy via GitHub Actions workflow
4. Monitor execution and logs
5. Iterate based on results

## Deployment

Automated deployment via GitHub Actions:
- Triggered on push to `DT3_Automation/**`
- Deploys to both Jarvis and Zapier Functions
- Uses secrets: `ZAPIER_API_KEY`, `JARVIS_TOKEN`

## Goal

Autonomously manage and execute business automations via OpenAI Assistants + Zapier, providing a unified orchestration layer for event-driven workflows.
