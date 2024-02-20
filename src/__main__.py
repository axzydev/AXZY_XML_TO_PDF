import os
import json
from dict.convert_to_dict import convert_to_dict
from parsers.cfdi_parser import parse_xml_to_comprobante
from pdf_template import generate_pdf_from_template

def process_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".xml"):
            xml_path = os.path.join(folder_path, filename)
            try:
                with open(xml_path, "r", encoding="utf-8") as file:
                    xml_string = file.read()
                    comprobante = parse_xml_to_comprobante(xml_string)
                    if comprobante is not None:
                        comprobante_dict = convert_to_dict(comprobante)
                        json_result = json.dumps(comprobante_dict, indent=3, ensure_ascii=False)
                        generate_pdf_from_template(json_result)
                    else:
                        print(f"Error parsing XML file: {xml_path}. Comprobante is None.")
            except FileNotFoundError as file_not_found_error:
                print(f"File not found error for XML file: {xml_path}. {file_not_found_error}")
            except Exception as e:
                print(f"Error processing XML file: {xml_path}. {e}")
                continue

def main():
    folder_path = os.path.join(os.getcwd(), "xmls")
    print(f"Processing folder: {folder_path}")
    process_folder(folder_path)

if __name__ == "__main__":
    main()
