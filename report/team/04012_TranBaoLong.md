# Báo cáo cá nhân — Trần Bảo Long — 04012

## 1. Thông tin thành viên

- Họ tên: Trần Bảo Long
- MSSV: 04012
- Email: tranbaolong5b@gmail.com
- GitHub: Blong1501
- Vai trong nhóm: Người gắn nhãn 1 (CP1–CP2 theo dõi điều kiện "Xong khi"; CP3–CP5 chủ file `bang_loi.md` và `pilot_plan.yaml`).

## 2. Phần việc phụ trách

- Cài đặt môi trường `.venv` trong `src/`, chạy kiểm chứng độc lập toàn bộ `src/lab13.py` trên máy cá nhân (máy thứ hai khác máy Phong) và theo dõi điều kiện "Xong khi" qua các checkpoint.
- Nhiệm vụ C (CP3): Gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR (người gắn nhãn 1), đối soát đồng thuận với Nguyễn Ngọc Bách, viết quy tắc phân biệt các ca dễ lẫn và hoàn thiện bảng khắc phục 5 ca trong [bang_loi.md](bang_loi.md).
- Nhiệm vụ D (CP4): Hoàn thiện toàn bộ kế hoạch pilot trong [pilot_plan.yaml](pilot_plan.yaml) (5 câu cỡ mẫu D1, 5 câu tách tác động D2, đánh đổi MDE 6 điểm, ngưỡng an toàn theo tỉ lệ mở lại thực tế, 3 luật dừng đủ 4 vế NẾU – TRONG – THÌ – KHÔNG THÌ, cơ chế rollback và danh sách `simulated_inputs`).

## 3. Đóng góp cụ thể

- Chạy kiểm chứng toàn bộ `src/lab13.py` (gồm A1–B4 của Phong và D1–E1 của Minh) trên máy cá nhân: đạt cả 3 phép thử A1 (`1,20 · 1,25 · 1,25`), `Tự kiểm tra D1–E1: ĐẠT` và toàn bộ bảng số liệu khớp sai số <= 2%.
- Nhiệm vụ C (`bang_loi.md`): Gắn nhãn độc lập 20 ca lỗi theo nguyên nhân gốc, đạt đồng thuận **20/20 (100%)** với Nguyễn Ngọc Bách (4 Do người dùng · 5 Hệ thống · 4 Ngữ cảnh · 4 Giới hạn hệ thống · 3 Ngầm); hoàn thiện bảng khắc phục 5 ca (Ca 9, 7, 18, 4, 17) với cách phát hiện đo được đồng bộ đúng tên event trong [chi_so.md](chi_so.md) (`refund_ledger_write`, `ticket_closed`, `ticket_reopened`, `handoff_to_staff`, `audit_sample_checked`) và một vai trò phụ trách cụ thể mỗi dòng.
- Nhiệm vụ D (`pilot_plan.yaml`): Hoàn thiện đầy đủ phần chú thích D1 (`1.251`, `DE = 2,48` / `3.103` / `42` người, trần 20 người `1.000`, trần 6 depot `300`, MDE 6 điểm `n = 859`, `m >= 299`, `DE = 6,96`, `5.980` yc thực/nhóm), 5 câu D2, công khai con số bất lợi (`power = 64,17%` nếu tác động thật chỉ 5 điểm), ngưỡng an toàn dựa trên tỉ lệ `mo_lai_trong_7_ngay` thực tế (`4,25%` toàn mẫu, `3,97%` trong phạm vi), và 3 luật dừng đủ 4 vế đồng bộ với [ho_so_launch_v0.md](ho_so_launch_v0.md) và [chi_so.md](chi_so.md).

## 4. Bằng chứng

- File bảng lỗi và cách khắc phục: [report/team/bang_loi.md](bang_loi.md)
- File kế hoạch pilot: [report/team/pilot_plan.yaml](pilot_plan.yaml)
- Kết quả chạy kiểm chứng `python lab13.py` trên máy thứ hai (`Ba phép thử đáp án biết trước: ĐẠT`, `Tự kiểm tra D1–E1: ĐẠT`) và kiểm tra `yaml.safe_load`, không còn dấu `?`, không có từ bị cấm trong toàn bộ file hồ sơ.

## 5. Công cụ AI đã dùng

- Công cụ: Gemini (trợ lý lập trình trên IDE).
- Dùng vào việc gì: Hỗ trợ khắc phục lỗi `PATH` khi tạo `.venv` trên Windows PowerShell, kiểm tra cú pháp YAML, đối chiếu công thức cỡ mẫu D1, rà soát đồng bộ tên event giữa `bang_loi.md`, `pilot_plan.yaml` và `chi_so.md`, xử lý xung đột git khi gộp bài nhóm.
- Cách tự kiểm tra:
  - Tự chạy `python lab13.py` trên `.venv` cục bộ để xác minh toàn bộ số A1–A4, B1–B4, D1 và E1 trực tiếp từ `src/logix_runs.csv` và `src/logix_requests.csv`.
  - Tự chạy script Python xác minh `yaml.safe_load(open('../report/team/pilot_plan.yaml', encoding='utf-8'))`, kiểm tra 0 dấu `?` ngoài dòng chú thích, 3 luật dừng đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ` và không có từ bị cấm theo Quy tắc 5.
  - Tự đối chiếu nguyên nhân gốc từng ca trong 20 ca lỗi với thành viên gắn nhãn 2 (Nguyễn Ngọc Bách) để giải thích được trước hội đồng Gate 2a.

## 6. Tự đánh giá

- Hoàn thành đầy đủ phần việc được phân công (`bang_loi.md`, `pilot_plan.yaml`, chạy kiểm chứng `lab13.py` trên máy thứ hai), giữ đồng bộ số liệu và tên event với toàn bộ hồ sơ nhóm.
- Nắm rõ các điểm trọng tâm để bảo vệ Gate 2a: vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm `thanh_cong`, trần cỡ mẫu hiệu dụng `c / ICC` khi chia theo cụm và đánh đổi MDE 6 điểm (power 64,17% ở 5 điểm), và lý do chọn ngưỡng dừng an toàn tương đối so với nhóm đối chứng.
