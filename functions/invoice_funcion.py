from classes import Invoice


def invoice():
    invoice_1 = Invoice(4, 'TV', 10, 600)
    invoice_1.invoice_generate()