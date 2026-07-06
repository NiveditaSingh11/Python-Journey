from datetime import datetime ,timedelta

now = datetime.now()
print(f"current timestamp : {now}")

result =now - timedelta(days=3)
print(f"3 days before , it was -> {result}")

formatted =now.strftime("%d-%m-%Y  %H:%M")
print(formatted)