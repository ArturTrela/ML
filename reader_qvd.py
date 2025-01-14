from pyqvd import QvdTable

tbl= QvdTable.from_qvd('./ILOSCAWARII_KWARTALNAPRODUKCJA.qvd')
print(tbl.head())

tbl2 = QvdTable.from_qvd('./ILOSCAWARII_SUMA.qvd')
print(tbl2)