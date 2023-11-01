from datetime import datetime


class Invoice:
    __SERIES = 'MG'
    __invoice_number = None
    __product_name = None
    __quantity = None
    __price_p_unit = None
    __total = None

    def __init__(self, invoice_number, product_name, quantity, price_p_unit):
        self.__invoice_number = invoice_number
        self.__product_name = product_name
        self.__quantity = quantity
        self.__price_p_unit = price_p_unit

    def quantity_change(self, quantity):
        self.__quantity = quantity

    def price_change(self, price_p_unit):
        self.__price_p_unit = price_p_unit

    def product_name_change(self, product_name):
        self.__product_name = product_name

    def __format_table(self):
        ls = [self.__product_name, self.__quantity, self.__quantity, self.__total]
        formatted_text = ''
        for element in ls:
            if len(str(element)) <= 16:
                prefix = (16 - len(str(element))) // 2
                suffix = 16 - (prefix + len(str(element)))
                formatted_text += (suffix * ' ') + str(element) + (prefix * ' ') + '|'
        print(formatted_text)

    def invoice_generate(self):
        self.__total = self.__price_p_unit * self.__quantity
        print(f'Invoice series: {self.__SERIES} number: {self.__invoice_number}\n'
              f'Date: {datetime.now().date()}\n'
              f'     Product    |    Quantity    |  Price/Unit $  |    Total $     |\n'
              f'____________________________________________________________________')
        self.__format_table()


