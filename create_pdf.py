import os
from pyhtml2pdf import converter

path = os.path.abspath('codebook.html')
converter.convert(f'file:///{path}', 'codebook.pdf')