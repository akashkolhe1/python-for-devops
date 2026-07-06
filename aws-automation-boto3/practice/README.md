# Practice: AWS Resource Report

Requires AWS credentials configured locally (`aws configure`).

## Your task

Complete `practice/aws_resource_report.py` so it:

1. Creates a `boto3.Session()` and an S3 client.
2. Lists all S3 bucket names.
3. Lists EC2 instances (instance id + state).
4. Prints the report and saves it to `aws_report.json`.
5. Bonus: wrap AWS calls in `try / except (BotoCoreError, ClientError)` so a
   missing-credentials situation prints a friendly message instead of a traceback.

Read-only operations only. Do not create/delete resources.

## Run it

```bash
python practice/aws_resource_report.py
```

## Done?

Compare with [`../solution/aws_resource_report.py`](../solution/aws_resource_report.py)
and the fuller [`../examples/aws_resource_report.py`](../examples/aws_resource_report.py).
