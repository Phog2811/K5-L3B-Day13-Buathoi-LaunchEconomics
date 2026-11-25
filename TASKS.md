# Chia việc nhóm · Lab 13 Launch Economics

Đọc trước: [README.md](README.md) → [CHECKPOINTS.md](CHECKPOINTS.md) → [RUBRIC.md](RUBRIC.md). Hướng dẫn từng bước và số để tự đối chiếu (lệch ≤ 2% là được nhận): [docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md](docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md).

## 1. Vai và người phụ trách

| Người | GitHub | Vai trước giải lao (CP1–CP2) | Vai sau giải lao (CP3–CP5) | File **chỉ mình người này sửa** |
| --- | --- | --- | --- | --- |
| Đinh Hoàng Phong | Phog2811 | **Người viết code 1** (A, B) | Viết `chi_so.md` (E1, event, E2), quản lý repo | `src/lab13.py` (tới 15:20), `report/team/chi_so.md`, `TEAM.md` |
| Trần Đình Nhật Minh | trandinhnhatminh1452 | **Người kiểm số** | **Người viết code 2** (D1, E1) | `report/team/bang_chi_phi.md`, `src/lab13.py` (từ 15:35) |
| Trần Bảo Long | Blong1501 | **Người gắn nhãn 1**, theo dõi "Xong khi" | Chủ file bảng lỗi + pilot plan | `report/team/bang_loi.md`, `report/team/pilot_plan.yaml` |
| Nguyễn Ngọc Bách | bachnguyen2001 | **Người gắn nhãn 2 kiêm giữ hồ sơ** | Giữ hồ sơ, trưởng duyệt chéo | `report/team/ho_so_launch_v0.md`, `report/team/phieu_cham.md`, `report/team/group_report.md` |

Ai cũng phải tự làm: file báo cáo cá nhân `report/team/MSSV_HoTen.md` (copy từ mẫu, **giữ nguyên file mẫu**) và tự nộp link repo trên LMS. Ai không nộp link thì không có điểm.

Đổi người viết code sau giải lao là yêu cầu của đề (ít nhất hai người tự tay tính được chi phí): Phong code A–B, Minh code D1–E1.

## 2. Việc từng người theo checkpoint

### CP1 · Nhiệm vụ A · 14:00 → 14:53

- [ ] **Cả nhóm (14:00, 10 phút):** cài môi trường theo [src/README.md](src/README.md), chạy `python lab13.py` thấy `NotImplementedError` là đúng.
- [ ] **Phong:** trong `src/lab13.py` viết 3 hàm A1 (`TODO CP1`) → chạy in `Ba phép thử đáp án biết trước: ĐẠT`. Viết `mo_hinh(...)` (A2), vòng lặp theo `loai` (A3), thêm tỉ lệ ok theo lần thử (pivot theo `loai` × `attempt`) để trả lời "chạy lại có giúp không". Tính A4 (cố định 40 triệu/tháng cho `noi_dia` + `hang_nang`). Push ngay khi A1 ĐẠT, push lần nữa khi xong A2–A4.
- [ ] **Minh:** tính tay **ít nhất một con số** (gợi ý: tiền token của 5 dòng đầu `logix_runs.csv`, hoặc tổng phút xem lại) để đối chiếu với code. Điền bảng A1, A2 (9 dòng, 2 dòng xem lại / làm lại ghi nhãn `simulated`), A3 (4 dòng), A4 và các câu trả lời vào `bang_chi_phi.md`. Mỗi câu ≤ 3 dòng, có số.
- [ ] **Long:** đọc kỹ đề, giữ checklist "Xong khi" của từng CP và nhắc nhóm. Đọc trước mục D của hướng dẫn, dựng khung `pilot_plan.yaml` (chưa điền số).
- [ ] **Bách:** điền `ho_so_launch_v0.md` **ngay từ đầu buổi**: mục 1 (chi phí mỗi việc thành công) và mục 3 (so với 12.000 đ — dùng chi phí cả hệ thống mỗi yêu cầu, đã cộng ca `chuyen_nhan_vien`) lấy từ số của Minh.

Xong khi: `python lab13.py` in ĐẠT + bảng A2; `bang_chi_phi.md` có A2 đủ 9 dòng, A3 đủ 4 dòng.

### CP2 · Nhiệm vụ B · 14:53 → 15:20

