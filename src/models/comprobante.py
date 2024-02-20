class Comprobante:
    def __init__(self):
        self.version = ''
        self.serie = ''
        self.folio = ''
        self.fecha = ''
        self.sello = ''
        self.forma_pago = ''
        self.no_certificado = ''
        self.certificado = ''
        self.subtotal = ''
        self.moneda = ''
        self.tipo_cambio = ''
        self.total = ''
        self.tipo_de_comprobante = ''
        self.exportacion = ''
        self.metodo_pago = ''
        self.lugar_expedicion = ''
        self.emisor = None
        self.receptor = None
        self.conceptos = []
        self.impuestos = None
        self.timbre_fiscal_digital = None

class Emisor:
    def __init__(self):
        self.rfc = ''
        self.nombre = ''
        self.regimen_fiscal = ''

class Receptor:
    def __init__(self):
        self.rfc = ''
        self.nombre = ''
        self.domicilio_fiscal_receptor = ''
        self.regimen_fiscal_receptor = ''
        self.uso_cfdi = ''

class Concepto:
    def __init__(self):
        self.clave_prod_serv = ''
        self.objeto_imp = ''
        self.cantidad = ''
        self.clave_unidad = ''
        self.unidad = ''
        self.descripcion = ''
        self.valor_unitario = ''
        self.importe = ''
        self.cuenta_predial = None
        self.impuestos = None

class CuentaPredial:
    def __init__(self):
        self.numero = ''

class ImpuestosDentroConcepto:
    def __init__(self):
        self.traslados = []
        self.retenciones = []

class ImpuestosFueraConcepto:
    def __init__(self):
        self.traslados = []
        self.retenciones = []
        self.total_impuestos_trasladados = ''

class Retencion:
    def __init__(self):
        self.base = ''
        self.impuesto = ''
        self.tipo_factor = ''
        self.tasa_o_cuota = ''
        self.importe = ''

class Traslado:
    def __init__(self):
        self.base = ''
        self.impuesto = ''
        self.tipo_factor = ''
        self.tasa_o_cuota = ''
        self.importe = ''

class TimbreFiscalDigital:
    def __init__(self):
        self.version = ''
        self.uuid = ''
        self.fecha_timbrado = ''
        self.rfc_prov_certif = ''
        self.leyenda = ''
        self.sello_cfd = ''
        self.no_certificado_sat = ''
        self.sello_sat = ''
