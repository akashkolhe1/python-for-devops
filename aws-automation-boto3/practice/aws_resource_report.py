# Practice: list S3 buckets + EC2 instances and save a JSON report.

import json  # noqa: F401
from pathlib import Path  # noqa: F401

import boto3  # noqa: F401


def build_report(session):
    # TODO: s3 client -> bucket names, ec2 client -> instances (id + state).
    # TODO: return {"s3_buckets": [...], "ec2_instances": [...]}
    raise NotImplementedError("Implement build_report")


def main():
    session = boto3.Session()
    # TODO: call build_report, print it, save to aws_report.json.
    # TODO (bonus): handle BotoCoreError / ClientError.
    pass


if __name__ == "__main__":
    main()
