
# 🧹 Profanity Checker GUI

Ứng dụng Python đơn giản với giao diện Tkinter dùng để **kiểm tra và phát hiện từ ngữ tục tĩu** trong câu văn. Công cụ hữu ích cho việc xử lý văn bản, kiểm duyệt nội dung hoặc xây dựng chatbot.

## 🖼️ Giao diện người dùng
Ứng dụng có giao diện đơn giản, cho phép người dùng:
- Nhập câu bất kỳ
- Kiểm tra câu có chứa từ tục tĩu hay không
- Hiển thị từ tục tĩu nếu có

## 📂 Cấu trúc dự án
```
profanity-checker-gui/
│
├── 2174802010361_MacDuyPhuc_XLNNTN_nhom14.py              # File chính: xử lý và hiển thị GUI
├── profanity.csv            # Danh sách từ tục tĩu (1 từ mỗi dòng)
└── README.md                # Tài liệu giới thiệu dự án
```

## 🚀 Hướng dẫn chạy ứng dụng

### 1. Cài đặt thư viện cần thiết

```bash
pip install pandas nltk
```

### 2. Chạy chương trình

```bash
python 2174802010361_MacDuyPhuc_XLNNTN_nhom14.py 
```

> ⚠️ Lưu ý: Lần đầu chạy, ứng dụng sẽ tự động tải các tài nguyên NLTK như `punkt`.

### 3. File `profanity.csv`
- Là danh sách các từ tục tĩu (mỗi từ trên một dòng).
- Không có header.
- Không để trống dòng.

Ví dụ:

```
fuck
motherfukr
assbag
```

## 🧠 Công nghệ sử dụng
- `Python` (3.x)
- `Tkinter`: giao diện người dùng
- `pandas`: đọc file CSV
- `nltk`: tiền xử lý văn bản, tách từ

## 📜 Giấy phép
MIT License – tự do sử dụng và chỉnh sửa.

## ✍️ Tác giả
- Tên bạn ở đây (nếu bạn muốn)
