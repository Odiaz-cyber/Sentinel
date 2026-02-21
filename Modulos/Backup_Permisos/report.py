#/usr/bin/python3 
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle





class Report:
    def __init__(self, document , result_list):
        self.document = document
        self.result_list = result_list


    # PDF   
    def report(self):
        if self.document == "pdf":
            doc = SimpleDocTemplate("report.pdf" , pagesize=letter)

            # Crear tabla

            table = Table(self.result_list)
            
            
            table.setStyle(TableStyle([
                ("BACKGROUND", (0,0), (-1,0), colors.grey),
                ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
                ("ALIGN", (0,0), (-1,-1), "CENTER"),
                ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
                ("BOTTOMPADDING", (0,0), (-1,0), 12),
                ("GRID", (0,0), (-1,-1), 1, colors.black),
                ("TEXTCOLOR", (1,2), (1,2), colors.green),   # Secure en verde
                ("TEXTCOLOR", (1,1), (1,1), colors.red),     # Insecure en rojo
            ]))

            elements = [table]
            doc.build(elements)
        
        # HTML
        
        
        elif self.document == "html":
                
                html_content = """
                <!DOCTYPE html>
                <html lang="es">
                <head>
                    <meta charset="UTF-8">
                    <title>Reporte de Auditoría</title>
                    <style>
                        body {
                            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                            background-color: #f9f9f9;
                            margin: 0;
                            padding: 0;
                            color: #333;
                        }
                        header {
                            background: linear-gradient(135deg, #4CAF50, #2E7D32);
                            color: white;
                            padding: 20px;
                            text-align: center;
                            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                        }
                        h1 {
                            margin: 0;
                            font-size: 24px;
                        }
                        table {
                            width: 90%;
                            margin: 30px auto;
                            border-collapse: collapse;
                            background-color: white;
                            border-radius: 8px;
                            overflow: hidden;
                            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                        }
                        th, td {
                            padding: 12px 15px;
                            text-align: center;
                        }
                        th {
                            background-color: #f4f4f4;
                            font-weight: 600;
                            text-transform: uppercase;
                            letter-spacing: 0.05em;
                        }
                        tr:nth-child(even) {
                            background-color: #fafafa;
                        }
                        .secure {
                            color: #4CAF50;
                            font-weight: bold;
                        }
                        .insecure {
                            color: #F44336;
                            font-weight: bold;
                        }
                        .unknown {
                            color: #FF9800;
                            font-weight: bold;
                        }
                        footer {
                            text-align: center;
                            padding: 15px;
                            font-size: 12px;
                            color: #777;
                        }

                        img {
                            width: 70px;
                            heigth: 70px;
                        }
                    </style>
            </head>
            <body>
                <header>
                    <h1>Reporte de Auditoría de Permisos</h1>
                    <img src="recursos/sentinel.png">
                </header>
                <table>
                    <tr>
            """

                # primera fila como encabezado
                headers = self.result_list[0]
                html_content += "<tr>" + "".join(f"<th>{h}</th>" for h in headers) + "</tr>"

                # resto de filas
                for row in self.result_list[1:]:
                    estado = row[1]
                    archivo = row[0]
                    detalle = row[2] if len(row) > 2 else ""

                    # asignar clase según estado
                    estado_class = "secure" if "Recomended" in estado else "insecure"

                    html_content += f"<tr><td class='{estado_class}'>{estado}</td><td>{archivo}</td><td>{detalle}</td></tr>"

                html_content += """
                    </table>
                </body>
                </html>
                """

                with open("report.html", "w") as f:
                    f.write(html_content)




