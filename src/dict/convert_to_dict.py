from models.comprobante import Comprobante, Emisor, Receptor,Concepto, ImpuestosDentroConcepto, CuentaPredial, ImpuestosFueraConcepto, Retencion, Traslado, TimbreFiscalDigital

def convert_to_dict(instance):
    instance_dict = {}
    for key, value in instance.__dict__.items():
        if value is not None:
            if isinstance(value, list):
                instance_dict[key] = [convert_to_dict(item) for item in value]
            elif isinstance(value, (Comprobante, 
                                    Emisor, 
                                    Receptor, 
                                    Concepto, 
                                    ImpuestosDentroConcepto,
                                    CuentaPredial,
                                    Retencion,
                                    ImpuestosFueraConcepto, 
                                    Traslado, 
                                    TimbreFiscalDigital)):
                instance_dict[key] = convert_to_dict(value)
            else:
                instance_dict[key] = value
    return instance_dict
