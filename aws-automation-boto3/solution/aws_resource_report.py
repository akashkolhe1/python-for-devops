# Solution: list S3 buckets + EC2 instances and save a JSON report.

import json
from pathlib import Path

import boto3
from botocore.exceptions import BotoCoreError, ClientError

OUTPUT = Path(__file__).parent / "aws_report.json"


def build_report(session):
    s3 = session.client("s3")
    ec2 = session.client("ec2")

    buckets = [b["Name"] for b in s3.list_buckets().get("Buckets", [])]

    instances = []
    for reservation in ec2.describe_instances().get("Reservations", []):
        for inst in reservation.get("Instances", []):
            instances.append(
                {"id": inst["InstanceId"], "state": inst["State"]["Name"]}
            )

    return {"s3_buckets": buckets, "ec2_instances": instances}


def main():
    session = boto3.Session()
    try:
        report = build_report(session)
    except (BotoCoreError, ClientError) as exc:
        print("AWS call failed (check your credentials/region):", exc)
        return

    print(json.dumps(report, indent=2))
    OUTPUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"\nWrote {OUTPUT.name}")


if __name__ == "__main__":
    main()