- [ ] **Phong:** ở `TODO CP2` viết 9 kịch bản B1, cặp B2 (token ×2 + xem lại ×2), B3 (giới hạn 1/2/3 lần, chi phí cả hệ thống = tổng trợ lý + 12.000 đ × số yêu cầu không thành công), B4 (xem lại 100% cho `noi_dia` + `hang_nang`, 5 phút/lần xem, 9 phút/ca làm lại; thêm trường hợp 15,3 phút theo dữ liệu). **Push trước 15:20** rồi bàn giao `lab13.py` cho Minh.
- [ ] **Minh:** điền B1 (9 dòng), B2 + xếp hạng 3 yếu tố, B3, B4 vào `bang_chi_phi.md`. Tự kiểm tra: kịch bản "giảm một nửa" thay đổi đúng bằng nửa "gấp đôi".
- [ ] **Bách:** cập nhật hồ sơ mục 2 (ba yếu tố nhạy nhất).
- [ ] **Long:** dùng số B để nháp 2 luật dừng chi phí cho pilot.

### CP3 · Nhiệm vụ C · 15:35 → 16:08

- [ ] **Long + Bách (8 phút đầu):** mở `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` mục "Hai mươi ca lỗi", **ngồi tách nhau, gắn nhãn độc lập cả 20 ca, không trao đổi**, ghi ra giấy hoặc file nháp riêng (không commit). **Không đọc mục "Nhãn tham khảo cho 20 ca" trong hướng dẫn trước khi gắn xong.** Gắn theo **nguyên nhân gốc**, không theo chỗ cần sửa.
- [ ] **Long:** nhận nhãn của Bách, điền cả hai cột vào `bang_loi.md`, tính tỉ lệ đồng thuận (cần ≥ 16/20; thấp hơn thì viết lại định nghĩa). Ghi một câu quy tắc cho mỗi ca không trùng. **Không sửa bộ nhãn độc lập sau khi đã so.** Cùng Bách chọn 5 ca (mỗi loại một ca) điền bảng khắc phục: cách phát hiện đo được (event, ngưỡng, tần suất) + một vai trò phụ trách, không ghi "cả đội".
- [ ] **Minh (trong 8 phút gắn nhãn):** nhận `lab13.py`, hoàn thiện nốt phần CP2 nếu còn thiếu, rồi bắt đầu `TODO CP4`.
- [ ] **Phong:** soát `bang_chi_phi.md` với output code (lệch ≤ 2%), bắt đầu nháp danh sách event cho `chi_so.md`.
- [ ] **Bách:** cập nhật hồ sơ mục 5 (bảng lỗi).

### CP4 · Nhiệm vụ D · 16:08 → 16:36

- [ ] **Minh:** ở `TODO CP4` trong `lab13.py` tính 5 câu D1 (a: theo yêu cầu; b: theo nhân viên m = 75; c: 20 nhân viên mỗi nhóm; d: 6 depot mỗi nhóm; e: mức chênh 6 điểm, 20 người mỗi nhóm), power khi tác động thật chỉ 5 điểm, tỉ lệ `mo_lai_trong_7_ngay` hiện tại (toàn mẫu và trong phạm vi `noi_dia` + `hang_nang`), và 3 chỉ số E1 (chính, dùng, an toàn). Push và gửi số cho Long + Phong.
- [ ] **Long:** điền toàn bộ `pilot_plan.yaml`: chú thích D1 (số của Minh), D2 (5 câu), đánh đổi đã chấp nhận, ngưỡng an toàn dựa trên tỉ lệ mở lại hiện tại; mọi trường kể cả `identifiability`, `interim_looks`, `simulated_inputs`; **≥ 3 luật dừng** (an toàn, chi phí, mức độ sử dụng) đủ 4 vế NẾU – TRONG – THÌ – KHÔNG THÌ.
- [ ] **Long tự kiểm tra** (trong `src/`):
  - `python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml'))"` không lỗi
  - `grep -v '^ *#' ../report/team/pilot_plan.yaml | grep -n '?'` không in gì
- [ ] **Bách:** cập nhật hồ sơ mục 6 (pilot plan).

### CP5 · Nhiệm vụ E + duyệt chéo · 16:36 → 18:00

