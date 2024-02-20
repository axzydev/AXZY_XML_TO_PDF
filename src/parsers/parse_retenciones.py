from models.comprobante import Retencion

def parse_retenciones(retenciones_element, namespaces):
    retenciones = []
    retencion_elements = retenciones_element.findall('.//cfdi:Retencion', namespaces)
    for retencion_element in retencion_elements:
        retencion = Retencion()
        retencion.base = retencion_element.attrib.get('Base', '')
        retencion.impuesto = retencion_element.attrib.get('Impuesto', '')
        retencion.tipo_factor = retencion_element.attrib.get('TipoFactor', '')
        retencion.tasa_o_cuota = retencion_element.attrib.get('TasaOCuota', '')
        retencion.importe = retencion_element.attrib.get('Importe', '')
        retenciones.append(retencion)
    return retenciones