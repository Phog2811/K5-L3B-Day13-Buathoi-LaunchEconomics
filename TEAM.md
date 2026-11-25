# Team

## Thông tin nhóm

- Tên nhóm: Buathoi
- Lớp: L3B
- Repo nhóm: `K5-L3B-Day13-Buathoi-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/Phog2811/K5-L3B-Day13-Buathoi-LaunchEconomics · nhánh `main` · commit chốt: (điền lúc nộp)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Đinh Hoàng Phong | 04090 |  | Phog2811 | Nhóm trưởng · Người viết code 1 (A, B trong `lab13.py`) · phụ trách `chi_so.md`, `TEAM.md` |
|   2 | Trần Đình Nhật Minh | 04083 |  | trandinhnhatminh1452 | Người kiểm số (`bang_chi_phi.md`) · Người viết code 2 sau giải lao (D1, E1 trong `lab13.py`) |
|   3 | Trần Bảo Long | 04012 |  | Blong1501 | Người gắn nhãn 1 · phụ trách `bang_loi.md`, `pilot_plan.yaml` |
|   4 | Nguyễn Ngọc Bách | 04108 |  | bachnguyen2001 | Người gắn nhãn 2, kiêm giữ hồ sơ · phụ trách `ho_so_launch_v0.md`, `phieu_cham.md`, `group_report.md` |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí. Chia việc chi tiết: [TASKS.md](TASKS.md).

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

## DinhHoangPhong-04090

### Phần việc phụ trách

- Nhiệm vụ A, B: viết `src/lab13.py` (A1, A2, A3, A4, B1–B4).
- Nhiệm vụ E: `report/team/chi_so.md` (E1, danh sách event, E2).
- Quản lý repo, điền `TEAM.md`, commit chốt.

### Đóng góp cụ thể

- Viết A1–A4, B1–B4 trong `src/lab13.py`: ba phép thử ĐẠT; chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn chia số yêu cầu.
- Viết `report/team/chi_so.md`: ba chỉ số E1, 10 event có `trace_id`, kiểm tra chéo, 4 dòng rủi ro kinh tế.
- Tạo repo, chia việc (`TASKS.md`), điền `TEAM.md`.

### Bằng chứng

- Commit `be79fee`, `782284e` (code A–B); `59a3c7c` và commit E1 (`chi_so.md`); `9318018`, `7d5626c`, `ba12f0b` (`TASKS.md`, `TEAM.md`).
- Báo cáo cá nhân: `report/team/04090_DinhHoangPhong.md`

## TranDinhNhatMinh-04083

### Phần việc phụ trách

- Nhiệm vụ A, B: kiểm số, điền `report/team/bang_chi_phi.md`.
- Nhiệm vụ D, E: viết `TODO CP4` trong `src/lab13.py` (D1, tỉ lệ mở lại, ba chỉ số E1).

### Đóng góp cụ thể

- Điền `report/team/bang_chi_phi.md` (A1–A4, B1–B4) từ output `lab13.py`, đủ nhãn `simulated`; tính tay 5 dòng đầu `logix_runs.csv` (1.090,45 đ) và kiểm tra độc lập tiền token bằng `csv` + `Decimal` (245.585,132 đ, khớp `mo_hinh`).
- Kiểm tra ba cặp độ nhạy: mức giảm khi ×0,5 bằng nửa mức tăng khi ×2.
- Viết hàm `co_mau` và phần D1–E1 trong `src/lab13.py`: cỡ mẫu 1.251 · 3.103 (42 người/nhóm) · trần 1.000 · trần 300 · m ≥ 299; power 64,17% nếu tác động thật chỉ +5 điểm; ba chỉ số E1 (82,83% · 27,12% · 4,25%) và tỉ lệ mở lại trong phạm vi 3,97%.
- Bàn giao số D1 cho Long, E1 cho Phong, số chi phí cho Bách.

### Bằng chứng

- Commit `966f78e` (`src/lab13.py`, `bang_chi_phi.md`).
- Báo cáo cá nhân: `report/team/04083_TranDinhNhatMinh.md`

## TranBaoLong-04012

### Phần việc phụ trách

- Nhiệm vụ C: gắn nhãn 1, điền `report/team/bang_loi.md`.
- Nhiệm vụ D: `report/team/pilot_plan.yaml`.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi (người gắn nhãn 1), đồng thuận 20/20 với Bách; điền `report/team/bang_loi.md` gồm hai bộ nhãn và bảng khắc phục 5 ca (ca 9, 7, 18, 4, 17), cách phát hiện dùng đúng tên event trong `chi_so.md`.
- Viết `report/team/pilot_plan.yaml`: chú thích D1, D2, đánh đổi MDE 6 điểm (power 64,17% ở mức 5 điểm), ngưỡng an toàn dựa trên tỉ lệ mở lại hiện tại (4,25% / 3,97%), 3 luật dừng đủ 4 vế.
- Chạy `src/lab13.py` trên máy thứ hai: ba phép thử A1 ĐẠT, `Tự kiểm tra D1–E1: ĐẠT`.

### Bằng chứng

- Commit `3d0e302` (`bang_loi.md`, `pilot_plan.yaml`).
- Báo cáo cá nhân: `report/team/04012_TranBaoLong.md`

## NguyenNgocBach-04108

### Phần việc phụ trách

- Nhiệm vụ C: gắn nhãn 2, đối soát nhãn độc lập.
- Nhiệm vụ E: `report/team/ho_so_launch_v0.md`; chuẩn bị duyệt chéo `report/team/phieu_cham.md`; `report/team/group_report.md`.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi theo PAIR, đạt đồng thuận 20/20 (100%), hoàn thiện bảng 5 ca khắc phục kèm event đo lường.
- Hoàn thiện hồ sơ launch v0 1 trang gồm 7 mục với đầy đủ nhãn Giả lập đúng quy định, đưa ra đề xuất Go có điều kiện có bằng chứng số liệu và 4 điều kiện xử lý.
- Soạn thảo báo cáo nhóm `group_report.md` và chuẩn bị phiếu chấm phản biện Gate 2a `phieu_cham.md`.

### Bằng chứng

- Commit `425f0e3` (`ho_so_launch_v0.md`, `group_report.md`, `bang_loi.md`).
- Báo cáo cá nhân: `report/team/04108_NguyenNgocBach.md`
