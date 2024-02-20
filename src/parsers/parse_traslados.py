from models.comprobante import Traslado


def parse_traslados(traslados_element, namespaces):
    traslados = []
    traslado_elements = traslados_element.findall('.//cfdi:Traslado', namespaces)
    for traslado_element in traslado_elements:
        traslado = Traslado()
        traslado.base = traslado_element.attrib.get('Base', '')
        traslado.impuesto = traslado_element.attrib.get('Impuesto', '')
        traslado.tipo_factor = traslado_element.attrib.get('TipoFactor', '')
        traslado.tasa_o_cuota = traslado_element.attrib.get('TasaOCuota', '')
        traslado.importe = traslado_element.attrib.get('Importe', '')
        traslados.append(traslado)
    return traslados
