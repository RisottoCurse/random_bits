import os
import PyPDF2

def combine_pdfs(output_filename="combined.pdf"):
    desktop_path = # add path to pdf folder
    pdf_files = [f for f in os.listdir(desktop_path) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print("No PDF files found on the desktop.")
        return
    
    pdf_writer = PyPDF2.PdfMerger()

    for pdf in sorted(pdf_files):
        pdf_path = os.path.join(desktop_path, pdf)
        try :
            pdf_writer.append(pdf_path)
            print(f"Added {pdf_path} to the PDF merger.")
        except Exception as e:
            print(f"Error: {e}")

    output_path = os.path.join(desktop_path, output_filename)
    pdf_writer.write(output_path)
    pdf_writer.close()
    print(f"Combined PDF saved to {output_path}")

if __name__ == "__main__":
    combine_pdfs()

 