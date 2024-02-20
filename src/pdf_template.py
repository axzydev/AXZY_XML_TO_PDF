from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import json
from qr.qr_generator import generate_qr_code_base64
import logging

def generate_pdf_from_template(data_json):
    logging.basicConfig(filename='./logs/pdf/pdf_template.log', level=logging.INFO, format='%(asctime)s - %(message)s')
    try:
        logging.info("Generating PDF from template...")
        
        logging.info(f"Data JSON: {data_json}")
        
        json_data = json.loads(data_json)
        
        env = Environment(loader=FileSystemLoader('templates'))
        
        template = env.get_template("pdf_template.html")
        
        logging.info(f"Template: {template}")
        
        required_keys = ['sello', 'timbre_fiscal_digital']
        
        logging.info(f"Required keys: {required_keys}")
        
        for key in required_keys:
            if key not in json_data:
                raise KeyError(f"Key '{key}' not found in JSON data.")
        
        logging.info("All required keys found in JSON data.")
        
        qr_data = json_data['sello']
        
        qr_file_name = json_data['timbre_fiscal_digital']['uuid']
        
        logging.info(f"QR data: {qr_data}")
        
        logging.info(f"QR file name: {qr_file_name}")
        
        base_64 = generate_qr_code_base64(qr_data, qr_file_name)
        
        logging.info(f"QR code base64: {base_64}")
        
        context = {"comprobante": json_data, "base64_qr": base_64}
        
        html_content = template.render(context)
        
        #save html content to file
        #html_file = open(f"./pdf/{json_data['timbre_fiscal_digital']['uuid']}.html", "w")
        #html_file.write(html_content)
        
        logging.info(f"HTML content: {html_content}")
        
        pdf_path = f"./pdf/{json_data['timbre_fiscal_digital']['uuid']}.pdf"
        
        logging.info(f"PDF path: {pdf_path}")
        
        #generar el pdf como A4 y en vertical
        HTML(string=html_content).write_pdf(pdf_path, optimize_images=True, presentational_hints=True, zoom=0.5, resolution=300)
        
        print(f"PDF file generated: {pdf_path}")
        
        return True
    
    except json.JSONDecodeError as json_error:
        print(f"JSON decoding error: {json_error}")
        return False
    except KeyError as key_error:
        print(f"Key error: {key_error}")
        return False
    except Exception as e:
        print(f"Error generating PDF: {e}")
        return False