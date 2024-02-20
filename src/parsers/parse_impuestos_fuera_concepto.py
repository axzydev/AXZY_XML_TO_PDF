from models.comprobante import ImpuestosFueraConcepto
from parsers.parse_traslados import parse_traslados
from parsers.parse_retenciones import parse_retenciones


def parse_impuestos_fuera_concepto(impuestos_element, namespaces):
    impuestos = ImpuestosFueraConcepto()
    traslados_element = impuestos_element.find('.//cfdi:Traslados', namespaces)
    if traslados_element is not None:
        impuestos.traslados = parse_traslados(traslados_element, namespaces)
    
    retenciones_element = impuestos_element.find('.//cfdi:Retenciones', namespaces)
    if retenciones_element is not None:
        impuestos.retenciones = parse_retenciones(retenciones_element, namespaces)
    
    impuestos.total_impuestos_trasladados = impuestos_element.attrib.get('TotalImpuestosTrasladados', '')
    return impuestos
