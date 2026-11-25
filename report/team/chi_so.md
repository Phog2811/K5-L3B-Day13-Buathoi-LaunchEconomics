# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200); trong phạm vi `noi_dia` + `hang_nang`: 3,97% (39/982) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm can thiệp được nhân viên mở bằng trợ lý | số `agent_suggestion_shown` có `arm = tro_ly`, chia số `refund_request_created` có `arm = tro_ly` | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền phát hiện qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 17) | số `audit_sample_checked` có `so_tien_da_hoan` khác `so_tien_dung`, chia số đơn được kiểm tra trong tuần | Không cần tính |

Số tính bằng phần E1 trong `src/lab13.py` (dữ liệu giả lập của lab). Chỉ số chính trong đợt chạy thử là 82,83%; đợt chạy thử không có nhóm đối chứng nên con số này chưa cho biết tác động của trợ lý so với baseline 0,70. Chỉ có pilot chia ngẫu nhiên trong `pilot_plan.yaml` mới tách được tác động.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien_vnd, depot, staff_id, arm, trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện cho nhân viên |
| `staff_review_decision` | Nhân viên | quyet_dinh (giu / sua / bo), phut_xem_lai đo thật, trace_id | Khi nhân viên bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | phut_lam_lai đo thật, ly_do, trace_id | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ hoàn tiền |
| `handoff_to_staff` | Agent | reason (thieu_du_lieu / ngoai_pham_vi / het_lan_chay), tom_tat, trace_id | Khi chuyển yêu cầu cho nhân viên |
| `ticket_closed` | Hệ thống ticket | closed_at, trace_id | Khi ticket đóng |
| `ticket_reopened` | Khách | reopened_at, reason, trace_id | Khi khách mở lại ticket |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, phien_ban_bang_gia, trace_id | Hằng tuần, mẫu 100 đơn |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số chính: `refund_request_created` (mẫu số) + `ticket_closed` (đóng trong 24 giờ, so `closed_at` với lúc tạo) + `ticket_reopened` (không mở lại trong 7 ngày).
- Tỉ lệ bỏ qua gợi ý: `staff_review_decision` (`quyet_dinh` là `sua` hoặc `bo`, chia tổng số event này).
- Tỉ lệ lỗi lọt đến khách: `ticket_reopened` trong 7 ngày, chia `refund_request_created`.
- Chỉ số dùng tự đề xuất: `agent_suggestion_shown` chia `refund_request_created` cùng `arm`.
- Chỉ số an toàn tự đề xuất: `audit_sample_checked`.
- Chi phí mỗi việc thành công trong pilot: `agent_run_completed` (token, tool) + `staff_review_decision` và `staff_rework_completed` (phút đo thật, thay cho cột simulated) + `ticket_closed` / `ticket_reopened` (đếm việc thành công).

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công +51,8%, từ 4.472 đ lên 6.787 đ [simulated] (B1) | Tỉ lệ ca làm lại theo tuần > 7% (đợt chạy thử: 48/982 = 4,9% trong phạm vi `noi_dia` + `hang_nang`) | Thu hẹp về `noi_dia`, rà 20 trace làm lại gần nhất để tìm nguyên nhân | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× của 12.000 đ với 9 phút làm lại; 12.415 đ = 1,03× với 15,3 phút như dữ liệu [simulated] (B4); hoà vốn khi mỗi lần xem lại ≤ 5,1 phút | % yêu cầu được xem lại còn > 50% ở cuối bước rollout 0.25; phút xem lại trung bình đo thật > 5 phút | Giảm tỉ lệ xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng (tổng 4.599 đ = 0,38×), +2.370 đ/việc nếu còn một nửa (5.784 đ = 0,48×) [simulated] (A4) | Số việc thành công theo tuần < 50% kế hoạch | Không mở rộng pilot, xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
| Lương nhân viên tăng | Lương tăng 25% làm chi phí mỗi việc thành công +23,1%, lên 5.506 đ [simulated] (B1) | Đơn giá phút nhân viên trong bảng lương quý | Ưu tiên giảm phút xem lại và làm lại trước khi mở rộng | PM trợ lý hoàn phí |
