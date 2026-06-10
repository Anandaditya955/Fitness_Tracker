# AI Agent for EKS Operations

This AI assisted operations script analyzes Kubernetes workloads running on Amazon EKS.

## Features

- Checks pod status
- Detects CrashLoopBackOff
- Detects ImagePullBackOff
- Detects Pending pods
- Checks Kubernetes services
- Checks application logs
- Generates troubleshooting commands

## Usage

python3 eks_ai_agent.py

Input:

Namespace: fitness-prod
App Label: fitness-tracker

## Output

The script generates an AI-style operations report with issue detection and recommended kubectl commands.
