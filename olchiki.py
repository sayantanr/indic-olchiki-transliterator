# =====================================================================
#  Streamlit App: Indic → Santali (Ol Chiki) Transliterator (Accurate)
# =====================================================================
#  Requirements:
#  pip install streamlit indic-transliteration
# =====================================================================

import streamlit as st
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
import zipfile, io, re, unicodedata
import pandas as pd

# -------------------------------------------------------------
# 1. OL CHIKI CHARACTER MAP (Full Vowel + Consonant + Diacritics)
# -------------------------------------------------------------
OL_CHIKI_MAP = {
    # Independent vowels
    'a': 'ᱚ', 'ā': 'ᱟ', 'i': 'ᱤ', 'ī': 'ᱤ', 'u': 'ᱩ', 'ū': 'ᱩ',
    'e': 'ᱮ', 'o': 'ᱳ',
    # Consonants
    'k': 'ᱠ', 'kh': 'ᱠᱷ', 'g': 'ᱜ', 'gh': 'ᱜᱷ', 'ṅ': 'ᱝ',
    'c': 'ᱪ', 'ch': 'ᱪᱷ', 'j': 'ᱡ', 'jh': 'ᱡᱷ', 'ñ': 'ᱧ',
    'ṭ': 'ᱴ', 'ṭh': 'ᱴᱷ', 'ḍ': 'ᱰ', 'ḍh': 'ᱰᱷ', 'ṇ': 'ᱬ',
    't': 'ᱛ', 'th': 'ᱛᱷ', 'd': 'ᱫ', 'dh': 'ᱫᱷ', 'n': 'ᱱ',
    'p': 'ᱯ', 'ph': 'ᱯᱷ', 'b': 'ᱵ', 'bh': 'ᱵᱷ', 'm': 'ᱢ',
    'y': 'ᱭ', 'r': 'ᱨ', 'l': 'ᱞ', 'v': 'ᱣ', 'w': 'ᱣ',
    'ś': 'ᱥ', 'ṣ': 'ᱥ', 's': 'ᱥ', 'h': 'ᱦ',
    'ṛ': 'ᱨ', 'ṝ': 'ᱨᱷ',
    # Diacritics
    'ṃ': 'ᱹ', 'ḥ': 'ᱺ', '̃': 'ᱸ', 'ː': 'ᱹ',
}

# -------------------------------------------------------------
# 2. Juktākṣara / Digraph Map (Phonetic Clusters)
# -------------------------------------------------------------
JUKTAKSHARA = {
    "kṣ": "ᱠᱥ", "kṣh": "ᱠᱥᱷ", "gy": "ᱜᱭ", "tr": "ᱛᱨ", "dr": "ᱫᱨ",
    "śr": "ᱥᱨ", "ṣṭ": "ᱥᱴ", "ṣṭh": "ᱥᱴᱷ", "ṇṭ": "ᱬᱴ",
    "ṇḍ": "ᱬᱰ", "ṇḍh": "ᱬᱰᱷ", "nt": "ᱱᱛ", "nd": "ᱱᱫ",
    "mp": "ᱢᱯ", "mb": "ᱢᱵ", "ṅk": "ᱝᱠ", "ṅg": "ᱝᱜ",
    "ñc": "ᱧᱪ", "ñj": "ᱧᱡ", "sk": "ᱥᱠ", "st": "ᱥᱛ", "sp": "ᱥᱯ",
    "hm": "ᱦᱢ", "hn": "ᱦᱱ", "hl": "ᱦᱞ", "hr": "ᱦᱨ",
}

VOWELS = {'a', 'ā', 'i', 'ī', 'u', 'ū', 'e', 'o'}
CONSONANTS = {k for k in OL_CHIKI_MAP.keys() if k not in VOWELS}

