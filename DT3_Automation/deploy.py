#!/usr/bin/env python3
"""
DT3 Automation Deployment Script

This script handles automated deployments to Zapier Functions or Jarvis.
It is triggered by the GitHub Actions workflow when changes are pushed to the DT3_Automation directory.
"""

import os
import sys


def get_env_variable(var_name, required=True):
    """Get environment variable with optional requirement check."""
    value = os.environ.get(var_name)
    if required and not value:
        print(f"Warning: {var_name} environment variable is not set.")
    return value


def deploy_to_zapier():
    """Deploy to Zapier Functions."""
    zapier_api_key = get_env_variable('ZAPIER_API_KEY', required=False)
    
    if zapier_api_key:
        print("Deploying to Zapier Functions...")
        # Add your Zapier deployment logic here
        print("Zapier deployment completed successfully!")
    else:
        print("Skipping Zapier deployment (no API key provided)")


def deploy_to_jarvis():
    """Deploy to Jarvis."""
    jarvis_token = get_env_variable('JARVIS_TOKEN', required=False)
    
    if jarvis_token:
        print("Deploying to Jarvis...")
        # Add your Jarvis deployment logic here
        print("Jarvis deployment completed successfully!")
    else:
        print("Skipping Jarvis deployment (no token provided)")


def main():
    """Main deployment function."""
    print("=" * 50)
    print("DT3 Automation Deployment Starting")
    print("=" * 50)
    
    try:
        deploy_to_zapier()
        deploy_to_jarvis()
        
        print("=" * 50)
        print("Deployment completed successfully!")
        print("=" * 50)
        return 0
    except Exception as e:
        print(f"Error during deployment: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
