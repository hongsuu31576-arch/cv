from pyngrok import ngrok
import time

# Mở cổng 8501 ra Internet
public_url = ngrok.connect(8501)
print("\n" + "="*50)
print(f"🚀 Link web công khai của bạn: {public_url}")
print("="*50 + "\n")

# Giữ cho link hoạt động
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Đã dừng chia sẻ link.")