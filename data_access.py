import sqlite3
from model.Todo import *

DATA_URL = "./data/donnees.sqlite"

#init de la base de données
conn = sqlite3.connect(DATA_URL)
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

#Création des tables
try :
    sql = """ CREATE TABLE IF NOT EXISTS "T_TODOS" ("Id"	INTEGER, "Description" TEXT)"""
    cursor.execute(sql)
    sql2 ="""CREATE TABLE IF NOT EXISTS "T_USER" ("Id"INTEGER,"Nom"	INTEGER)"""
    cursor.execute(sql2)
    conn.commit()

finally :
    print('table check ends')
    conn.close()

def getAllTodos():
    L=[]
    conn = sqlite3.connect( DATA_URL )
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * from T_TODOS" )

    for i in cursor:
        t = Todo(i["id"],i["Description"])
        L.append(t)
    return L

def add_todo(id_t,description):
    conn = sqlite3.connect( DATA_URL )
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO T_TODOS VALUES  (?,?)", (id_t,description) )
        conn.commit()

    finally :
        return "Fiche ajoutée"


def remove_todo(id_t):
    conn = sqlite3.connect( DATA_URL )
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM T_TODOS WHERE Id = ?", (id_t,) )
        conn.commit()
    except Exception as e:
        print("Something went wrong", e)
    finally :
        return "Fiche ajoutée"

def modify_todo(id_t, description):
    conn = sqlite3.connect( DATA_URL )
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        cursor.execute("UPDATE T_TODOS WHERE id = ? SET description = ?", (id_t,_description) )
        conn.commit()

    finally :
        return "Fiche ajoutée"

def get_todo(id_t):
    conn = sqlite3.connect( DATA_URL )
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM T_TODOS WHERE id = ?", (id_t) )
        conn.commit()
        for i in cursor:
            return Todo(i["id"],i["Description"])
    except Exception:
        print("Something went wrong")

