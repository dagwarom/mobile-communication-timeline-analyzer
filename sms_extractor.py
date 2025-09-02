import subprocess
import pandas as pd
import os

def extract_sms():
    try:
        # Run adb command to fetch SMS
        result = subprocess.run(
            [r"C:\platform-tools\adb.exe", "shell", "content", "query", "--uri", "content://sms"],
            capture_output=True, text=True, encoding="utf-8", errors="ignore"
        )

        if result.returncode != 0 or not result.stdout:
            print("❌ Error: Unable to fetch SMS. Check if SMS content provider is accessible.")
            print("ADB Error:", result.stderr)
            return

        raw_sms = result.stdout.strip().splitlines()
        sms_data = []

        for line in raw_sms:
            sms_dict = {}
            for part in line.split(", "):
                if "=" in part:
                    key, value = part.split("=", 1)
                    sms_dict[key.strip()] = value.strip()
            sms_data.append(sms_dict)

        if not sms_data:
            print("⚠️ No SMS data found.")
            return

        df = pd.DataFrame(sms_data)

        # --- Clean important fields ---
        if "address" not in df.columns:
            df["address"] = ""
        if "type" not in df.columns:
            df["type"] = ""
        if "date" not in df.columns:
            df["date"] = ""
        if "body" not in df.columns:
            df["body"] = ""

        # Convert date (ms → datetime), handle NaN safely
        df["date"] = pd.to_numeric(df["date"], errors="coerce")
        df["date"] = pd.to_datetime(df["date"], unit="ms", errors="coerce")

        # Map type (1 = Inbox/Incoming, 2 = Sent/Outgoing)
        type_map = {"1": "INCOMING", "2": "OUTGOING"}
        df["type"] = df["type"].map(type_map).fillna(df["type"])

        # Final clean dataset
        df_clean = df[["address", "type", "date", "body"]]

        # Save in ../data/ folder
        output_dir = "../data"
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, "sms_clean.xlsx")

        df_clean.to_excel(output_file, index=False)
        print(f"✅ SMS extracted and saved to {output_file}")

    except Exception as e:
        print("❌ Exception occurred:", str(e))


if __name__ == "__main__":
    extract_sms()
