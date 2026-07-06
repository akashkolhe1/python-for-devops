# AWS Automation with Python (Boto3 + IaC)

AWS is managed with APIs, not clicks. This module shows how Python automates the
cloud with Boto3 (read-only here), plus an intro to Infrastructure as Code with
AWS CDK.

The examples only read from AWS (list S3 buckets, list EC2 instances). Nothing
is created, modified, or deleted unless you choose to run the optional create
helpers.

---

## Learning objectives

- Connect to AWS from Python using [`boto3`](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- List S3 buckets and EC2 instances, and save a report to JSON
- Understand when to use Boto3 (glue/reporting) vs. IaC tools (Terraform/CloudFormation) for CRUD
- Understand the idea of Infrastructure as Code with AWS CDK (Python)

## Prerequisites

- An AWS account with credentials configured locally:
  ```bash
  aws configure          # or set AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY / AWS_DEFAULT_REGION
  ```
  Guide: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## What's inside

```
aws-automation-boto3/
├── examples/
│   ├── s3_utilities.py         # AWSUtils class: list buckets, (optional) create/upload
│   ├── aws_resource_report.py  # list S3 + EC2 and write aws_report.json
│   └── cdk_demo/               # IaC intro: a CDK stack defining one S3 bucket
│       ├── app.py
│       └── README.md
├── practice/
│   ├── aws_resource_report.py
│   └── README.md
└── solution/
    └── aws_resource_report.py
```

## How to run

```bash
# List your S3 buckets + EC2 instances and write a JSON report
python examples/aws_resource_report.py

# Just the S3 helper class
python examples/s3_utilities.py
```

These call real AWS APIs and need valid credentials. Without them you'll get a
`NoCredentialsError` / `ClientError` — that's expected.

## Boto3 vs. Infrastructure as Code

- Boto3 is great for reading state, reporting, and one-off automation.
- For creating/updating/deleting infrastructure, prefer IaC tools (Terraform,
  CloudFormation, CDK) — they track state, are repeatable, and reviewable. See
  [`examples/cdk_demo/`](examples/cdk_demo/) for the CDK idea.

## Practice

See [`practice/README.md`](practice/README.md).
