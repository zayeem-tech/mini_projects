import qrcode

upi_id = input('Enter your UPI ID: ')

phonepe_url = f'upi://pay?pa={upi_id}&pa=Recipient%20Name'
paytm_url = f'upi://pay?pa={upi_id}&pa=Recipient%20Name'
google_pay_url = f'upi://pay?pa={upi_id}&pa=Recipient%20Name'

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

phonepe_qr.save('phonepe_qr.img')
paytm_qr.save('paytm_qr.img')
google_pay_qr.save('google_pay_qr.img')

phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()