# -------------------------------------------------------------
# 3. Regex-Optimized Transliteration Function
# -------------------------------------------------------------
def roman_to_olchiki(text: str) -> str:
    """Convert ITRANS/ISO-15919 romanized text to Ol Chiki accurately."""
    text = unicodedata.normalize('NFC', text.lower())
    text = re.sub(r'aa', 'ā', text)
    text = re.sub(r'ii', 'ī', text)
    text = re.sub(r'uu', 'ū', text)
    text = re.sub(r'~n', 'ñ', text)
    text = re.sub(r'n(?=[kg])', 'ṅ', text)
    text = re.sub(r'\.m', 'ṃ', text)

    # Replace complex clusters first
    for digraph, olchiki in sorted(JUKTAKSHARA.items(), key=lambda x: len(x[0]), reverse=True):
        text = text.replace(digraph, olchiki)

    result = []
    i = 0
    while i < len(text):
        # consonant + vowel pair
        if i < len(text)-1 and text[i:i+2] in OL_CHIKI_MAP:
            result.append(OL_CHIKI_MAP[text[i:i+2]])
            i += 2
        elif i < len(text)-1 and text[i] in OL_CHIKI_MAP and text[i+1] in VOWELS:
            result.append(OL_CHIKI_MAP[text[i]] + OL_CHIKI_MAP[text[i+1]])
            i += 2
        elif text[i] in OL_CHIKI_MAP:
            result.append(OL_CHIKI_MAP[text[i]])
            i += 1
        else:
            result.append(text[i])
            i += 1
    return ''.join(result)

# -------------------------------------------------------------
# 4. Indic Scripts Supported via indic-transliteration
# -------------------------------------------------------------
scripts = {
    "Assamese": sanscript.BENGALI,
    "Bengali": sanscript.BENGALI,
    "Bodo": sanscript.DEVANAGARI,
    "Dogri": sanscript.DEVANAGARI,
    "Gujarati": sanscript.GUJARATI,
    "Hindi": sanscript.DEVANAGARI,
    "Kannada": sanscript.KANNADA,
    "Kashmiri": sanscript.DEVANAGARI,
    "Konkani": sanscript.DEVANAGARI,
    "Maithili": sanscript.DEVANAGARI,
    "Malayalam": sanscript.MALAYALAM,
    "Manipuri": sanscript.BENGALI,
    "Marathi": sanscript.DEVANAGARI,
    "Nepali": sanscript.DEVANAGARI,
    "Odia": sanscript.ORIYA,
    "Punjabi": sanscript.GURMUKHI,
    "Sanskrit": sanscript.DEVANAGARI,
    "Sindhi": sanscript.DEVANAGARI,
    "Tamil": sanscript.TAMIL,
    "Telugu": sanscript.TELUGU,
}

# -------------------------------------------------------------
# 5. Streamlit App UI
# -------------------------------------------------------------
st.set_page_config(page_title="Indic → Santali (Ol Chiki) Transliterator", layout="centered")
st.title("🪶 Indic → Santali (Ol Chiki) Transliterator")

st.markdown("""
Upload a **ZIP** containing `.txt` files in any supported Indic script (like Hindi, Bengali, Tamil, etc.).  
Each file will be transliterated into **Santali (Ol Chiki)** script.
""")

uploaded_file = st.file_uploader("Upload ZIP of text files", type="zip")
source_lang = st.selectbox("Select Source Language (Script)", options=list(scripts.keys()))

if uploaded_file and source_lang:
    source_scheme = scripts[source_lang]
    try:
        with zipfile.ZipFile(uploaded_file, 'r') as zip_ref:
            txt_files = [f for f in zip_ref.namelist() if f.lower().endswith('.txt')]
            if not txt_files:
                st.error("No `.txt` files found in the ZIP.")
                st.stop()

            st.info(f"Found {len(txt_files)} file(s). Processing...")

            output_zip = io.BytesIO()
            with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as new_zip:
                for txt_file in txt_files:
                    try:
                        content = zip_ref.read(txt_file).decode('utf-8')
                    except UnicodeDecodeError:
                        content = zip_ref.read(txt_file).decode('utf-8', errors='replace')

                    # Indic → Roman (ITRANS)
                    try:
                        roman_text = transliterate(content, source_scheme, sanscript.ITRANS)
                    except Exception as e:
                        st.warning(f"Skipping {txt_file}: Transliteration failed ({e})")
                        continue

                    # Roman → Ol Chiki
                    olchiki_text = roman_to_olchiki(roman_text)

                    new_name = txt_file.rsplit('.', 1)[0] + "_olchiki.txt"
                    new_zip.writestr(new_name, olchiki_text)

            output_zip.seek(0)
            st.success("✅ Conversion complete!")
            st.download_button(
                label="⬇️ Download Ol Chiki ZIP",
                data=output_zip,
                file_name="olchiki_transliterated.zip",
                mime="application/zip"
            )

    except zipfile.BadZipFile:
        st.error("Corrupted or invalid ZIP file.")
    except Exception as e:
        st.error(f"Unexpected error: {e}")
