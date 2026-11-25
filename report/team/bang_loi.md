# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Trần Bảo Long · Người gắn nhãn 2: Nguyễn Ngọc Bách (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 (Trần Bảo Long) | Nhãn người 2 (Nguyễn Ngọc Bách) | Trùng? | Nhãn thống nhất |
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

**Tỉ lệ đồng thuận:** 20 / 20 = 100% (4 Do người dùng · 5 Hệ thống · 4 Ngữ cảnh · 4 Giới hạn hệ thống · 3 Ngầm)

## Quy tắc phân biệt cho các ca không trùng

Đồng thuận đạt 20/20 (100% ≥ 80%, không có ca lệch). Các nguyên tắc phân biệt cốt lõi theo nguyên nhân gốc được nhóm thống nhất cho các ca dễ lẫn:

- **Ca 6, 9 là Do người dùng, không phải Hệ thống:** Nguyên nhân gốc do khách chọn sai mục hoặc nhập mã sàn TMĐT thay cho mã vận đơn; việc bổ sung gợi ý nằm ở cột khắc phục.
- **Ca 8, 15 là Hệ thống, không phải Ngầm:** Lỗi đã lộ ra (trích dẫn điều khoản 7.2 không tồn tại nhìn thấy ngay; tính sai 100% bị nhân viên xem lại phát hiện trước khi gửi).
- **Ca 13 là Giới hạn hệ thống:** Yêu cầu ngoài phạm vi trợ lý (bảo hiểm của đối tác) là giới hạn hệ thống, kể cả khi trợ lý phản hồi chung chung.
- **Ca 10, 16, 18 là Ngữ cảnh:** Trợ lý xử lý đúng thiết kế/chính sách nhưng giả định không khớp hoàn cảnh của khách (bão bất khả kháng vs cam kết 24h trên app, gửi Zalo lúc 2:14 sáng, thiếu công thức tính trong tin nhắn).
- **Ca 12 là Ngầm:** Kết quả bên ngoài vẫn đúng nên không ai nhận ra, nhưng gọi lặp tool khiến chi phí token depot D05 gấp 3 lần suốt 3 tuần.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện đo được (event, ngưỡng, tần suất) và đồng bộ với danh sách event trong `report/team/chi_so.md`. Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` (bổ sung gắn `trace_id`) hoặc `agent_run_completed` (`status = loi` do sai định dạng mã); cảnh báo khi > 2% số yêu cầu/ngày | Tự nhận diện mã đơn sàn TMĐT để tra chéo sang mã vận đơn LogiX; nếu không tra được thì hiển thị hướng dẫn kèm ảnh vị trí mã vận đơn | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát tự động mỗi giờ giữa tin nhắn báo "đã hoàn" (`ticket_closed`) và bản ghi `refund_ledger_write` (`ket_qua = ok`) cùng `trace_id`; ngưỡng cảnh báo: > 0 ca lệch | Chỉ cho phép báo "đã hoàn tiền thành công" khi `refund_ledger_write` trả `ok` kèm `idempotency_key`; gặp lỗi 503 sau tối đa 2 lần thử thì báo "đang xử lý" và phát `handoff_to_staff` | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Thống kê hằng tuần tỉ lệ `ticket_reopened` có `reason = thieu_tien` nhưng đối soát cho thấy số tiền hoàn đúng chính sách; ngưỡng cảnh báo: > 1% số đơn hoàn một phần/tuần | Chuẩn hoá mẫu tin nhắn luôn hiển thị rõ công thức tính minh bạch (ví dụ: `30.000 đ × 50% = 15.000 đ`) và kênh nhận tiền (ví LogiX hoặc tài khoản ngân hàng) | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason = thieu_du_lieu` hoặc `ngoai_pham_vi`, tổng hợp hằng ngày theo cột `loai`; ngưỡng cảnh báo: > 5% tổng yêu cầu trong phạm vi pilot/ngày | Giữ cơ chế chuyển nhân viên kèm bản tóm tắt ngay ở lần thử 1 (không chạy lại 3 lần); đưa hoàn toàn nhóm `quoc_te` ra khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `audit_sample_checked`: kiểm tra mẫu định kỳ 100 đơn/tuần so sánh `so_tien_da_hoan` với `so_tien_dung` theo `phien_ban_bang_gia` hiện hành; ngưỡng cảnh báo: >= 1% đơn kiểm tra bị lệch | Gắn `phien_ban_bang_gia` vào mọi `agent_run_completed`; tự động xoá bộ nhớ đệm (cache invalidation) khi phát hành bảng giá mới và cảnh báo nếu trace dùng phiên bản cũ | Kế toán trưởng |
