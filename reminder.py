import tkinter as tk
from tkinter import messagebox
import json
import os
import time
import schedule
import threading
import sys
import shutil
from win11toast import toast
from PIL import Image
import pystray
from pystray import MenuItem as item
import winsound # Thư viện có sẵn của Windows để phát âm thanh

CONFIG_FILE = "config.json"

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {"checkin": "07:30", "checkout": "17:35", "break_interval": "45"}

def save_config(checkin, checkout, interval):
    with open(CONFIG_FILE, "w") as f:
        json.dump({"checkin": checkin, "checkout": checkout, "break_interval": interval}, f)

# --- Tính năng Bảo vệ Mắt ---
def dim_screen():
    # Tạo cửa sổ mờ toàn màn hình
    dimmer = tk.Tk()
    dimmer.attributes("-alpha", 0.5) # Độ mờ 50%
    dimmer.attributes("-fullscreen", True)
    dimmer.attributes("-topmost", True)
    dimmer.config(bg="black")
    dimmer.overrideredirect(True) # Xóa thanh tiêu đề

    label = tk.Label(dimmer, text="👀 NGHỈ MẮT VÀ VẬN ĐỘNG THÔI!\n(Tự động đóng sau 20 giây)", 
                     fg="white", bg="black", font=("Arial", 30, "bold"))
    label.pack(expand=True)

    # Phát tiếng bíp cảnh báo
    winsound.Beep(1000, 500)
    
    # Đóng sau 20 giây
    dimmer.after(20000, dimmer.destroy)
    dimmer.mainloop()

def break_reminder_loop():
    while True:
        config = load_config()
        interval = int(config.get("break_interval", 45))
        time.sleep(interval * 60) # Chờ x phút
        dim_screen()

# --- Logic Nhắc nhở cũ ---
def send_notif(mode="checkin"):
    config = load_config()
    if mode == "checkin":
        toast("🔔 Check-in!", f"Đến giờ rồi ({config['checkin']}). Check-in thôi!")
    else:
        toast("🔔 Check-out!", f"Đã sau {config['checkout']}. Về thôi anh em!")

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(10)

def setup_schedule():
    config = load_config()
    schedule.clear()
    days = [schedule.every().monday, schedule.every().tuesday, schedule.every().wednesday, 
            schedule.every().thursday, schedule.every().friday, schedule.every().saturday]
    for day in days:
        day.at(config['checkin']).do(send_notif, mode="checkin")
        day.at(config['checkout']).do(send_notif, mode="checkout")

# --- System Tray & UI ---
def quit_app(icon, item):
    icon.stop()
    os._exit(0)

def show_settings(icon, item):
    icon.stop()
    threading.Thread(target=start_ui).start()

def start_ui():
    root = tk.Tk()
    root.title("Reminder Ultimate")
    root.geometry("350x300")
    
    config = load_config()

    tk.Label(root, text="Giờ Check-in (HH:MM):").pack(pady=2)
    entry_in = tk.Entry(root)
    entry_in.insert(0, config['checkin'])
    entry_in.pack()

    tk.Label(root, text="Giờ Check-out (HH:MM):").pack(pady=2)
    entry_out = tk.Entry(root)
    entry_out.insert(0, config['checkout'])
    entry_out.pack()

    tk.Label(root, text="Cứ sau bao nhiêu phút thì nhắc vận động?").pack(pady=2)
    entry_interval = tk.Entry(root)
    entry_interval.insert(0, config['break_interval'])
    entry_interval.pack()

    def on_save():
        save_config(entry_in.get(), entry_out.get(), entry_interval.get())
        setup_schedule()
        root.destroy()
        
        # Chạy System Tray
        icon_path = resource_path("logo.ico")
        img = Image.open(icon_path) if os.path.exists(icon_path) else Image.new('RGB', (64, 64), color='blue')
        menu = (item('Cài đặt', show_settings), item('Thoát', quit_app))
        icon = pystray.Icon("Reminder", img, "Reminder Ultimate", menu)
        icon.run()

    tk.Button(root, text="Lưu & Chạy ngầm", command=on_save, bg="#FF5722", fg="white", font=("Arial", 10, "bold")).pack(pady=15)
    root.mainloop()

if __name__ == "__main__":
    if "--test" in sys.argv:
        dim_screen()
        sys.exit()

    setup_schedule()
    
    # Chạy thread nhắc nhở checkin/out
    threading.Thread(target=run_schedule, daemon=True).start()
    # Chạy thread bảo vệ mắt
    threading.Thread(target=break_reminder_loop, daemon=True).start()

    start_ui()