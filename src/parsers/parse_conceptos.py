from models.comprobante import Concepto, CuentaPredial, ImpuestosDentroConcepto
from parsers.parse_cuenta_predial import parse_cuenta_predial
from parsers.parse_impuestos_dentro_concepto import parse_impuestos_dentro_concepto


def parse_conceptos(conceptos_element, namespaces):
    conceptos = []
    concepto_elements = conceptos_element.findall('.//cfdi:Concepto', namespaces)
    for concepto_element in concepto_elements:
        concepto = Concepto()
        concepto.clave_prod_serv = concepto_element.attrib.get('ClaveProdServ', '')
        concepto.objeto_imp = concepto_element.attrib.get('ObjetoImp', '')
        concepto.cantidad = concepto_element.attrib.get('Cantidad', '')
        concepto.clave_unidad = concepto_element.attrib.get('ClaveUnidad', '')
        concepto.unidad = concepto_element.attrib.get('Unidad', '')
        concepto.descripcion = concepto_element.attrib.get('Descripcion', '')
        concepto.valor_unitario = concepto_element.attrib.get('ValorUnitario', '')
        concepto.importe = concepto_element.attrib.get('Importe', '')

        cuenta_predial_element = concepto_element.find('.//cfdi:CuentaPredial', namespaces)
        if cuenta_predial_element is not None:
            concepto.cuenta_predial = parse_cuenta_predial(cuenta_predial_element, namespaces)
        else:
            concepto.cuenta_predial = CuentaPredial()

        impuestos_element = concepto_element.find('.//cfdi:Impuestos', namespaces)
        if impuestos_element is not None:
            concepto.impuestos = parse_impuestos_dentro_concepto(impuestos_element, namespaces)
        else:
            concepto.impuestos = ImpuestosDentroConcepto()

        conceptos.append(concepto)
    return conceptos
