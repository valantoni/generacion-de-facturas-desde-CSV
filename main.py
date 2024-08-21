import pdfkit
import pandas as pd
from invoice import config_invoice


def create_invoice(html, invoice_number):
    # Ruta del archivo PDF de salida
    pdf_file = "invoices/invoice_" + str(invoice_number) + ".pdf"
    # Opciones de configuración de pdfkit, para permitir el acceso a archivos locales
    options = {
        'enable-local-file-access': None, 
    }
    # Generar el archivo PDF a partir del HTML
    pdfkit.from_string(html, pdf_file, options=options)


def main():
    # Leer el archivo CSV
    df = pd.read_csv('invoices.csv')
    data = df.to_dict('records')

     # Crear las facturas
    for factura in data:
        # Verificar si "items" es una cadena y convertirla a una lista
        if isinstance(factura["items"], str):
            factura["items"] = eval(factura["items"])
        elif pd.isna(factura["items"]):
            factura["items"] = []
        #crear htlm de los items
        html_items = ""
        for item in factura["items"]:
            html_items += f"""
            <tr class="item">
            <td>
                {item["name"]}
            </td>
            <td class="cantidad">
                {item["quantity"]}
            </td>
            <td>
                {item["price"]}
            </td>
            </tr>           
            """
        html = config_invoice(factura["logo_path"], factura["invoice_number"], factura["timestamp"], factura["expire_date"], factura["company_name"], 
                              factura["ceo_name"], factura["contact_email"], factura["customer_name"], factura["customer_address"], factura["customer_email"], 
                              factura["payment_method"], factura["paid_amount"], html_items, factura["total_amount"])
        
        create_invoice(html, factura["invoice_number"])

if __name__ == "__main__":
    main()