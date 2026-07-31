"""
==========================================================
Stitches By S AI Chatbot
Document Splitter
==========================================================

Splits PDF documents into smaller chunks for
embedding and retrieval.

Author : Sugumar R
==========================================================
"""

from typing import List

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)


class DocumentSplitter:
    """
    Split LangChain documents into chunks.
    """

    def __init__(
        self,
        chunk_size: int = CHUNK_SIZE,
        chunk_overlap: int = CHUNK_OVERLAP,
    ):

        self.splitter = RecursiveCharacterTextSplitter(

            chunk_size=chunk_size,

            chunk_overlap=chunk_overlap,

            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                "",
            ],
        )

    def split(
        self,
        documents: List[Document],
    ) -> List[Document]:
        """
        Split documents.

        Parameters
        ----------
        documents : List[Document]

        Returns
        -------
        List[Document]
        """

        if not documents:

            print("No documents received.")

            return []

        chunks = self.splitter.split_documents(
            documents
        )

        print(
            f"Created {len(chunks)} chunks."
        )

        return chunks


def split_all_documents(
    document_dict,
):
    """
    Split all knowledge bases.
    """

    splitter = DocumentSplitter()

    return {

        "fabric":
            splitter.split(
                document_dict["fabric"]
            ),

        "tailoring":
            splitter.split(
                document_dict["tailoring"]
            ),

        "business":
            splitter.split(
                document_dict["business"]
            ),
    }
