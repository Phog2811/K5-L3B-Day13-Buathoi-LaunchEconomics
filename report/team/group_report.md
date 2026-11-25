# Báo cáo nhóm · Lab 13 Launch Economics

Báo cáo ngắn. Số liệu chi tiết nằm trong các file hồ sơ; ở đây dẫn lại các con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Buathoi
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

- Xây dựng hồ sơ launch v0 trả lời 4 câu hỏi cốt lõi tại Gate 2a cho trợ lý hoàn phí LogiX-VN: Có đáng chạy không? Nhân viên có dùng không? Khi hỏng thì sao? Pilot thiết kế thế nào để ra quyết định?
- Tiếp cận phân tích kinh tế thực chứng: tính toán Cost-of-Pass thực tế tính gộp chi phí nhân sự xem lại/làm lại, phân tích độ nhạy, phân loại lỗi theo Google PAIR, thiết kế thử nghiệm ngẫu nhiên phân cụm (Cluster Randomized Controlled Trial) và telemetry có `trace_id`.

## 3. Giải pháp

- **Nhiệm vụ A:** Viết mô hình chi phí trong `src/lab13.py` và tổng hợp tại [bang_chi_phi.md](bang_chi_phi.md). Tử số tính tất cả các lần chạy (kể cả lỗi) và thời gian nhân viên can thiệp, mẫu số chỉ tính 978 việc thành công.
- **Nhiệm vụ B:** Chạy 9 kịch bản độ nhạy đơn và kịch bản kết hợp. Xếp hạng 3 yếu tố nhạy nhất: Làm lại (+51,8%), Xem lại (+40,7%), Lương (+23,1%) [simulated]; token chỉ chiếm +5,6%. Tìm ra giới hạn tối đa 2 lần chạy là tối ưu cho toàn hệ thống.
- **Nhiệm vụ C:** Gắn nhãn độc lập 20 ca lỗi theo Google PAIR đạt đồng thuận 20/20 (100%), thiết lập bảng giải pháp khắc phục cho 5 ca lỗi đại diện tại [bang_loi.md](bang_loi.md).
- **Nhiệm vụ D:** Thiết kế kế hoạch pilot phân bổ theo nhân viên (20 can thiệp vs 20 đối chứng) tại [pilot_plan.yaml](pilot_plan.yaml) với MDE = 0,06 (power 80%, $m \ge 299$, $n_{\text{hiệu dụng}} = 859$), 3 luật dừng và cơ chế rollback 30 phút.
- **Nhiệm vụ E:** Đặc tả telemetry 10 sự kiện mang `trace_id` tại [chi_so.md](chi_so.md), tổng hợp hồ sơ 1 trang tại [ho_so_launch_v0.md](ho_so_launch_v0.md) và thực hiện phản biện chéo tại [phieu_cham.md](phieu_cham.md).

## 4. Kết quả

- **Chi phí mỗi việc thành công:** 4.472 đ [simulated], gấp 16,3 lần hoá đơn token+tool chia số yêu cầu (274,7 đ). Chi phí toàn hệ thống mỗi yêu cầu là 5.865 đ = 0,49× mức 12.000 đ [simulated].
- **Phạm vi hiệu quả:** Thu hẹp về `noi_dia` (2.696 đ = 0,22×) và `hang_nang` (8.221 đ = 0,69× [simulated]). Loại bỏ `quoc_te` (22.515 đ = 1,88× [simulated]). Cộng cố định 40 triệu/tháng là 4.599 đ/việc (0,38×) ở 45.000 yêu cầu/tháng.
- **Chỉ số quan sát trong chạy thử:** Đóng trong 24h & không mở lại trong 7 ngày đạt 82,83%; tỉ lệ bỏ qua gợi ý 27,12%; mở lại trong 7 ngày 4,25% (toàn mẫu) và 3,97% (trong phạm vi).
- **Đề xuất cuối cùng:** **Go có điều kiện** (chỉ triển khai pilot cho `noi_dia` + `hang_nang`, kèm 4 điều kiện: sửa khoá chống trùng lặp/đối soát sổ cái, ký duyệt đánh đổi MDE 6 điểm, bật 10 telemetry event và lộ trình giảm xem lại theo bậc).
- **Kết quả duyệt chéo nhận được từ hội đồng:** Nhóm nhận được quyết định **Go có điều kiện** với điểm số **30/30** (hoặc 95% theo thang tổng thể của lab). Hội đồng đánh giá cao tính minh bạch khi nêu rõ các con số bất lợi và thiết kế pilot chặt chẽ có đối chứng song song; đồng thời có lưu ý nhóm về việc phân biệt nguyên nhân gốc tại Ca 13 (giữa lỗi Hệ thống và Giới hạn hệ thống).

## 5. Khó khăn và cách xử lý

- *Khó khăn về phân loại lỗi:* Ở Ca 13 (khách hỏi hoàn phí bảo hiểm của đối tác, trợ lý trả lời chung chung), nhóm dễ nhầm sang lỗi "Hệ thống" vì tập trung vào việc mô hình không biết từ chối mà lại trả lời lấp liếm. Nhóm đã xử lý và rút ra bài học: phải bám vào nguyên nhân gốc của Google PAIR — nghiệp vụ bảo hiểm đối tác hoàn toàn ngoài phạm vi năng lực (out-of-scope) nên gốc rễ là lỗi "Giới hạn hệ thống".
- *Khó khăn về cỡ mẫu:* Với 40 nhân viên và hệ số tương quan nội cụm ICC = 0,02, không cách chia phân cụm nào đủ mẫu để phát hiện mức chênh 5 điểm phần trăm. Nhóm đã xử lý bằng cách chấp nhận nới MDE lên +6 điểm phần trăm ($m \ge 299$ yêu cầu/nhân viên, n hiệu dụng = 859) và công khai đánh đổi thống kê trong hồ sơ.

## 6. Tổng hợp đóng góp

- **Đinh Hoàng Phong:** Viết code A1–B4 trong `src/lab13.py`, phụ trách `chi_so.md`, quản lý repo.
- **Trần Đình Nhật Minh:** Kiểm số độc lập A–B, điền `bang_chi_phi.md`, viết code D1–E1 trong `src/lab13.py`.
- **Trần Bảo Long:** Người gắn nhãn 1, hoàn thiện `bang_loi.md` và `pilot_plan.yaml`.
- **Nguyễn Ngọc Bách:** Người gắn nhãn 2, hoàn thiện `ho_so_launch_v0.md`, `phieu_cham.md`, `group_report.md`.

## 7. Hạn chế và hướng cải thiện

- Số liệu thời gian xem lại và làm lại hiện tại vẫn là dữ liệu giả lập (`_simulated`). Cần đo lường thời gian thực tế qua telemetry ngay trong tuần đầu tiên của pilot.
- Cần xây dựng cơ chế phát hiện tự động các yêu cầu nằm ngoài phạm vi (như ca 13) để chuyển nhân viên kèm tóm tắt ngay lập tức thay vì đưa ra câu trả lời chung chung.

## 8. Tài liệu tham khảo

- Erol et al., *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arXiv:2504.13359.
- Google PAIR, *People + AI Guidebook: Errors + Graceful Failure*.
- Thư viện `statsmodels.stats.power.NormalIndPower`.
