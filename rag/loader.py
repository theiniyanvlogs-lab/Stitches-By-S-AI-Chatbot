"""
==========================================================
Stitches By S AI Chatbot
PDF Loader Module
==========================================================

Loads all PDF documents from:

- data/fabric/
- data/tailoring/
- data/business/

Author: Sugumar R
==========================================================
"""

from pathlib import Path
from typing import List

from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader


class PDFLoader:
    """
    Loads PDF files from a directory.
    """

    def __init__(self, folder_path: str):
        self.folder_path = Path(folder_path)

    def load_documents(self) -> List[Document]:
        """
        Load every PDF inside the folder.

        Returns
        -------
        List[Document]
            LangChain Document objects.
        """

        documents = []

        if not self.folder_path.exists():
            raise FileNotFoundError(
                f"Folder not found: {self.folder_path}"
            )

        pdf_files = sorted(self.folder_path.glob("*.pdf"))

        if not pdf_files:
            print(f"No PDF files found in {self.folder_path}")
            return documents

        print(f"\nLoading PDFs from: {self.folder_path}")

        for pdf in pdf_files:

            try:

                loader = PyPDFLoader(str(pdf))

                pages = loader.load()

                for page in pages:

                    page.metadata["source_file"] = pdf.name
                    page.metadata["category"] = self.folder_path.name

                documents.extend(pages)

                print(
                    f"Loaded {pdf.name} ({len(pages)} pages)"
                )

            except Exception as error:

                print(
                    f"Failed to load {pdf.name}"
                )

                print(error)

        print(
            f"\nTotal Pages Loaded : {len(documents)}"
        )

        return documents


def load_all_documents(
    fabric_path: str,
    tailoring_path: str,
    business_path: str,
):
    """
    Load PDFs from all knowledge bases.
    """

    fabric_docs = PDFLoader(fabric_path).load_documents()

    tailoring_docs = PDFLoader(
        tailoring_path
    ).load_documents()

    business_docs = PDFLoader(
        business_path
    ).load_documents()

    return {
        "fabric": fabric_docs,
        "tailoring": tailoring_docs,
        "business": business_docs,
    }
