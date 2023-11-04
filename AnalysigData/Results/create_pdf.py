from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet
import os
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

def add_image_to_pdf(pdf_file, img_file):
    print('on ajoute : '+str(img_file)+" à "+str(pdf_file))
    out_pdf_file = 'report_with_images.pdf'

    packet = io.BytesIO()
    can = canvas.Canvas(packet)
    x_start = 0
    y_start = 0
    can.drawImage(img_file, x_start, y_start, width=120, preserveAspectRatio=True, mask='auto')
    can.save()

    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    existing_pdf = PdfFileReader(open(pdf_file, "rb"))
    output = PdfFileWriter()

    for i in range(len(existing_pdf.pages)):
        page = existing_pdf.getPage(i)
        page.mergePage(new_pdf.getPage(0))  # Utilisez toujours la première page de l'image
        output.addPage(page)

    outputStream = open(out_pdf_file, "wb")
    output.write(outputStream)
    outputStream.close()

def generate_report(stats,test_number):
    # Créer un PDF
    doc = SimpleDocTemplate(f"/Users/Utilisateur/Desktop/Travail/Python/ThorCore/rapport.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Ajouter le titre
    titre = Paragraph("<b>Rapport Statistique</b>", styles['Title'])
    contenu = [titre]

    # Ajouter les statistiques
    stats_paragraph = ""
    for stat in stats:
        stats_paragraph += f"Test number: {stat['Test number']}, Value: {stat['Value']}<br/>"
        stats_paragraph += f"Mean Value: {stat['Mean Value']}, Range: {stat['Range']}<br/>"
        stats_paragraph += f"Variance: {stat['Variance']}, Median: {stat['Median']}<br/>"
        stats_paragraph += f"Mean Deviation: {stat['Mean Deviation']}, Standard Deviation: {stat['Standard Deviation']}<br/>"
        stats_paragraph += f"Skewness: {stat['Skewness']}, Kurtosis: {stat['Kurtosis']}<br/><br/>"

    contenu.append(Paragraph(stats_paragraph, styles['Normal']))

    # Générer le PDF
    doc.build(contenu)

def get_images(path):
    if not os.path.exists(path):
        print(f"Le dossier {path} n'existe pas.")
        return []

    images = []
    extensions_valides = ['.jpg', '.jpeg', '.png', '.gif']

    for root, dirs, files in os.walk(path):
        for fichier in files:
            extension = os.path.splitext(fichier)[-1].lower()

            if extension in extensions_valides:
                chemin_image = os.path.join(root, fichier)
                images.append(chemin_image)

    return images

def images(test_number):
    image_dir = f"/Users/Utilisateur/Desktop/Travail/Python/ThorCore/AnalysisData/Results/plots/"
    image_types=get_images(image_dir)


    for image_type in image_types:
        print(image_type)
        add_image_to_pdf(image_type, "/Users/Utilisateur/Desktop/Travail/Python/ThorCore/rapport.pdf")