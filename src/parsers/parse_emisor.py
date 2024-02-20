

from models.comprobante import Emisor

def parse_emisor(emisor_element, namespaces):
    emisor = Emisor()
    emisor.rfc = emisor_element.attrib.get('Rfc', '')
    emisor.nombre = emisor_element.attrib.get('Nombre', '')
    emisor.regimen_fiscal = emisor_element.attrib.get('RegimenFiscal', '')
    return emisor