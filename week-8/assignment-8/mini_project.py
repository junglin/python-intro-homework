import csv

def load_data():
    try:
        with open("../data/messy_data.csv", "r") as d:
            reader = csv.DictReader(d)
            skipped = []
            clean_data = []
            rows_attempted = 0
            rows_parsed = 0
            for row_num, row in enumerate(reader, start=1):
                rows_attempted += 1
                if None in row:
                    skipped.append(f"Row {row_num}: extra column detected — skipped")
                    continue
                try:
                    amount = float(row["amount"])
                    row["amount"] = amount
                    clean_data.append(row)
                    rows_parsed += 1
                except ValueError as e:
                    skipped.append(f"Row {row_num}: ValueError — could not convert '{row['amount']}' to float")
                except KeyError as e:
                    skipped.append(f"Row {row_num}: KeyError — missing column {e}")
            print("=== CSV Report ===")
            print(f"Rows attempted: {rows_attempted}")
            print(f"Rows parsed: {rows_parsed}")
            print(f"Rows skipped: {len(skipped)}")
            print("\nSkipped rows:")
            for item in skipped:
                print(f"{item}")
            print("\nClean data:")
            for row in clean_data:
                print(f"{row['name']} | {row['category']} | ${row['amount']:.2f}")

    except FileNotFoundError:
        print("Error: '../data/messy_data.csv' was not found. Please check the file path and try again.")
        return

load_data()


