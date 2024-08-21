from style import css

def config_invoice(logo_path, invoice_number, timestamp, expire_date, company_name, ceo_name, contact_email, customer_name, customer_address, customer_email, payment_method, paid_amount, items, total_amount):

    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Factura</title>
        <style>
           {css}
        </style>
    </head>
    <body>
        <div class="invoice-box">
            <table>
                <tr class="top">
                    <td colspan="3">
                        <table>
                            <tr>
                                <td class="title">
                                    <img src={logo_path}  style="width: 100%; max-width: 150px;">
                                </td>
                                <td>
                                    Factura #: {invoice_number}<br>
                                    Creada: {timestamp}<br>
                                    Vencimiento: {expire_date}
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                
                <tr class="information">
                    <td colspan="3">
                        <table>
                            <tr>
                                <td>
                                    {company_name}<br>
                                    {ceo_name}<br>
                                    {contact_email}
                                </td>
                                <td>
                                    {customer_name}<br>
                                    {customer_address}<br>
                                    {customer_email}
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                
                <tr class="heading">
                    <td>
                        Método de Pago
                    </td>
                    <td>
                        {payment_method} #
                    </td>
                </tr>
                
                <tr class="details">
                    <td>
                        {payment_method}
                    </td>
                    <td>
                        {paid_amount}
                    </td>
                </tr>
                
                <tr class="heading">
                    <td>
                        Producto
                    </td>
                    <td class="cantidad">
                        Cantidad
                    </td>
                    <td>
                        Precio unitario
                    </td>
                </tr>
                
                {items}
                
                <tr class="total">
                    <td></td>
                    <td></td>
                    <td>
                    Total: {total_amount}
                    </td>
                </tr>
            </table>
        </div>
    </body>
    </html>
    
    """

    return html

