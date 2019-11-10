from fpdf import FPDF

## classe que defineix la generació del document PDF amb la informació de la pàgina a avaluar.
class CustomPDF(FPDF):
 
 ## Es defineix la funció que crearà la capçalera del document
    def header(self):
        self.set_font('Arial', 'B', 10)
        self.cell(100)
        self.cell(0, 5, 'Daniel Lòpez', ln=1)
        self.cell(100)
        self.cell(0, 5, 'Tipologia i cicle de vida de les dades', ln=1)
        self.cell(100)
        self.cell(0, 5, 'PRAC 1', ln=1)
        self.ln(20)
 
 ## Es defineix la funció que crearà el peu de pàgina del document
    def footer(self):
        self.set_y(-10)
        self.set_font('Arial', 'I', 8)
        page = 'Pàgina ' + str(self.page_no()) + '/{nb}'
        self.cell(0, 10, page, 0, 0, 'C')

## Es defineix la funció que crearà el contingut del document amb la informació generada per les consultes realitzades
    def informacio_scrap_pdf(self,pdf_path,existeixRobots,rob,delay,sitemap,tamanyWeb,tecnologiaWeb,propietariWeb):
        pdf = CustomPDF()
        # Create the special value {nb}
        pdf.alias_nb_pages()
        pdf.add_page()
        if (existeixRobots):
            pdf.set_font('Times','B',15)
            pdf.cell(0,10,txt="Contingut del fitxer robots.txt")
            pdf.ln()
            pdf.set_font('Times', '', 12)
            pdf.multi_cell(0,10,str(rob))
            pdf.ln()
            pdf.set_font('Times','B',13)
            pdf.cell(0,10,txt="Espera entre peticions")
            pdf.ln()
            pdf.set_font('Times', '', 12)
            pdf.cell(0,10,"L'espera entre peticions ha de ser de: " + str(delay) + " segons.")
            pdf.ln()
        if (sitemap):
            pdf.set_font('Times','B',15)
            pdf.cell(0,10,txt="Contingut del sitemap",ln=0)
            pdf.ln()
            pdf.set_font('Times', '', 12)
            pdf.multi_cell(0,10,str(sitemap))
            pdf.ln()
        pdf.ln()
        pdf.set_font('Times','B',15)
        pdf.cell(0,10,txt="Tamany de la Web",ln=0)
        pdf.ln()
        pdf.set_font('Times', '', 12)
        pdf.cell(0,10,"El tamany de la web és de : " + str(tamanyWeb) + " entrades.",ln=0)
        pdf.ln()
        pdf.ln()
        pdf.set_font('Times','B',15)
        pdf.cell(0,10,txt="Tecnologia Web",ln=0)
        pdf.ln()
        pdf.set_font('Times', '', 12)
        pdf.cell(0,10,"La tecnologia web emprada és: ", ln=0)
        pdf.ln()
        pdf.multi_cell(0,10,str(tecnologiaWeb))
        pdf.ln()
        pdf.set_font('Times','B',15)
        pdf.cell(0,10,txt="Propietari",ln=0)
        pdf.ln()
        pdf.set_font('Times', '', 12)
        pdf.cell(0,10,"El propietari de la web és: ", ln=0)
        pdf.ln()
        pdf.multi_cell(0,10,str(propietariWeb))
        pdf.ln()
        #line_no = 1
        #for i in range(50):
        #    pdf.cell(0, 10, txt="Line #{}".format(line_no), ln=1)
        #    line_no += 1
        pdf.output(pdf_path)