import requests
import uuid
import sys

# Mã màu cho terminal
reset = "\033[0m"
red = "\033[91m"
green = "\033[92m"

# Kiểm tra đầu vào từ dòng lệnh
if len(sys.argv) != 4:
    print(f"{red}Cách sử dụng: python3 spam.py <username> <nội_dung> <số_lần>{reset}")
    sys.exit(1)

# Lấy dữ liệu từ dòng lệnh
username = sys.argv[1]
nd = sys.argv[2].replace(" ", "+")
try:
    so_lan = int(sys.argv[3])
except ValueError:
    print(f"{red}Số lần gửi phải là một số nguyên!{reset}")
    sys.exit(1)

# Cấu hình request
url = "https://ngl.link/api/submit"
headers = {
    "accept": "*/*",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36",
    "origin": "https://ngl.link",
    "referer": f"https://ngl.link/{username}"
}

# Gửi yêu cầu nhiều lần
for i in range(so_lan):
    data = {
        "username": username,
        "question": nd,
        "deviceId": str(uuid.uuid4()),  # Tạo ID ngẫu nhiên
        "gameSlug": "",
        "referrer": ""
    }
    try:
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200 and "questionId" in response.json():
            print(f"{green}[{i + 1}] Gửi thành công: '{nd}' tới '{username}'{reset}")
        elif "Could not find user" in response.text:
            print(f"{red}Username '{username}' không tồn tại!{reset}")
            break
        else:
            print(f"{red}[{i + 1}] Thất bại, lỗi: {response.text}{reset}")
    except requests.RequestException as e:
        print(f"{red}Lỗi kết nối: {e}{reset}")
