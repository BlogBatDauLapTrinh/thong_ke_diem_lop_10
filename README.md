
# **Thống kê điểm lớp 10 Bình Dương năm 2022**

Toàn bộ dữ liệu được crawl trực tiếp từ [trang web của sở giáo dục Bình Dương](https://binhduong.edu.vn/tra-cuu-diem-tuyen-sinh-lop-10.html)

Và các bạn có thể truy cập trực tiếp các file thống kê [tại đây](https://batdaulaptrinh.com/thong-ke-diem-tuyen-sinh-lop-10-binh-duong-2022/)

### Môi trường và thư viện

- Python3
- BeautifulSoup
- Selenium
- Openpyxl

### Work-flow

Bước 1: Crawl dữ liệu của thí sinh bằng cách sử dụng `Selenium` và phân tách các dữ liệu quan trọng bằng `BeautifulSoup` và lưu trữ dưới dạng `.csv`

Bước 2: Sử dụng thư viện `pandas` để thực hiện sắp xếp thứ tự theo tổng điểm và tuất file Excel dưới dạng `xlsx`