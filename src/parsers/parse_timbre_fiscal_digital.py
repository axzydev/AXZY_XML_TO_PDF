from models.comprobante import TimbreFiscalDigital


def parse_timbre_fiscal_digital(timbre_fiscal_digital_element, namespaces):
    timbre_fiscal_digital = TimbreFiscalDigital()
    timbre_fiscal_digital.version = timbre_fiscal_digital_element.attrib.get('Version', '')
    timbre_fiscal_digital.uuid = timbre_fiscal_digital_element.attrib.get('UUID', '')
    timbre_fiscal_digital.fecha_timbrado = timbre_fiscal_digital_element.attrib.get('FechaTimbrado', '')
    timbre_fiscal_digital.rfc_prov_certif = timbre_fiscal_digital_element.attrib.get('RfcProvCertif', '')
    timbre_fiscal_digital.leyenda = timbre_fiscal_digital_element.attrib.get('Leyenda', '')
    timbre_fiscal_digital.sello_cfd = timbre_fiscal_digital_element.attrib.get('SelloCFD', '')
    timbre_fiscal_digital.no_certificado_sat = timbre_fiscal_digital_element.attrib.get('NoCertificadoSAT', '')
    timbre_fiscal_digital.sello_sat = timbre_fiscal_digital_element.attrib.get('SelloSAT', '')
    return timbre_fiscal_digital