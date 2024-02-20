import xml.etree.ElementTree as ET

from models.comprobante import Comprobante, ImpuestosFueraConcepto
from parsers.parse_conceptos import parse_conceptos
from parsers.parse_emisor import parse_emisor
from parsers.parse_impuestos_fuera_concepto import parse_impuestos_fuera_concepto
from parsers.parse_receptor import parse_receptor
from parsers.parse_timbre_fiscal_digital import parse_timbre_fiscal_digital

NAMESPACES_V3 = {'cfdi': 'http://www.sat.gob.mx/cfd/3', 'tfd': 'http://www.sat.gob.mx/TimbreFiscalDigital'}
NAMESPACES_V4 = {'cfdi': 'http://www.sat.gob.mx/cfd/4', 'tfd': 'http://www.sat.gob.mx/TimbreFiscalDigital'}

def parse_xml_to_comprobante(xml_string):
    try:
        root = ET.fromstring(xml_string)
        
        if 'Version' in root.attrib and root.attrib['Version'] == '3.3':
            namespaces = NAMESPACES_V3
        elif 'Version' in root.attrib and root.attrib['Version'] == '4.0':
            namespaces = NAMESPACES_V4
        else:
            raise ValueError("Versión de espacio de nombres no compatible.")
        
        comprobante = Comprobante()
        comprobante.version = root.attrib.get('Version', '')
        comprobante.serie = root.attrib.get('Serie', '')
        comprobante.folio = root.attrib.get('Folio', '')
        comprobante.fecha = root.attrib.get('Fecha', '')
        comprobante.sello = root.attrib.get('Sello', '')
        comprobante.forma_pago = root.attrib.get('FormaPago', '')
        comprobante.no_certificado = root.attrib.get('NoCertificado', '')
        comprobante.certificado = root.attrib.get('Certificado', '')
        comprobante.subtotal = root.attrib.get('SubTotal', '')
        comprobante.moneda = root.attrib.get('Moneda', '')
        comprobante.tipo_cambio = root.attrib.get('TipoCambio', '')
        comprobante.total = root.attrib.get('Total', '')
        comprobante.tipo_de_comprobante = root.attrib.get('TipoDeComprobante', '')
        comprobante.exportacion = root.attrib.get('Exportacion', '')
        comprobante.metodo_pago = root.attrib.get('MetodoPago', '')
        comprobante.lugar_expedicion = root.attrib.get('LugarExpedicion', '')

        emisor_element = root.find('.//cfdi:Emisor', namespaces)
        if emisor_element is not None:
            comprobante.emisor = parse_emisor(emisor_element, namespaces)
        else:
            raise ValueError("Emisor element not found in XML.")

        receptor_element = root.find('.//cfdi:Receptor', namespaces)
        if receptor_element is not None:
            comprobante.receptor = parse_receptor(receptor_element, namespaces)
        else:
            raise ValueError("Receptor element not found in XML.")

        conceptos_element = root.find('.//cfdi:Conceptos', namespaces)
        if conceptos_element is not None:
            comprobante.conceptos = parse_conceptos(conceptos_element, namespaces)

        impuestos_element = root.find('.//cfdi:Impuestos[@TotalImpuestosTrasladados]', namespaces)
        if impuestos_element is not None:
            comprobante.impuestos = parse_impuestos_fuera_concepto(impuestos_element, namespaces)
        else:
            impuestos_element = ImpuestosFueraConcepto()
        timbre_fiscal_digital_element = root.find('.//tfd:TimbreFiscalDigital', namespaces)
        if timbre_fiscal_digital_element is not None:
            comprobante.timbre_fiscal_digital = parse_timbre_fiscal_digital(timbre_fiscal_digital_element, namespaces)
        else:
            raise ValueError("TimbreFiscalDigital element not found in XML.")

        return comprobante

    except ET.ParseError as pe:
        print(f"XML ParseError: {pe}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"Error parsing XML file: {e}")
    return None
  
