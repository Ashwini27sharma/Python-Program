ctc = int(input('Enter the annual CTC: '))
hra = 0.10 * ctc
da = 0.05 * ctc
pf = 0.03 * ctc
if ctc <= 300000:
    tax = 0
elif ctc <= 700000:
    tax = 0.05 * (ctc - 300000)
elif ctc <= 1000000:
    tax = 20000 + (0.10 * (ctc - 700000))
elif ctc <= 1200000:
    tax = 50000 + (0.15 * (ctc - 1000000))
elif ctc <= 1500000:
    tax = 80000 + (0.20 * (ctc - 1200000))
else:
    tax = tax = 140000 + (0.30 * (ctc - 1500000))
total_deduction = hra + da + pf + tax
inhand_ctc = ctc - total_deduction
monthly = inhand_ctc / 12
print("Net Monthly In-Hand: ", monthly)