import os
import json
import psycopg2

conn = psycopg2.connect(
    dbname="projectdb",
    user="user",
    password="admin123",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

base_path = r"C:\Users\grzag\Desktop\bazy\Projekt-Bazodanowy---MD-MP-main\jsonInstances"

for folder in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder)
    if os.path.isdir(folder_path):
        table_name = folder.lower() + "_jsonb"
        print(f"Creating table: {table_name}")

        cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id SERIAL PRIMARY KEY,
                data JSONB
            );
        """)

        for file in os.listdir(folder_path):
            if file.endswith(".json"):
                file_path = os.path.join(folder_path, file)
                try:
                    with open(file_path, encoding="utf-8") as f:
                        json_data = json.load(f)
                        if isinstance(json_data, list):
                            for item in json_data:
                                cur.execute(f"INSERT INTO {table_name} (data) VALUES (%s)", [json.dumps(item)])
                        else:
                            cur.execute(f"INSERT INTO {table_name} (data) VALUES (%s)", [json.dumps(json_data)])
                except Exception as e:
                    print(f"Error in {file}: {e}")

conn.commit()
cur.close()
conn.close()
print("DONE.")
