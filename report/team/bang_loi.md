# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Trần Bảo Long · Người gắn nhãn 2: Nguyễn Ngọc Bách (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Trùng | Do người dùng |
| 2 | Hệ thống | Hệ thống | Trùng | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Trùng | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Trùng | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Trùng | Ngầm |
| 6 | Do người dùng | Do người dùng | Trùng | Do người dùng |
| 7 | Hệ thống | Hệ thống | Trùng | Hệ thống |
| 8 | Hệ thống | Hệ thống | Trùng | Hệ thống |
| 9 | Do người dùng | Do người dùng | Trùng | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Trùng | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Trùng | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Trùng | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Trùng | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Trùng | Do người dùng |
| 15 | Hệ thống | Hệ thống | Trùng | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Trùng | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Trùng | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Trùng | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Trùng | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Trùng | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100%

## Quy tắc phân biệt cho các ca không trùng

Đồng thuận đạt 20/20 (100% ≥ 80%). Các nguyên tắc phân biệt cốt lõi bám theo nguyên nhân gốc:

- **Ca 6, 9 là do người dùng, không phải hệ thống:** Nguyên nhân gốc do khách chọn sai danh mục hoặc nhập sai định dạng mã vận đơn; hệ thống xử lý đúng theo đầu vào được cấp.
- **Ca 8 là lỗi hệ thống:** Trích dẫn điều khoản không tồn tại (hallucination) là lỗi sinh nội dung sai của mô hình/hệ thống, dù số tiền hoàn ngẫu nhiên vẫn đúng.
- **Ca 10, 16 là lỗi ngữ cảnh:** Trợ lý từ chối đúng chính sách bão hoặc gửi thông báo đúng lúc xong việc, nhưng vi phạm ngữ cảnh cam kết app hoặc gây phiền toái vào ban đêm.
- **Ca 12 là lỗi ngầm:** Kết quả bên ngoài vẫn đúng nên người dùng và nhân viên không biết, nhưng bên trong bị lặp gọi tool làm chi phí token tăng gấp 3 lần suốt 3 tuần.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo khi quá 2% số yêu cầu/ngày | Nhận diện mã sàn TMĐT và tra sang mã vận đơn; không tra được thì hướng dẫn kèm ảnh | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: tin nhắn “đã hoàn” không có bản ghi sổ cái ok cùng `trace_id`; ngưỡng 0 ca | Chỉ báo “đã hoàn” khi sổ cái trả ok; lỗi 503 sau 3 lần thì báo “đang xử lý” và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ mở lại vì lý do số tiền mà kiểm tra thấy đúng, theo dõi theo tuần | Mẫu tin nhắn luôn ghi rõ công thức tính minh bạch: 30.000 đ × 50% = 15.000 đ | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason = thieu_du_lieu`, theo loại yêu cầu | Giữ luồng chuyển tiếp kèm bản tóm tắt; đưa `quoc_te` ra khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn/tuần so với bảng giá hiện hành; ngưỡng 1% đơn lệch | Xoá bộ nhớ đệm tự động khi phát hành bảng giá mới; ghi phiên bản bảng giá vào trace | Kế toán trưởng |
