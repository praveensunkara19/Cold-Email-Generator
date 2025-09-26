# portfolio_db.py

import os
import pandas as pd
import chromadb
import uuid

class Portfolio:
    def __init__(self, file_path=None):
        # Set default file path relative to current file
        if file_path is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(base_dir, 'resources', 'portfolio.csv')

        self.file_path = file_path

        # Load portfolio CSV if exists, else initialize empty DataFrame
        if os.path.exists(self.file_path):
            self.data = pd.read_csv(self.file_path)
        else:
            print(f"⚠️ portfolio.csv not found at {self.file_path}. Continuing with empty dataset.")
            self.data = pd.DataFrame(columns=['Techstack', 'portfolio'])

        # Initialize ChromaDB client and collection
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name='Portfolio')

    def load_portfolio(self):
        """
        Load portfolio data into the ChromaDB collection if it's empty.
        """
        if self.collection.count() == 0:
            for _, row in self.data.iterrows():
                self.collection.add(
                    documents=[row["Techstack"]],
                    metadatas=[{"links": row["portfolio"]}],
                    ids=[str(uuid.uuid4())]
                )

    def query_links(self, skills):
        """
        Query the portfolio collection based on provided skills.
        Returns a list of metadata dicts with 'links'.
        """
        results = self.collection.query(query_texts=skills, n_results=2)
        return results.get('metadatas', [])
