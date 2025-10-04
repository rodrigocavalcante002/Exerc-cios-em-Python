import streamlit as st
from PyPDF2 import PdfReader

st.title("Analisador de Amostras em PDF")

uploaded_file = st.file_uploader("Envie o arquivo PDF", type="pdf")

if uploaded_file:
    reader = PdfReader(uploaded_file)
    textComp = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            textComp += text.lower().replace("\n", " ").replace("\xa0", " ")

    wordKeytipAmostra = [
        "santot", "soro", "placon", "soro/plasma", "plasma",
        "spcon", "splpl", "stplc", "biop", "uriso"
    ]

    wordKeyTempC = ["soroc", "placon", "spconp", "stplc"]
    wordKeyTempR = ["Sangue", "soro", "plasma", "splpl"]
    amostras = {
        "Sangue": textComp.count(wordKeytipAmostra[0]),
        "soro": textComp.count(wordKeytipAmostra[1]),
        "plasmaCon": textComp.count(wordKeytipAmostra[2]),
        "soro/plasma": textComp.count(wordKeytipAmostra[3]),
        "plasma": textComp.count(wordKeytipAmostra[4]),
        "spcon": textComp.count(wordKeytipAmostra[5]),
        "splpl": textComp.count(wordKeytipAmostra[6]),
        "stplc": textComp.count(wordKeytipAmostra[7]),
        "biop": textComp.count(wordKeytipAmostra[8]),
        "urina": textComp.count(wordKeytipAmostra[9])
    }

    quantSan = amostras["Sangue"]
    quantSoro = amostras["soro"] + amostras["plasmaCon"] - amostras["soro/plasma"]
    quantPl = amostras["plasma"] - amostras["soro/plasma"]
    quantOutros = amostras["spcon"] + amostras["splpl"] + amostras["stplc"]
    quantBiop = amostras["biop"]
    quantUrina = amostras["urina"]

    quantCongelado = sum(textComp.count(temp) for temp in wordKeyTempC)
    quantRefrigerado = quantSan+amostras["soro"] + amostras["plasma"]+amostras["splpl"]  - amostras["soro/plasma"]

    st.subheader("Resultados da Análise")
    st.write(f"🧪 Soro: {quantSoro}")
    st.write(f"🧪 Plasma: {quantPl}")
    st.write(f"🧪 Sangue: {quantSan}")
    st.write(f"🧪 Outros: {quantOutros}")
    st.write(f"🧪 Biopsia: {quantBiop}")
    st.write(f"🧪 Urina: {quantUrina}")
    st.write(f"❄️ Amostras Congeladas: {quantCongelado}")
    st.write(f"❄️ Amostras Refrigeradas: {quantRefrigerado}")