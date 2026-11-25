# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 — ĐẠT |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 — ĐẠT |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 — ĐẠT |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv`, mọi lần chạy | đo từ trace |
| Tool | 84.000 | `logix_runs.csv`, 5.600 lần gọi | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1, đã nằm trong token + tool | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated`: 890 phút × 2.000 đ | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated`: 1.132 phút × 2.000 đ | simulated |
| Tổng chi phí | 4.373.585 | token + tool + xem lại + làm lại | simulated |
| Số việc thành công | 978 việc | `ket_qua == 'thanh_cong'` | đếm từ dữ liệu |
| Chi phí mỗi việc thành công | 4.472 | tổng chi phí / 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (token + tool) / 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? **16,3 lần [simulated]**; tử số gồm mọi lần chạy và giờ nhân viên, mẫu số chỉ đếm 978 việc thành công.
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? **Làm lại: 51,8% [simulated]**, xem lại: 40,7% [simulated]; tổng giờ nhân viên chiếm 92,5% [simulated].

So với nhân viên tự làm: chi phí cả hệ thống = (4.373.585,132 + 222 × 12.000) / 1.200 = **5.865 đ/yêu cầu = 0,49× [simulated]**, chưa cộng chi phí cố định.
Theo quy ước B3, 222 yêu cầu không thành công gồm 74 ca làm lại và 148 ca chuyển nhân viên; khoản 12.000 đ/ca được cộng ngoài giờ làm lại đã có trong mô hình.

### Đối chiếu bằng phép tính tay

Năm dòng đầu `logix_runs.csv`: tổng đầu vào = 4.759 + 2.953 + 4.171 + 3.311 + 3.536 = **18.730 token**; đầu ra = 492 + 409 + 619 + 409 + 290 = **2.219 token**.
Tiền token = 18.730 / 1.000 × 26 + 2.219 / 1.000 × 130 = **775,45 đ**; 21 lần gọi tool × 15 = **315 đ**; tổng **1.090,45 đ**.
Kiểm tra độc lập bằng `csv` + `Decimal` cho toàn bộ trace được **245.585,132 đ tiền token**, khớp `mo_hinh`; không dùng số làm tròn để tính tiếp.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công [simulated] | So với 12.000 đ [simulated] |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? **`quoc_te`**: 22.515 đ/việc [simulated], thành công 27,3%; tỉ lệ `ok` theo lần 1–2–3 chỉ 30,0%–11,4%–2,2%, lợi ích chạy lại rất thấp. Thu hẹp pilot về `noi_dia` + `hang_nang`; `doi_tac` chỉ thành công 54,4% và có điều khoản riêng.

Các tỉ số A3 chia cho 12.000 đ để đối chiếu theo đề; chưa gồm phần nhân viên làm thay và cố định nên chưa phải mức tiết kiệm của cả hệ thống.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định [simulated] | So với 12.000 đ [simulated] |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| Một nửa khối lượng (22.500 yêu cầu/tháng) | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Với 40 triệu đ/tháng, chi phí mỗi việc vẫn dưới 12.000 đ ở cả 45.000 và 22.500 yêu cầu/tháng: **4.599 và 5.784 đ [simulated]**; khối lượng giảm một nửa làm cố định/việc tăng gấp đôi.

Phạm vi có 900 việc thành công trên 1.200 yêu cầu toàn mẫu: 45.000 × 900 / 1.200 = 33.750 việc/tháng; chi phí biến đổi trong phạm vi là 3.414 đ/việc [simulated]. A4 chưa cộng phần nhân viên làm thay.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công [simulated] | Thay đổi (%) [simulated] |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien; đặt phút xem/làm lại của các ca đó về 0 | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ | −8,1% |

Mốc gốc: 4.472 đ/việc [simulated]. Cả ba cặp token, xem lại, làm lại đã qua kiểm tra bằng số chưa làm tròn: mức giảm khi ×0,5 bằng một nửa mức tăng khi ×2 (sai số < 10⁻⁸ đ).

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ/việc, +46,3% [simulated]**; tác động bằng tổng hai tác động riêng do mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất trong các kịch bản B1: **1. Làm lại (+51,8%) · 2. Xem lại (+40,7%) · 3. Lương nhân viên (+23,1%) [simulated]**; token chỉ +5,6% [simulated].

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý [simulated] | Số yêu cầu không thành công | Chi phí cả hệ thống [simulated] | Chi phí mỗi việc thành công [simulated] |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? **2 lần** rẻ nhất cho cả hệ thống: 6.901.220 đ [simulated]; **1 lần** có chi phí/việc thấp nhất: 4.111 đ [simulated] nhưng đẩy thêm 85 yêu cầu sang nhân viên so với 2 lần.

Chi phí cả hệ thống = tổng trợ lý + 12.000 đ × số yêu cầu không thành công; chưa gồm cố định.

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: **11.743 đ = 0,98× [simulated]** với 9 phút làm lại; **12.415 đ = 1,03× [simulated]** với thời gian trung bình 15,2973 phút [simulated] từ dữ liệu.
- Kết quả này nói gì về thứ pilot cần học được? Với 5 phút/lần xem lại, tiết kiệm gần hết hoặc chuyển sang lỗ; pilot cần đo thời gian xem lại thật và giảm tỉ lệ xem lại an toàn. Ngưỡng hoà vốn lần lượt **≤ 5,1 và ≤ 4,8 phút [simulated]** cho hai giả định làm lại.

Trong 982 yêu cầu thuộc phạm vi, 948 yêu cầu có ít nhất một lần `ok` cần xem lại; 48 ca làm lại; 900 việc thành công. Token + tool = 224.513 đ; xem lại = 948 × 5 × 2.000 = 9.480.000 đ [simulated].
Với 9 phút làm lại: tổng 10.568.513 đ [simulated]; dùng trung bình chưa làm tròn 1.132 / 74 phút [simulated]: tổng 11.173.054 đ [simulated]. Không lấy 15,3 đã làm tròn để tính tiếp; B4 chưa cộng cố định và phần nhân viên làm thay.
