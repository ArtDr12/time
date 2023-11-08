from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

print("Content-Type: text/html")
print()
print(f"<H1>Current Time {current_time}</H1>")
