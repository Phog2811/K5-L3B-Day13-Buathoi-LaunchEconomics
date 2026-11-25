# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Buathoi · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc (gấp 16,3 lần hoá đơn token+tool chia yêu cầu: 274,7 đ); phạm vi `noi_dia` + `hang_nang` cộng cố định 40tr/tháng là 4.599 đ/việc | Giả lập | Kỹ sư trưởng agent |
| 2 · Ba yếu tố nhạy nhất | Làm lại (+51,8%), Xem lại (+40,7%), Lương nhân viên (+23,1%); token chỉ +5,6% | Giả lập | Kỹ sư trưởng agent |
| 3 · So với nhân viên tự làm | Chi phí cả hệ thống 5.865 đ/yêu cầu = 0,49× mức 12.000 đ; xem lại 100% chi phí lên 11.743 đ – 12.415 đ (0,98× – 1,03×) | Giả lập | Kế toán trưởng |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đóng 24h & không mở lại 7 ngày: 82,83% (994/1.200); bỏ qua gợi ý: 27,12% (48/177); mở lại 7 ngày: 4,25% (toàn mẫu), 3,97% (trong phạm vi) | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca lỗi (PAIR: 4 người dùng, 5 hệ thống, 4 ngữ cảnh, 4 giới hạn, 3 ngầm); đồng thuận 20/20 (100%); 5 ca khắc phục kèm event đo lường | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 6 · Pilot plan | 20 nhân viên can thiệp vs 20 đối chứng (c = 20), MDE = 0,06 (power 80%, m >= 299/người, n hiệu dụng 859); 3 luật dừng và rollback 30 phút | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Xem lại 100% làm mất hoàn toàn lợi ích kinh tế (1,03× mức 12.000 đ [simulated]); chạy lại 3 lần tốn kém hơn giới hạn 2 lần (thêm 136.365 đ [simulated]) | Giả lập | Kế toán trưởng |

**Đề xuất:** Go có điều kiện

**Lý do và các điều kiện bắt buộc trước khi rollout:**
Nhóm đề xuất **Go có điều kiện** cho kế hoạch pilot tại 12 depot trên phạm vi thu hẹp `noi_dia` + `hang_nang` (loại bỏ `quoc_te` vì chi phí cao 22.515 đ [simulated] và `doi_tac`), với 4 điều kiện tiên quyết:
1. **Khắc phục lỗi chặn kỹ thuật (Trước ngày 01/12/2026):** Kỹ sư trưởng agent triển khai khoá chống hoàn trùng lặp (idempotency key, ca 20) và cơ chế đối soát trạng thái sổ cái trước khi gửi tin nhắn cho khách (ca 7).
2. **Ký duyệt đánh đổi thống kê (Trước ngày 05/12/2026):** Giám đốc vận hành ký biên bản chấp thuận thiết kế MDE = +6 điểm phần trăm (power 64,17% nếu tác động thực tế chỉ đạt +5 điểm phần trăm).
3. **Hoàn thiện hệ thống telemetry (Trước ngày rollout tuần 1):** Bật đầy đủ 10 sự kiện giám sát mang `trace_id` trong luồng xử lý; bắt đầu đo thời gian xem lại/làm lại thực tế của nhân viên thay thế số giả lập (`simulated`).
4. **Lộ trình giảm tỉ lệ xem lại:** Thiết lập kế hoạch giảm tỉ lệ xem lại theo bậc (từ 100% trong tuần 1 giảm dần xuống dưới 30%), đảm bảo thời gian xem lại thực tế $\le 4,8$ phút/ca để duy trì hiệu quả tiết kiệm chi phí.
