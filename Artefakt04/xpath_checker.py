import xml.etree.ElementTree as ET
import glob
# Student projektuje tutaj cechy elementu (symulacja złożonego XPath)
TARGET_ID = "buttonStart"
TARGET_TEXT = "Start"
def validate_selector():
    matches = 0
    # Przestrzeń nazw Androida w plikach XML
    ns = {'android': 'http://schemas.android.com/apk/res/android'}
    for file in glob.glob("../Artefakt02/decompiled_apk/res/layout/*.xml"):
        tree = ET.parse(file)
        for elem in tree.iter():
            # Logika Boolean: ID się zgadza ORAZ tekst się zgadza
            node_id = elem.get('{http://schemas.android.com/apk/res/android}id', '')
            node_text = elem.get('{http://schemas.android.com/apk/res/android}text', '')
            if TARGET_ID in node_id and node_text == TARGET_TEXT:
                matches += 1
    result = f"Znaleziono dopasowań: {matches}"
    status = "ZALICZONE" if matches == 1 else "BŁĄD: Selektor nie jest unikalny!"
    with open('xpath_verification.txt', 'w') as f:
        f.write(f"Selektor: ID={TARGET_ID}, Text={TARGET_TEXT}\n{result}\nStatus: {status}")
    print(f"{result} -> {status}")
validate_selector()