# Import các thư viện
import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
import tkinter as tk
from tkinter import messagebox

# Download các resource của NLTK nếu chưa được download
nltk.download('punkt')
nltk.download('punkt_tab')

# Đọc dữ liệu từ file CSV
def load_data(file_path):
    df = pd.read_csv(file_path, header=None, names=["text"])
    return set(df["text"].str.lower())

# Tiền xử lý văn bản
def preprocess_text(text):
    # Loại bỏ các ký tự không cần thiết như dấu câu và ký tự đặc biệt
    text = re.sub(r'[^\w\s]', '', text)
    # Chuyển đổi văn bản về chữ thường
    text = text.lower()
    return text

# Kiểm tra xem từ trong câu có trong tập dữ liệu từ tục tĩu hay không
def check_profanity(sentence, profanity_words):
    sentence = preprocess_text(sentence)
    words = word_tokenize(sentence)  # Sử dụng NLTK để tokenize câu
    profanity_found = []
    for word in words:
        if word in profanity_words:
            profanity_found.append(word)
    return len(profanity_found) > 0, ", ".join(profanity_found)

# Hàm xử lý sự kiện khi người dùng nhấn nút "Kiểm tra"
def check_input():
    global profanity_words
    user_input = entry.get()  # Lấy dữ liệu nhập từ người dùng
    is_profanity, profanity_word = check_profanity(user_input, profanity_words)  # Kiểm tra từ nhập từ người dùng
    if is_profanity:
        messagebox.showinfo("Kết quả", f"Từ tục tĩu '{profanity_word}' được tìm thấy trong câu của bạn: '{user_input}'")
    else:
        messagebox.showinfo("Kết quả", "Không tìm thấy từ tục tĩu trong câu của bạn.")

# Hàm khởi tạo giao diện Tkinter
def create_gui():
    root = tk.Tk()
    root.title("Kiểm tra từ tục tĩu")
    
    # Giao diện nhập dữ liệu từ người dùng
    entry_label = tk.Label(root, text="Nhập câu của bạn:")
    entry_label.pack()
    global entry
    entry = tk.Entry(root, width=50)
    entry.pack()
    
    # Nút kiểm tra
    check_button = tk.Button(root, text="Kiểm tra", command=check_input)
    check_button.pack()
    
    root.mainloop()

# Đường dẫn tới file CSV chứa các từ tục tĩu
file_path = "profanity.csv"

# Load các từ tục tĩu từ file CSV vào một tập hợp
profanity_words = load_data(file_path)

# Tạo giao diện người dùng
create_gui()