- [ ] **Phong:** điền `chi_so.md`: E1 (3 chỉ số tính thử từ code của Minh + 1 chỉ số dùng + 1 chỉ số an toàn tự đề xuất), **≥ 6 event có `trace_id`**, kiểm tra chéo chỉ số ↔ event, E2 **≥ 2 dòng rủi ro** lấy số từ bảng độ nhạy.
- [ ] **Bách:** hoàn thiện `ho_so_launch_v0.md` đủ 7 mục (mỗi mục: con số chính, trạng thái `Xong, có bằng chứng` / `Chưa` / `Giả lập`, một vai trò phụ trách). Mục 1, 2, 3, 7 ghi Giả lập. Dòng cuối: **một** trong Go / Go có điều kiện / No-go, có nêu cả con số bất lợi và cách xử lý. **17:00 gửi hồ sơ cho nhóm hội đồng.**
- [ ] **Cả nhóm (17:00–17:45):** làm hội đồng chấm nhóm n + 1. **Bách** ghi `phieu_cham.md` (điểm, lý do có số, một câu hỏi, câu trả lời của đội trình). Cả nhóm chuẩn bị trả lời: vì sao tử số tính mọi lần chạy, cỡ mẫu hiệu dụng khi chia cụm, lý do đề xuất.
- [ ] **17:45 Bách:** điền `group_report.md` (con số chính, đề xuất, kết quả duyệt chéo nhận được).
- [ ] **17:45 mỗi người:** viết báo cáo cá nhân `report/team/<MSSV>_<HoTenKhongDau>.md` (vai, đóng góp, bằng chứng = commit/file, công cụ AI đã dùng và cách tự kiểm tra), push.
- [ ] **Phong (cuối cùng):** điền `TEAM.md` (thông tin nhóm, vai, đóng góp từng người — mọi người gửi nội dung cho Phong), chạy checklist mục 4, push commit chốt.

## 3. Quy tắc git để không conflict

1. Chỉ sửa file trong cột "chỉ mình người này sửa" ở mục 1. Muốn đổi file của người khác thì nhắn người đó sửa.
2. Trước khi bắt đầu và trước mỗi lần push: `git pull --rebase origin main`.
3. Commit nhỏ, thường xuyên, ghi rõ CP: `git add <file của mình>` → `git commit -m "CP1: A2 mo_hinh"` → `git push origin main`.
4. Không `git add .` (dễ dính `.venv/`, file nháp nhãn). Không force-push, không xoá commit (vi phạm [RULES.md](RULES.md)).
5. Phong cần mời 3 bạn làm collaborator của repo (Settings → Collaborators) để mọi người push được.

## 4. Checklist trước khi nộp (Phong chạy, cả nhóm soát)

- [ ] `cd src && python lab13.py` chạy hết trên **một máy khác** máy Phong; ba phép thử in ĐẠT (1,20 · 1,25 · 1,25).
- [ ] Đủ 6 file hồ sơ trong `report/team/`, đúng tên: `bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`, `phieu_cham.md`.
- [ ] Mọi số tính từ cột `_simulated` có nhãn `simulated`.
- [ ] `pilot_plan.yaml` đọc được bằng `yaml.safe_load`, không còn `?`, ≥ 3 luật dừng đủ 4 vế.
- [ ] Người phụ trách luôn là một vai trò, không có "cả đội".
- [ ] `grep -rni production report/team` không in gì (Gate 2a chỉ duyệt pilot).
- [ ] Không viết "trợ lý đã nâng chỉ số" — chỉ viết "chỉ số trong đợt chạy thử là …".
- [ ] 4 file báo cáo cá nhân + file mẫu `MSSV_HoTen.md` vẫn còn.
- [ ] `TEAM.md` đã điền; tên repo đúng mẫu `K5-L3B-DAY13-TenNhom-LaunchEconomics`, repo public hoặc đã mời giảng viên.
- [ ] **Cả 4 người** nộp link repo trên LMS trước **23h59 GMT+7** ngày lab.

## 5. Lưu ý liêm chính

- Số trong hồ sơ phải do `src/lab13.py` tính ra (hoặc tính tay có ghi cách tính). Số trong hướng dẫn chỉ để **đối chiếu**, không chép thẳng.
- Không sửa `src/logix_runs.csv`, `src/logix_requests.csv`, `src/lab13_starter.py`.
- Đọc CSV yêu cầu luôn có `keep_default_na=False`.
