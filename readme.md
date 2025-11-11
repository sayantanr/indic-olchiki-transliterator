
📘 *Indic → Santali (Ol Chiki) Transliterator (with Streamlit UI)* .

---

# 🪶 Indic → Santali (Ol Chiki) Transliterator

A **Streamlit-based web app** that converts any Indic language text (Hindi, Bengali, Tamil, Telugu, etc.) into **Santali (Ol Chiki)** script using a combination of the `indic-transliteration` library and a custom **Roman → Ol Chiki phonetic mapping**.

This app supports **batch conversion** — simply upload a ZIP file containing `.txt` documents, and it will produce a downloadable ZIP with all files transliterated into **Ol Chiki**.

---

## 🚀 Features

✅ Converts from any major **Indic script** to **Santali (Ol Chiki)**
✅ Supports **22 scheduled Indian languages**
✅ Handles **vowels, consonants, digraphs, diacritics, and nasalization**
✅ Works with **ZIP uploads** of multiple `.txt` files
✅ Built with **Streamlit** for a clean web interface
✅ 100% Unicode-compliant, syllable-aware conversion
✅ Preserves punctuation, digits, and formatting

---

## 🧰 Tech Stack

| Component                         | Description                                    |
| --------------------------------- | ---------------------------------------------- |
| **Python 3.8+**                   | Core language                                  |
| **Streamlit**                     | Web application framework                      |
| **indic-transliteration**         | Converts Indic scripts → ITRANS (Roman)        |
| **Custom Transliterator**         | Converts Roman → Ol Chiki using phonetic rules |
| **Regex + Unicode Normalization** | Handles vowels, digraphs, and nasal forms      |
| **zipfile + io**                  | Batch input/output management                  |

---

## 🏗️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/indic-to-olchiki.git
   cd indic-to-olchiki
   ```

2. **Install dependencies**

   ```bash
   pip install streamlit indic-transliteration pandas
   ```

3. **Run the Streamlit app**

   ```bash
   streamlit run indic_to_olchiki.py
   ```

4. Open your browser and visit
   👉 [http://localhost:8501](http://localhost:8501)

---

## 🗂️ Usage

1. Prepare a **ZIP file** containing one or more `.txt` files written in your source language.
   Example:

   ```
   hindi_poem.txt
   bengali_story.txt
   tamil_news.txt
   ```

2. Open the web app and:

   * Choose the **source script** (e.g., Hindi, Bengali, Tamil)
   * Upload your **ZIP file**
   * Click **Convert**

3. After conversion, download your new ZIP:

   ```
   hindi_poem_olchiki.txt
   bengali_story_olchiki.txt
   tamil_news_olchiki.txt
   ```

---

## 🧠 How It Works

1. **Indic → Roman (ITRANS):**
   The app uses `indic-transliteration` to convert Indic scripts into a standardized Roman phonetic form (ITRANS/ISO-15919).

2. **Roman → Ol Chiki:**
   The Roman text is then parsed syllable by syllable and transliterated into Santali (Ol Chiki) script using:

   * `OL_CHIKI_MAP`: Individual vowel and consonant mapping
   * `JUKTAKSHARA`: Common phonetic clusters (e.g., “tr”, “dr”, “gy”)
   * Regex + vowel detection logic for accuracy

3. **Batch Output:**
   All processed files are written into a new ZIP archive, ready for download.

---

## 🌐 Supported Languages (Source Scripts)

| Language  | Script     |
| --------- | ---------- |
| Assamese  | Bengali    |
| Bengali   | Bengali    |
| Bodo      | Devanagari |
| Dogri     | Devanagari |
| Gujarati  | Gujarati   |
| Hindi     | Devanagari |
| Kannada   | Kannada    |
| Kashmiri  | Devanagari |
| Konkani   | Devanagari |
| Maithili  | Devanagari |
| Malayalam | Malayalam  |
| Manipuri  | Bengali    |
| Marathi   | Devanagari |
| Nepali    | Devanagari |
| Odia      | Oriya      |
| Punjabi   | Gurmukhi   |
| Sanskrit  | Devanagari |
| Sindhi    | Devanagari |
| Tamil     | Tamil      |
| Telugu    | Telugu     |

---

## 🧩 Example

### Input (`Hindi`)

```
नमस्ते दुनिया
```

### Intermediate (ITRANS)

```
namaste duniyaa
```

### Output (`Ol Chiki`)

```
ᱱᱟᱢᱥᱛᱮ ᱫᱩᱱᱤᱭᱟᱣ
```

---

## ⚙️ Project Structure

```
indic-olchiki-transliterator/
├── olchiki.py     # Main Streamlit app
├── README.md               # Project documentation
      
              
```

---



---

## 👨‍💻 Author

**Sayantan Roy**
Cognizant · Software Engineer
Skills: .NET · SQL · ServiceNow · AI · NLP · Indic Computing

---




