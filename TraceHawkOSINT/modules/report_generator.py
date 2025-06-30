# modules/report_generator.py

from fpdf import FPDF
import os

class ReportGenerator:
    def __init__(self, filename):
        # NEW: Full control over filename (no auto "reports/" prefix)
        self.filename = filename if filename.endswith('.pdf') else filename + '.pdf'

        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.sections = []

        self.pdf.add_page()
        self.pdf.set_font("Arial", "B", 16)
        self.pdf.cell(0, 10, "TraceHawkOSINT Report", ln=True, align="C")
        self.pdf.ln(10)

    def add_section(self, title, content_lines):
        if not content_lines:
            content_lines = ["[!] No output returned.\n"]

        self.pdf.set_font("Arial", "B", 14)
        self.pdf.cell(0, 10, title, ln=True)

        self.pdf.set_font("Arial", "", 12)
        if isinstance(content_lines, list):
            for line in content_lines:
                self.pdf.multi_cell(0, 10, line)
        else:
            self.pdf.multi_cell(0, 10, str(content_lines))

        self.pdf.ln(5)
        self.sections.append(title)

    def save(self):
        folder = os.path.dirname(self.filename)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)
        self.pdf.output(self.filename)

