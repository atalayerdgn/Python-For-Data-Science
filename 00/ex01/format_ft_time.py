import time
from datetime import datetime

timestamp = time.time()
scientific_notation = f"{timestamp:.2e}"
readable_date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
print(f"Seconds since January 1, 1970: {timestamp:.4f} or {scientific_notation} in scientific notation$")
print(readable_date + "$")
