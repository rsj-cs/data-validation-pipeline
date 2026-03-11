import random
import time

def generate_records(num_records):
    records = []
    for i in range (num_records):
        record = {
            "id": i + 1,
            "age": random.randint (-5, 100),
            "salary": random.randint (-1000, 150000),
            "name": random.choice (["Alice", "Bob", "", "Charlie", "Dana", ""])
        }
        records.append(record)
    return records

def validate_record(record):
    errors = []
    if record ["age"] < 0 or record ["age"] > 99:
        errors.append("Invalid age")
    if record["salary"] < 0:
        errors.append("Invalid salary")
    if record["name"] == "":
        errors.append("Missing name")
    return errors

def run_pipeline(records):
    clean = []
    rejected = []
    start = time.time()
    for record in records:
        errors = validate_record(record)
        if errors:
            record["errors"] = errors
            rejected.append(record)
        else:
            clean.append(record)
    end = time.time()
    return clean, rejected, end - start

def print_report(clean, rejected, duration):
    total = len(clean) + len(rejected)
    print("=" * 50)
    print("   DATA VALIDATION PIPELINE - REPORT")
    print("=" * 50)
    print(f"  Total Records      : {total}")
    print(f"  Clean Records      : {len(clean)}")
    print(f"  Rejected Records   : {len(rejected)}")
    print(f"  Pass Rate          : {len(clean)/total*100:.1f}%")
    print(f"  Processing Time    : {duration:.4f} seconds")
    print("-" * 50)
    print("  REJECTED RECORD DETAILS:")
    for record in rejected:
        print(f"  ID {record['id']} -> {record['errors']}")
    print("=" * 50)


if __name__ == "__main__":
    records = generate_records(30)
    clean, rejected, duration = run_pipeline(records)
    print_report(clean, rejected, duration)