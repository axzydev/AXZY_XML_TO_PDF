from models.comprobante import Receptor


def parse_receptor(receptor_element, namespaces):
    receptor = Receptor()
    receptor.rfc = receptor_element.attrib.get('Rfc', '')
    receptor.nombre = receptor_element.attrib.get('Nombre', '')
    receptor.domicilio_fiscal_receptor = receptor_element.attrib.get('DomicilioFiscalReceptor', '')
    receptor.regimen_fiscal_receptor = receptor_element.attrib.get('RegimenFiscalReceptor', '')
    receptor.uso_cfdi = receptor_element.attrib.get('UsoCFDI', '')
    return receptor
