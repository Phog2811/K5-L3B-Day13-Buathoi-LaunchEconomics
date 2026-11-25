# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): Buathoi (Nhóm L3B)
- Nhóm được chấm: Nhóm kế tiếp (L3B-NhomTiepTheo)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất Go có điều kiện nêu đầy đủ con số bất lợi: chi phí xem lại 100% lên tới 1,03× [simulated] (12.415 đ > 12.000 đ) và power giảm xuống 64,17% nếu effect size chỉ đạt 5 điểm phần trăm. Có giải pháp điều kiện ràng buộc rõ ràng. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Có nhãn [simulated] ở mọi số liệu giả lập (chi phí 4.472 đ, độ nhạy xem/làm lại...); phạm vi thu hẹp về `noi_dia` (0,22×) và `hang_nang` (0,69×), loại bỏ `quoc_te` (1,88× với 22.515 đ/việc [simulated]). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Phân bổ ngẫu nhiên theo 20 nhân viên can thiệp vs 20 đối chứng (c = 20), $m \ge 299$, $n_{\text{hiệu dụng}} = 859$; có 3 luật dừng cụ thể đủ cú pháp NẾU - TRONG - THÌ - KHÔNG THÌ kèm người dừng và quy trình rollback 30 phút. |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Hồ sơ cung cấp bằng chứng định lượng chặt chẽ, thẳng thắn nhìn nhận các rủi ro kinh tế và giới hạn kích thước mẫu cụm; các điều kiện tiên quyết trước khi rollout giải quyết đúng điểm nghẽn kỹ thuật và an toàn tài chính. Tuy nhiên ở phần gắn nhãn PAIR cần lưu ý phân biệt giữa lỗi hệ thống và giới hạn hệ thống.

**Một câu hỏi cho đội trình:** Trong Bảng lỗi PAIR (Nhiệm vụ C), ở Ca 13 (khách hỏi hoàn phí bảo hiểm hàng hoá của đối tác, trợ lý trả lời chung chung về phí vận chuyển thay vì từ chối), tại sao nhóm lại gắn nhãn là "Hệ thống" thay vì "Giới hạn hệ thống"?

**Câu trả lời của đội trình (ghi lại tại buổi):** Đội trình giải thích rằng nhóm gắn nhãn "Hệ thống" vì nhìn vào hành vi sai của trợ lý: hệ thống không nhận diện được phạm vi ngoài thẩm quyền và đưa ra câu trả lời chung chung, không nói rõ mình không xử lý được (lỗi xử lý của mô hình). Tuy nhiên, sau khi hội đồng chất vấn, nhóm thừa nhận theo nguyên tắc gốc của Google PAIR thì nguyên nhân sâu xa là bảo hiểm đối tác nằm ngoài phạm vi năng lực và cơ sở dữ liệu của LogiX (out-of-scope), nên đáp án chuẩn xác phải là **Giới hạn hệ thống (System Limitations)**; việc bot phản hồi chung chung chỉ là hệ quả giao tiếp.
