from models.comprobante import CuentaPredial


def parse_cuenta_predial(cuenta_predial_element, namespaces):
    cuenta_predial = CuentaPredial()
    cuenta_predial.numero = cuenta_predial_element.attrib.get('Numero', '')
    return cuenta_predial