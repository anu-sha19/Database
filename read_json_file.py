import json
import sqlite3
import ast
import os

def initialize_database():
    if not os.path.exists('database.db'):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE "Authors" ("ID" VARCHAR(10), "FNAME" TEXT, "LNAME" TEXT)')
            cursor.execute('CREATE TABLE "Paper" ("ID" VARCHAR(10) NOT NULL,"Title" TEXT NOT NULL,"Submitter_firstname" TEXT,"Submitter_lastname" TEXT,"LastUpdate" TEXT, PRIMARY KEY("ID"))')
            cursor.execute('CREATE TABLE "Citations" ("ID" VARCHAR(10),"CITE_ID" VARCHAR(10))')
            cursor.execute('CREATE TABLE "Categories" ("ID" VARCHAR(10),"Category" TEXT)')
            conn.commit()

def insert_into_db(data):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        
        for paper in data:
            paper_id = paper['id']

            # Insert categories
            for category in paper['categories'].split():
                cursor.execute('INSERT INTO Categories (ID,Category) VALUES(?,?)', (paper_id, category))

            # Insert authors
            for author in paper['authors']:
                author = author.replace("'", "")
                first_name, last_name = author.split()[-1], author.split()[0]
                cursor.execute('INSERT INTO Authors (ID,FNAME,LNAME) VALUES(?,?,?)', (paper_id, first_name, last_name))

            # Insert citations
            for citation in ast.literal_eval(paper['cited']):
                cursor.execute('INSERT INTO Citations (ID,Cite_ID) VALUES(?,?)', (paper_id, citation))

            # Insert paper
            title = paper['title'].replace("'", "")
            submitter = paper["submitter"].replace("'", "").split()
            submitter_fname, submitter_lname = submitter[-1], submitter[0]
            cursor.execute('INSERT INTO Paper (ID,Title,Submitter_firstname,Submitter_lastname,LastUpdate) VALUES(?,?,?,?,?)', (paper_id, title, submitter_fname, submitter_lname, paper["last_update"]))

        conn.commit()

def main():
    initialize_database()

    papers_data = []
    with open('arXiv21.json', 'r', encoding="utf-8") as json_file:
        for line in json_file:
            papers_data.append(json.loads(line))

    insert_into_db(papers_data)

if __name__ == "__main__":
    main()