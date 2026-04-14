import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, Image, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

EXPERIMENTS_DATA = [
    {"id": 1, "name": "DETERMINATION OF HARDNESS (Ca²⁺) OF WATER USING EDTA COMPLEXOMETRY METHOD", "slug": "exp1"},
    {"id": 2, "name": "ESTIMATION OF AMOUNT OF CHLORIDE CONTENT OF A WATER SAMPLE", "slug": "exp2"},
    {"id": 3, "name": "DETERMINATION OF THE AMOUNT OF SODIUM CARBONATE AND SODIUM HYDROXIDE IN A MIXTURE BY TITRATION", "slug": "exp3"},
    {"id": 4, "name": "DETERMINATION OF STRENGTH OF AN ACID USING pH METER", "slug": "exp4"},
    {"id": 5, "name": "DETERMINATION OF STRENGTH OF AN ACID BY CONDUCTOMETRY", "slug": "exp5"},
    {"id": 6, "name": "DETERMINATION OF THE STRENGTH OF A MIXTURE OF ACETIC ACID AND HYDROCHLORIC ACID BY CONDUCTOMETRY", "slug": "exp6"},
    {"id": 7, "name": "DETERMINATION OF FERROUS ION USING POTASSIUM DICHROMATE BY POTENTIOMETRIC TITRATION", "slug": "exp7"},
    {"id": 8, "name": "DETERMINATION OF MOLECULAR WEIGHT OF A POLYMER BY VISCOSITY AVERAGE METHOD", "slug": "exp8"}
]

def get_experiment_title(slug):
    for exp in EXPERIMENTS_DATA:
        if exp['slug'] == slug:
            return exp['name'].upper()
    return "EXPERIMENT TITLE"

def get_standard_styles():
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'TitleStyle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=14, alignment=1, spaceAfter=20
    )
    h2_style = ParagraphStyle(
        'H2', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=12, spaceBefore=15, spaceAfter=10
    )
    normal_style = styles['Normal']
    normal_style.fontSize = 11
    normal_style.spaceAfter = 6
    calc_style = ParagraphStyle(
        'CalcStyle', parent=normal_style, fontName='Helvetica', fontSize=11, spaceBefore=2, spaceAfter=2, leftIndent=20
    )
    return styles, title_style, h2_style, normal_style, calc_style

def add_pdf_header(elements, slug, date_str, name, reg_no, title_style, normal_style):
    title = get_experiment_title(slug)
    elements.append(Paragraph(title, title_style))
    elements.append(Paragraph(f"Date: {date_str}", normal_style))
    elements.append(Paragraph(f"Name: {name}", normal_style))
    elements.append(Paragraph(f"Registration No: {reg_no}", normal_style))
    elements.append(Spacer(1, 10))
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.black, spaceBefore=0, spaceAfter=15))

def get_standard_table_style():
    return TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ])

def create_graph(x_data, y_data, x_label, y_label, title=""):
    plt.figure(figsize=(6, 4))
    plt.plot(x_data, y_data, marker='o', linestyle='-', color='b')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if title:
        plt.title(title)
    plt.grid(True)
    
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png', bbox_inches='tight')
    plt.close()
    img_buffer.seek(0)
    return Image(img_buffer, width=400, height=270)
