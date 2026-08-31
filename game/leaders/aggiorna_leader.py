import os

# Cartella corrente dove si trovano i file dei leader
cartella = os.path.dirname(os.path.abspath(__file__))

for nome_file in os.listdir(cartella):
    percorso = os.path.join(cartella, nome_file)
    
    # Salta lo script stesso e controlla che sia un file valido
    if os.path.isfile(percorso) and nome_file != "aggiorna_leader.py":
        with open(percorso, 'rb') as f:
            dati = f.read()
        
        # Cerca la sequenza binaria di ".png" e la sostituisce con ".dds"
        if b'.png' in dati:
            nuovi_dati = dati.replace(b'.png', b'.dds')
            
            with open(percorso, 'wb') as f:
                f.write(nuovi_dati)
            print(f"Modificato: {nome_file}")

print("Fatto! Tutti i leader sono stati aggiornati a .dds")
