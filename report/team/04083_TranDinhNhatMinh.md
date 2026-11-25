# Báo cáo cá nhân — Trần Đình Nhật Minh — 04083

## 1. Thông tin thành viên

- Họ tên: Trần Đình Nhật Minh.
- MSSV: 04083.
- Email: trandinhnhatminh1112@gmail.com
- GitHub: trandinhnhatminh1452.
- Vai trong nhóm: người kiểm số CP1–CP2; người viết code 2, phụ trách D1 và tính chỉ số E1 sau giải lao.

## 2. Phần việc phụ trách

- Kiểm số A–B từ hai CSV, đối chiếu ít nhất một phép tính tay và điền `bang_chi_phi.md`.
- Hoàn thiện phần D1 trong `src/lab13.py`: năm câu cỡ mẫu và power khi tác động thật chỉ tăng 5 điểm phần trăm.
- Tính ba chỉ số E1 và tỉ lệ mở lại trong toàn mẫu, trong phạm vi `noi_dia` + `hang_nang` để bàn giao cho Long và Phong.

## 3. Đóng góp cụ thể

- Hoàn thiện A1–A4, B1–B4 trong `bang_chi_phi.md` từ output code A–B đã có của Phong. Mọi chi phí phụ thuộc thời gian giả lập đều có nhãn `simulated`.
- Trình bày phép tính tay từ 5 dòng đầu CSV: 18.730 token đầu vào, 2.219 token đầu ra → 775,45 đ tiền token; thêm 315 đ tiền tool → 1.090,45 đ.
- Đối chiếu độc lập bằng `csv` + `Decimal`: tổng tiền token là 245.585,132 đ, khớp `mo_hinh`; tổng phút xem lại/làm lại là 890/1.132 [simulated].
- Kiểm tra ba cặp độ nhạy token, xem lại, làm lại: mức giảm khi ×0,5 bằng một nửa mức tăng khi ×2, sai số < 10⁻⁸ đ.
- Bổ sung `co_mau` theo công thức hai tỉ lệ của đề, phần in D1–E1 và các assert đối chiếu cỡ mẫu, số yêu cầu/người tối thiểu, chỉ số trên bộ CSV cố định.
- Ghi rõ đánh đổi: thiết kế 20 nhân viên/nhóm không đủ mẫu cho +5 điểm; khi chấp nhận +6 điểm cần 299 yêu cầu/người; power nếu tác động thật chỉ +5 điểm còn 64,17%.
- Giữ nguyên dữ liệu CSV, file starter và các file báo cáo do thành viên khác phụ trách.

## 4. Bằng chứng

- Code: [src/lab13.py](../../src/lab13.py), hàm `co_mau` và phần D1–E1.
- Bảng chi phí: [bang_chi_phi.md](bang_chi_phi.md), A1–A4, B1–B4 và phép đối chiếu tay.
- Chạy từ thư mục `src/` bằng Python trong `.venv` của repo:

```powershell
..\.venv\Scripts\python.exe -X utf8 lab13.py
```

Kết quả chạy kiểm tra bằng Codex: chương trình chạy hết, ba phép thử A1 in ĐẠT; kiểm tra D1–E1 đạt. Thư viện được cài theo `src/requirements.txt`; không gọi API model.

### Số bàn giao cho Long — D1 và ngưỡng an toàn

| Câu | Cách tính | Kết quả mỗi nhóm |
| --- | --- | --- |
| a · Theo yêu cầu, +5 điểm | Công thức hai tỉ lệ, 70% → 75%, alpha 0,05; power 80% | 1.251 yêu cầu |
| b · Theo nhân viên, m = 75 | DE = 1 + 74 × 0,02 = 2,48; làm tròn lên 1.251 × 2,48 | 3.103 yêu cầu; 42 người/nhóm, tổng 84 > 40 |
| c · 20 nhân viên | n hiệu dụng = 20m / (1 + (m − 1) × 0,02) | Với m = 75: 604,84; mọi m hữu hạn đều < 1.000, không đạt 1.251 |
| d · 6 depot | n hiệu dụng < 6 / 0,02 | < 300, không đủ 1.251; chỉ 6 cụm/nhóm |
| e · +6 điểm, 20 nhân viên | Cần 859 yêu cầu hiệu dụng; m ≥ 859 × 0,98 / (20 − 859 × 0,02) | m tối thiểu = 299; DE = 6,96; n hiệu dụng = 859,20 |

Câu e cần 5.980 yêu cầu thực/nhóm, tổng 11.960. Với n hiệu dụng = 859 và tác động thật +5 điểm, `NormalIndPower` cho power **64,17%**, thấp hơn mục tiêu 80%; không có khác biệt có ý nghĩa chưa chứng minh trợ lý không có tác động.

Tỉ lệ mở lại hiện tại: toàn mẫu **51/1.200 = 4,25%**; trong phạm vi **39/982 = 3,97%**. Đây là số quan sát trên dữ liệu giả lập, để Long lựa chọn luật dừng và ghi vào `pilot_plan.yaml`; chưa phải bằng chứng về tác động so với đối chứng.

### Số bàn giao cho Phong — E1

| Chỉ số | Tử số / mẫu số | Kết quả |
| --- | --- | --- |
| Chính: đóng trong 24 giờ và không mở lại trong 7 ngày | 994/1.200 | 82,83% |
| Dùng: sửa hoặc bỏ gợi ý trong các yêu cầu được xem lại | 48/177 | 27,12% |
| An toàn: mở lại trong 7 ngày | 51/1.200 | 4,25% |

Các chỉ số trên mô tả đợt chạy thử; chưa có nhóm đối chứng nên chưa kết luận trợ lý làm tăng chỉ số. Phong dùng bảng này để điền ba dòng E1 trong `chi_so.md`.

### Số bàn giao cho người giữ hồ sơ

- A2: 4.472 đ/việc thành công [simulated]; chi phí cả hệ thống mỗi yêu cầu là 5.865 đ = 0,49× mức 12.000 đ [simulated], chưa gồm cố định.
- A4: phạm vi `noi_dia` + `hang_nang`, đã cộng cố định, 4.599 đ/việc ở 45.000 yêu cầu/tháng; 5.784 đ khi khối lượng giảm một nửa [simulated]; chưa cộng phần nhân viên làm thay.
- B3: giới hạn 2 lần chạy rẻ nhất cho hệ thống: 6.901.220 đ [simulated].
- B4: xem lại 100%, 5 phút/lần, làm lại 9 phút → 11.743 đ/việc [simulated]; dùng thời gian làm lại trung bình chưa làm tròn 15,2973 phút [simulated] → 12.415 đ/việc [simulated], vượt 12.000 đ.

## 5. Công cụ AI đã dùng

- Codex hỗ trợ đọc đề và phân công, viết phần D1–E1, tính và điền báo cáo, chạy các lệnh kiểm chứng.
- Kiểm tra tự động đã thực hiện: chạy toàn bộ `lab13.py`, đối chiếu số với hướng dẫn sau khi tính từ CSV, kiểm tiền token bằng `csv` + `Decimal`, kiểm ba cặp độ nhạy và các assert D1–E1.
- Các phép kiểm tra trên do Codex chạy. 

## 6. Tự đánh giá

Đã có code và số liệu cho phần được giao; dữ liệu không thay đổi, giới hạn của phép so sánh chi phí và thiết kế chia cụm được ghi rõ. 

