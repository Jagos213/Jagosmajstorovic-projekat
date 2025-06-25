def get_bot_response(message):
    message = message.lower()
    if "zdravo" in message or "cao" in message:
        return "Zdravo! Dobro došli u našu firmu za ugradnju i održavanje klima uređaja. Kako mogu da vam pomognem?"
    elif "ugradnja" in message or "montaža" in message:
        return "Nudimo profesionalnu ugradnju klima uređaja. Da li želite da zakažete termin ili vas zanima cena?"
    elif "održavanje" in message or "servis" in message:
        return "Redovan servis klima produžava njen vek trajanja. Da li želite da zakažete servis?"
    elif "cene" in message or "koliko" in message:
        return "Naše cene zavise od vrste usluge. Možete pogledati cenovnik na sajtu ili mi recite koja usluga vas zanima."
    elif "kontakt" in message or "broj" in message:
        return "Možete nas kontaktirati na broj 060/123-4567 ili putem mejla klima@firma.rs."
    elif "garancija" in message:
        return "Dajemo garanciju na sve naše radove i ugrađene uređaje. Trajanje zavisi od tipa uređaja i usluge."
    else:
        return "Nisam siguran kako da odgovorim na to. Možete li precizirati pitanje vezano za naše klima usluge?"