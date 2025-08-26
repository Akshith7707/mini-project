from fastapi import APIRouter, UploadFile, File
import os
import PyPDF2

router = APIRouter()

# Folder where resumes will be stored
UPLOAD_DIR = "data/resumes"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    """
    Upload and parse resume (PDF extraction for now)
    """
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save the uploaded file
    with open(file_path, "wb") as f:
        f.write(await file.read())

    extracted_text = ""

    # PDF resume parsing
    if file.filename.endswith(".pdf"):
        with open(file_path, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            for page in reader.pages:
                extracted_text += page.extract_text() or " "
    else:
        extracted_text = "Only PDF resumes supported right now."

    return {
        "message": f"{file.filename} uploaded successfully",
        "text_preview": extracted_text[:500]  # send preview
    }