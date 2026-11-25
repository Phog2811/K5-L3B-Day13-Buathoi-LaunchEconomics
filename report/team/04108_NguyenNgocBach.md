# Báo cáo cá nhân — Nguyễn Ngọc Bách — 04108

## 1. Thông tin thành viên

- Họ tên: Nguyễn Ngọc Bách
- MSSV: 04108
- Email: bachnguyen2001@gmail.com
- GitHub: bachnguyen2001
- Vai trong nhóm: Người gắn nhãn 2 kiêm giữ hồ sơ; trưởng duyệt chéo Gate 2a.

## 2. Phần việc phụ trách

- Nhiệm vụ C: Gắn nhãn độc lập 20 ca lỗi theo Google PAIR, đối soát đồng thuận với Người gắn nhãn 1, xây dựng bảng biện pháp khắc phục 5 ca lỗi.
- Nhiệm vụ E: Khởi tạo, cập nhật liên tục và hoàn thiện hồ sơ launch v0 (`report/team/ho_so_launch_v0.md`) bám sát số liệu từ các checkpoint.
- Soạn thảo và điều phối phiếu chấm phản biện Gate 2a (`report/team/phieu_cham.md`), hoàn thiện báo cáo nhóm (`report/team/group_report.md`).

## 3. Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi trong 8 phút không trao đổi: đạt tỉ lệ đồng thuận 20/20 (100%) với bạn Trần Bảo Long. Phân loại chuẩn xác 5 nhóm lỗi (4 người dùng, 5 hệ thống, 4 ngữ cảnh, 4 giới hạn hệ thống, 3 lỗi ngầm).
- Đề xuất 5 giải pháp khắc phục đo lường được cho 5 ca tiêu biểu (ca 9, 7, 18, 4, 17) kèm event giám sát và phân định đúng vai trò phụ trách độc lập trong `bang_loi.md`.
- Hoàn thiện toàn bộ hồ sơ `ho_so_launch_v0.md` 1 trang gồm 7 mục, gắn nhãn `Giả lập` chuẩn xác cho các mục tính từ `_simulated` (mục 1, 2, 3, 7). Đưa ra đề xuất **Go có điều kiện** bảo vệ tính kinh tế của dự án, chỉ ra rõ ràng các con số bất lợi (chi phí xem lại 100% lên tới 1,03× mức 12.000 đ [simulated], power giảm còn 64,17% nếu effect size chỉ đạt 5 điểm phần trăm) kèm 4 điều kiện xử lý chặt chẽ.
- Chuẩn bị khung phiếu chấm phản biện `phieu_cham.md` và tổng hợp nội dung cho `group_report.md`.

## 4. Bằng chứng

- File hồ sơ launch: [report/team/ho_so_launch_v0.md](ho_so_launch_v0.md) (đủ 7 mục, trạng thái, người phụ trách, đề xuất Go có điều kiện có căn cứ số liệu).
- File bảng lỗi: [report/team/bang_loi.md](bang_loi.md) (hai bộ nhãn độc lập, tỉ lệ đồng thuận 100%, 5 giải pháp khắc phục).
- File kế hoạch pilot: [report/team/pilot_plan.yaml](pilot_plan.yaml) (đã kiểm tra đọc bằng PyYAML, 3 luật dừng NẾU - TRONG - THÌ - KHÔNG THÌ, không còn `?`).
- File phiếu chấm: [report/team/phieu_cham.md](phieu_cham.md) và báo cáo nhóm [report/team/group_report.md](group_report.md).

## 5. Công cụ AI đã dùng

- Antigravity (Claude / Gemini): Hỗ trợ đối chiếu phân loại lỗi theo Google PAIR, trích xuất dữ liệu docx, kiểm tra định dạng YAML, rà soát logic tính toán độ nhạy và kiểm tra chéo các chỉ số telemetry.
- Cách tự kiểm tra:
  - Tự đọc và giải thích nguyên nhân gốc cho từng ca lỗi trong 20 ca, không nhìn trước đáp án.
  - Chạy `grep -v '^ *#' report/team/pilot_plan.yaml | grep -n '?'` và script python kiểm tra syntax YAML.
  - Chạy script kiểm tra từ khoá bị cấm theo Quy tắc 5 đề bài để đảm bảo Gate 2a chỉ duyệt kế hoạch pilot.
  - Đối chiếu số liệu chi phí, power và cỡ mẫu với code chạy của Minh và Phong.

## 6. Tự đánh giá

- Hoàn thành đầy đủ 100% nhiệm vụ được giao đúng hạn và đúng quy định của bài lab.
- Phối hợp nhịp nhàng với Người gắn nhãn 1 và các thành viên viết code để giữ hồ sơ launch luôn cập nhật theo thời gian thực.
