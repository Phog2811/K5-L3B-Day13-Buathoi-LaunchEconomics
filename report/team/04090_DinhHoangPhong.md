# Báo cáo cá nhân — Đinh Hoàng Phong — 04090

## 1. Thông tin thành viên

- Họ tên: Đinh Hoàng Phong
- MSSV: 04090
- Email:
- GitHub: Phog2811
- Vai trong nhóm: nhóm trưởng; người viết code 1 (CP1–CP2); phụ trách `chi_so.md` (CP5) và `TEAM.md`.

## 2. Phần việc phụ trách

- Tạo và quản lý repo nhóm, mời thành viên, chia việc trong [TASKS.md](../../TASKS.md), điền [TEAM.md](../../TEAM.md).
- Nhiệm vụ A, B trong `src/lab13.py`: ba hàm A1, `mo_hinh` (A2), tách theo loại (A3), chi phí cố định (A4), độ nhạy B1–B4.
- Nhiệm vụ E: [chi_so.md](chi_so.md), gồm E1, danh sách event, kiểm tra chéo và E2.
- Bàn giao `lab13.py` cho Minh sau giải lao (đổi người viết code theo yêu cầu của đề).

## 3. Đóng góp cụ thể

- A1: ba hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`; ba phép thử in ĐẠT (1,20 · 1,25 · 1,25).
- A2: `mo_hinh` cộng token và tool của **mọi** lần chạy, kể cả lần lỗi, rồi chia cho 978 việc thành công → 4.472 đ/việc [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ). Làm lại chiếm 51,8%, xem lại 40,7% tổng chi phí [simulated].
- A3: in thêm tỉ lệ `ok` theo từng lần thử. `quoc_te` 30,0% → 11,4% → 2,2%, nên chạy lại không giúp; `quoc_te` 1,88× của 12.000 đ [simulated].
- A4: phạm vi `noi_dia` + `hang_nang`, cộng cố định 40 triệu/tháng → 4.599 đ (0,38×) ở 45.000 yêu cầu/tháng, 5.784 đ (0,48×) nếu còn một nửa [simulated].
- B1–B4: 9 kịch bản độ nhạy; cặp token ×2 + xem lại ×2 = +46,3%; giới hạn 2 lần rẻ nhất cho cả hệ thống (6.901.220 đ) dù chi phí mỗi việc thấp nhất là 1 lần; xem lại 100% → 0,98× (9 phút làm lại) hoặc 1,03× (15,3 phút theo dữ liệu), hoà vốn khi mỗi lần xem lại ≤ 5,1 / 4,8 phút [simulated].
- `chi_so.md`: ba chỉ số E1 từ code của Minh (82,83% · 27,12% · 4,25%), hai chỉ số tự đề xuất, 10 event có `trace_id`, kiểm tra chéo chỉ số ↔ event, 4 dòng rủi ro kinh tế lấy số từ bảng độ nhạy.

## 4. Bằng chứng

- Commit `be79fee` (A1, A2), `782284e` (A3, A4, B1–B4), `59a3c7c` và commit điền E1 (`chi_so.md`), `9318018` (`TASKS.md`), `7d5626c`, `ba12f0b` (`TEAM.md`).
- Chạy trong `src/`: `python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT` và toàn bộ bảng A2, A3, A4, B1–B4.
- Mọi số A–B khớp bảng đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`; riêng B4 với 15,3 phút ra 12.415 đ (hướng dẫn 12.414 đ) vì dùng trung bình chưa làm tròn, trong sai số 2%. Minh kiểm tra độc lập tiền token bằng `csv` + `Decimal` (245.585,132 đ), khớp `mo_hinh`.

## 5. Công cụ AI đã dùng

- Claude (Claude Code): đọc đề và đề xuất chia việc, viết code A1–B4 trong `lab13.py`, viết nháp `chi_so.md`, `TEAM.md` và báo cáo này, chạy lệnh git.
- Cách tự kiểm tra: chạy `lab13.py` và đối chiếu từng số với bảng trong hướng dẫn (lệch ≤ 2%); kiểm tra kịch bản "giảm một nửa" thay đổi đúng bằng nửa kịch bản "gấp đôi"; kiểm tra cặp B2 bằng tổng hai tác động riêng (5,6% + 40,7% ≈ 46,3%); Minh tính tay 5 dòng đầu CSV để đối chiếu.
- Tôi tự đọc lại code để giải thích được: vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm `thanh_cong`, và vì sao giới hạn rẻ nhất cho công ty khác giới hạn có chi phí mỗi việc thấp nhất.

## 6. Tự đánh giá
khá tốt
