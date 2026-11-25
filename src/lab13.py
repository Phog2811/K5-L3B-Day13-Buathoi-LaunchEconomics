"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    # Lần chạy thứ i xảy ra khi i-1 lần trước đều sai: tổng (1-p)^(i-1), i=1..k = (1-(1-p)^k)/p
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        # Bỏ các lần chạy vượt giới hạn; yêu cầu cần nhiều lần hơn coi như chuyển nhân viên
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    # Tử số: MỌI lần chạy, kể cả lần lỗi
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    # Mẫu số: chỉ yêu cầu thành công
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm để so hai tỉ lệ độc lập, kiểm định hai phía."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    goc = ket_qua['cps']
    print(f"Chi phí mỗi việc thành công / hoá đơn mỗi yêu cầu: {goc / ket_qua['hoa_don_moi_yc']:.1f} lần")
    for khoan in ['token', 'tool', 'xem_lai', 'lam_lai']:
        print(f"  Tỉ trọng {khoan:8s} {ket_qua[khoan] / ket_qua['tong']:6.1%}")
    khong_tc = len(reqs) - ket_qua['thanh_cong']
    he_thong_moi_yc = (ket_qua['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f'Chi phí cả hệ thống mỗi yêu cầu (cộng {khong_tc} ca nhân viên làm thay): '
          f'{he_thong_moi_yc:,.0f} đ = {he_thong_moi_yc / BASELINE:.2f}x của 12.000 đ [simulated]')

    # ---------- Nhiệm vụ A3 · Tách theo loại yêu cầu ----------
    print('\nA3 · Theo loại yêu cầu [cps: simulated]')
    print(f"{'loai':10s} {'so_yc':>6s} {'ti_le_tc':>9s} {'chay/yc':>8s} {'cps':>8s} {'so_12k':>7s}")
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs['loai'] == loai]
        m = mo_hinh(runs, r)
        so_chay = runs['request_id'].isin(r['request_id']).sum()
        print(f"{loai:10s} {len(r):6d} {m['thanh_cong'] / len(r):9.1%} {so_chay / len(r):8.2f} "
              f"{m['cps']:8,.0f} {m['cps'] / BASELINE:6.2f}x")
    # Chạy lại có giúp không: tỉ lệ ok theo từng lần thử
    ok_theo_lan = (runs.assign(ok=runs['status'] == 'ok')
                   .merge(reqs[['request_id', 'loai']])
                   .pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean'))
    print('Tỉ lệ ok theo lần thử:')
    print((ok_theo_lan * 100).round(1).to_string())

    # ---------- Nhiệm vụ A4 · Chi phí cố định, phạm vi noi_dia + hang_nang ----------
    CO_DINH_THANG, YC_THANG = 40_000_000, 45_000
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    m_pv = mo_hinh(runs, pham_vi)
    print(f"\nA4 · Phạm vi noi_dia + hang_nang: {m_pv['thanh_cong']} việc thành công / {len(reqs)} yêu cầu mẫu, "
          f"cps {m_pv['cps']:,.0f} đ [simulated]")
    for ten, khoi_luong in [('45.000 yc/tháng', YC_THANG), ('Một nửa khối lượng', YC_THANG / 2)]:
        tc_thang = khoi_luong * m_pv['thanh_cong'] / len(reqs)
        co_dinh = CO_DINH_THANG / tc_thang
        tong_viec = m_pv['cps'] + co_dinh
        print(f'  {ten:20s} {tc_thang:8,.0f} việc/tháng · cố định {co_dinh:6,.0f} đ/việc · '
              f'cps + cố định {tong_viec:6,.0f} đ = {tong_viec / BASELINE:.2f}x [simulated]')

    # ---------- Nhiệm vụ B1 · Đổi từng yếu tố ----------
    kich_ban = {
        'Giá token gấp đôi':        dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':   dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':          dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa':     dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':          dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa':     dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':           dict(luong_phut=2500),
        'Tối đa 2 lần chạy':        dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':           dict(max_lan_chay=1),
    }
    print(f'\nB1 · Độ nhạy [simulated] · gốc {goc:,.0f} đ')
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'  {ten:25s} {cps:8,.0f} {(cps / goc - 1) * 100:+6.1f}%')

    # ---------- Nhiệm vụ B2 · Đổi một cặp ----------
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'B2 · Token gấp đôi + xem lại gấp đôi: {cps_cap:,.0f} đ {(cps_cap / goc - 1) * 100:+.1f}% [simulated]')

    # ---------- Nhiệm vụ B3 · Giới hạn chạy lại và chi phí cả hệ thống ----------
    print('B3 · Giới hạn số lần chạy [simulated]')
    for gioi_han in [1, 2, 3]:
        m = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        khong_tc = len(reqs) - m['thanh_cong']
        print(f"  {gioi_han} lần: trợ lý {m['tong']:11,.0f} đ · không thành công {khong_tc:4d} · "
              f"cả hệ thống {m['tong'] + khong_tc * BASELINE:11,.0f} đ · cps {m['cps']:6,.0f} đ")

    # ---------- Nhiệm vụ B4 · Xem lại 100% trong phạm vi noi_dia + hang_nang ----------
    PHUT_XEM, PHUT_LAM_DE = 5, 9
    co_ok = runs.loc[runs['status'] == 'ok', 'request_id']
    so_xem = pham_vi['request_id'].isin(co_ok).sum()   # yêu cầu có ít nhất một lần chạy ok
    so_lam_lai = (pham_vi['ket_qua'] == 'lam_lai').sum()
    token_tool = m_pv['token'] + m_pv['tool']
    phut_lam_dl = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    print(f'B4 · Xem lại 100%: {so_xem} yêu cầu xem lại, {so_lam_lai} ca làm lại, token + tool {token_tool:,.0f} đ')
    for nhan, phut_lam in [(f'{PHUT_LAM_DE} phút làm lại (đề)', PHUT_LAM_DE),
                           (f'{phut_lam_dl:.1f} phút làm lại (dữ liệu)', phut_lam_dl)]:
        tien_xem = so_xem * PHUT_XEM * LUONG_PHUT
        tien_lam = so_lam_lai * phut_lam * LUONG_PHUT
        cps = (tien_xem + tien_lam + token_tool) / m_pv['thanh_cong']
        hoa_von = (BASELINE * m_pv['thanh_cong'] - tien_lam - token_tool) / (so_xem * LUONG_PHUT)
        print(f'  {nhan:26s} tổng {tien_xem + tien_lam + token_tool:12,.0f} đ · cps {cps:6,.0f} đ = '
              f'{cps / BASELINE:.2f}x · hoà vốn khi xem lại ≤ {hoa_von:.1f} phút [simulated]')

    # ---------- Nhiệm vụ D1 · Cỡ mẫu và đánh đổi khi chia cụm ----------
    from statsmodels.stats.proportion import proportion_effectsize
    from statsmodels.stats.power import NormalIndPower

    ICC, M, C = 0.02, 75, 20
    n_5 = co_mau(0.70, 0.75)
    de_75 = 1 + (M - 1) * ICC
    n_cum = math.ceil(n_5 * de_75)
    so_nguoi = math.ceil(n_cum / M)
    n_6 = co_mau(0.70, 0.76)
    m_6 = math.ceil(n_6 * (1 - ICC) / (C - n_6 * ICC))
    de_6 = 1 + (m_6 - 1) * ICC
    n_hieu_dung = C * m_6 / de_6
    power_5 = NormalIndPower().power(
        effect_size=abs(proportion_effectsize(0.70, 0.75)),
        nobs1=n_6, alpha=0.05, ratio=1, alternative='two-sided')

    assert (n_5, n_6) == (1251, 859), 'Đối chiếu công thức hai tỉ lệ của đề'
    assert C * (m_6 - 1) / (1 + (m_6 - 2) * ICC) < n_6 <= n_hieu_dung
    print('\nD1 · Cỡ mẫu mỗi nhóm (baseline 70%, alpha 0,05, power 80%, ICC 0,02)')
    print(f'  a) Theo yêu cầu, +5 điểm phần trăm: {n_5:,} yêu cầu/nhóm.')
    print(f'  b) Theo nhân viên, m={M}: DE={de_75:.2f}; {n_cum:,} yêu cầu/nhóm; '
          f'{so_nguoi} người/nhóm, tổng {2 * so_nguoi} > 40: không đủ người.')
    print(f'  c) {C} nhân viên/nhóm: n hiệu dụng < {C / ICC:,.0f} < {n_5:,}; '
          f'với m={M} chỉ đạt {C * M / de_75:.2f}; tăng thời gian vẫn không đủ cho +5 điểm.')
    print(f'  d) 6 depot/nhóm: n hiệu dụng < {6 / ICC:,.0f} < {n_5:,}; '
          'chỉ 6 cụm/nhóm, dưới mức 20 cụm.')
    print(f'  e) +6 điểm phần trăm: {n_6} yêu cầu hiệu dụng/nhóm; {C} người/nhóm cần '
          f'm >= {m_6}; DE={de_6:.2f}; n hiệu dụng={n_hieu_dung:.2f}; '
          f'{C * m_6:,} yêu cầu thực/nhóm, tổng {2 * C * m_6:,}.')
    print(f'  Đánh đổi: nếu tác động thật chỉ +5 điểm, power tại n={n_6} là {power_5:.2%}, '
          'thấp hơn mục tiêu 80%; không phát hiện khác biệt chưa chứng minh không có tác động.')

    # ---------- Nhiệm vụ E1 · Chỉ số quan sát và tỉ lệ mở lại cho D ----------
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    chinh = ((reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)).sum()
    bo_qua = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo']).sum()
    mo_lai = (reqs['mo_lai_trong_7_ngay'] == 1).sum()
    mo_lai_pv = (pham_vi['mo_lai_trong_7_ngay'] == 1).sum()
    assert (chinh, bo_qua, len(xem), mo_lai, mo_lai_pv) == (994, 48, 177, 51, 39), \
        'Đối chiếu chỉ số trên bộ CSV cố định của lab'
    print('\nE1 · Chỉ số trong đợt chạy thử (dữ liệu giả lập; chưa có đối chứng)')
    print(f'  Chính: đóng trong 24 giờ và không mở lại trong 7 ngày '
          f'{chinh}/{len(reqs)} = {chinh / len(reqs):.2%}.')
    print(f'  Dùng: sửa hoặc bỏ gợi ý trong các yêu cầu được xem lại '
          f'{bo_qua}/{len(xem)} = {bo_qua / len(xem):.2%}.')
    print(f'  An toàn / D: mở lại trong 7 ngày, toàn mẫu '
          f'{mo_lai}/{len(reqs)} = {mo_lai / len(reqs):.2%}; '
          f'noi_dia + hang_nang {mo_lai_pv}/{len(pham_vi)} = {mo_lai_pv / len(pham_vi):.2%}.')
    print('Tự kiểm tra D1–E1: ĐẠT')
