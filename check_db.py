import psycopg2

try:
    conn = psycopg2.connect(
        dbname="professeur_ia",
        user="postgres",
        password="onion123",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
    tables = cur.fetchall()
    
    print("====== RESULTATS ======")
    if not tables:
        print("Aucune table trouvée. La base est vide.")
    else:
        print(f"[{len(tables)}] Tables trouvées :")
        for t in tables:
            print("-", t[0])
    
    conn.close()
except Exception as e:
    print("====== ERREUR ======")
    print(e)
