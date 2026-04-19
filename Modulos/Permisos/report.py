#/usr/bin/python3
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

class Report:
    def __init__(self, document, result_list):
        self.document = document
        self.result_list = result_list

    def report(self):
        if self.document == "pdf":
            # Crear PDF
            doc = SimpleDocTemplate("report/report.pdf", pagesize=letter)
            
            table = Table(self.result_list)
            
            # Estilo base
            table.setStyle(TableStyle([
                ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#273c75")),  # encabezado azul oscuro
                ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
                ("ALIGN", (0,0), (-1,-1), "CENTER"),
                ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
                ("FONTSIZE", (0,0), (-1,0), 12),
                ("BOTTOMPADDING", (0,0), (-1,0), 12),
                ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#7f8c8d")),
            ]))
            
            # Filas alternadas
            for i in range(1, len(self.result_list)):
                bg_color = colors.HexColor("#f1f2f6") if i % 2 == 0 else colors.HexColor("#ffffff")
                table.setStyle(TableStyle([("BACKGROUND", (0,i), (-1,i), bg_color)]))
            
            # Colores de estado
            for i, row in enumerate(self.result_list[1:], start=1):
                estado = row[1]
                if "Recomended" in estado:
                    table.setStyle(TableStyle([("TEXTCOLOR", (1,i), (1,i), colors.green)]))
                elif "Insecure" in estado:
                    table.setStyle(TableStyle([("TEXTCOLOR", (1,i), (1,i), colors.red)]))
            
            elements = [table]
            doc.build(elements)

        elif self.document == "html":
            # HTML moderno
            html_content = """
            <!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <title>Reporte de Auditoría</title>
                <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
                <style>
                    body {
                        font-family: 'Inter', sans-serif;
                        background-color: #f5f6fa;
                        color: #2f3640;
                        margin: 0;
                        padding: 0;
                    }
                    header {
                        background: linear-gradient(90deg, #1abc9c, #16a085);
                        padding: 20px 40px;
                        color: #fff;
                        display: flex;
                        align-items: center;
                    }
                    header img {
                        width: 70px;
                        margin-right: 20px;
                    }
                    header h1 { margin: 0; font-size: 24px; font-weight: 700; }
                    header h2 { margin: 5px 0 0 0; font-weight: 400; font-size: 14px; color: #dff9fb; }
                    #searchBox {
                        width: 50%;
                        margin: 20px auto;
                        display: block;
                        padding: 10px;
                        border-radius: 6px;
                        border: 1px solid #dcdde1;
                        font-size: 14px;
                    }
                    table {
                        width: 90%;
                        margin: 20px auto;
                        border-collapse: collapse;
                        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                    }
                    th, td {
                        padding: 12px 15px;
                        text-align: center;
                        border-bottom: 1px solid #dcdde1;
                    }
                    th {
                        background-color: #273c75;
                        color: #f5f6fa;
                        font-weight: 600;
                    }
                    tr:nth-child(even) { background-color: #f1f2f6; }
                    tr:hover { background-color: #dcdde1; }
                    .badge {
                        padding: 5px 10px;
                        border-radius: 12px;
                        font-size: 13px;
                        font-weight: 500;
                        color: #fff;
                    }
                    .secure { background-color: #44bd32; }
                    .insecure { background-color: #e84118; }
                    .unknown { background-color: #fbc531; color: #2f3640; }
                    .status-dot {
                        display: inline-block;
                        width: 12px;
                        height: 12px;
                        border-radius: 50%;
                        margin-right: 6px;
                    }
                    .green { background-color: #44bd32; }
                    .red { background-color: #e84118; }
                    .orange { background-color: #fbc531; }
                    footer {
                        text-align: center;
                        padding: 20px;
                        font-size: 13px;
                        color: #7f8fa6;
                        border-top: 1px solid #dcdde1;
                    }
                </style>
                <script>
                    function searchTable() {
                        var input = document.getElementById("searchBox");
                        var filter = input.value.toLowerCase();
                        var table = document.getElementById("auditTable");
                        var trs = table.getElementsByTagName("tr");
                        for (var i = 1; i < trs.length; i++) {
                            var tds = trs[i].getElementsByTagName("td");
                            var show = false;
                            for (var j = 0; j < tds.length; j++) {
                                if (tds[j].innerText.toLowerCase().indexOf(filter) > -1) {
                                    show = true;
                                    break;
                                }
                            }
                            trs[i].style.display = show ? "" : "none";
                        }
                    }
                </script>
            </head>
            <body>
                <header>
                    <img src="recursos/sentinel_blanco.png" alt="Logo SentinelLinux">
                    <div>
                        <h1>SentinelLinux - Reporte de Auditoría</h1>
                        <h2>Auditoría de seguridad según estándares ISO27001 / CIS</h2>
                    </div>
                </header>
                <input type="text" id="searchBox" onkeyup="searchTable()" placeholder="Buscar por archivo, permisos o estado...">
                <table id="auditTable">
            """

            headers = self.result_list[0]
            html_content += "<tr>" + "".join(f"<th>{h}</th>" for h in headers) + "</tr>"

            for row in self.result_list[1:]:
                archivo = row[0]
                estado = row[1]
                detalle = row[2] if len(row) > 2 else ""

                if "Recomended" in estado:
                    estado_class = "secure"
                    dot_class = "green"
                    icon = "✔️"
                elif "Insecure" in estado:
                    estado_class = "insecure"
                    dot_class = "red"
                    icon = "⚠️"
                else:
                    estado_class = "unknown"
                    dot_class = "orange"
                    icon = "❓"

                html_content += f"""
                <tr>
                    <td><span class='badge file'>📄 {archivo}</span></td>
                    <td><span class='badge perm'>{detalle}</span></td>
                    <td><span class='status-dot {dot_class}'></span><span class='badge {estado_class}'>{icon} {estado}</span></td>
                </tr>
                """

            html_content += """
                </table>
                <footer>
                    Generado automáticamente por SentinelLinux - Auditoría de Seguridad<br>
                    Fecha de generación: <script>document.write(new Date().toLocaleString());</script>
                </footer>
            </body>
            </html>
            """

            with open("report/report.html", "w") as f:
                f.write(html_content)