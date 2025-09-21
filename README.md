
```markdown
# 📚 CORD-19 Dataset Explorer

This project is part of the **Power Learn Academy Python Assignment (Week 7)**.  
It demonstrates **data analysis and visualization** using `pandas`, `matplotlib`, `seaborn`, and an interactive dashboard built with `streamlit`.

---

## 🚀 Project Overview
The project uses the **CORD-19 metadata dataset** to:
- 📂 Load and clean data  
- 🔎 Perform exploratory data analysis (EDA)  
- 📊 Visualize publication patterns (per year, per journal, abstract lengths)  
- 💡 Generate insights on COVID-19 research trends  

The solution includes:
1. **Python script (`analysis.py`)** → handles dataset loading, cleaning, analysis, and visualizations  
2. **Streamlit app (`app.py`)** → provides an interactive dashboard  

---

## 🛠️ Technologies Used
- **Python 3.x**
- [Pandas](https://pandas.pydata.org/) → Data handling & analysis  
- [Matplotlib](https://matplotlib.org/) → Data visualization  
- [Seaborn](https://seaborn.pydata.org/) → Statistical visualizations  
- [Streamlit](https://streamlit.io/) → Interactive dashboard  
- [WordCloud](https://amueller.github.io/word_cloud/) *(optional, for text visualizations)*  

---

## 📂 Project Structure
```

📁 wk7assignment
┣ 📄 assignment.py     # Core data analysis script
┣ 📄 app.py          # Streamlit interactive app

┣ 📄 README.md       # Project documentation

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository (if using GitHub)
```bash
git clone https://github.com/<your-username>/cord19-analysis.git
cd cord19-analysis
````

### 2️⃣ Install Dependencies

Make sure you have Python installed. Then install required packages:

```bash
pip install pandas matplotlib seaborn streamlit wordcloud
```

### 3️⃣ Run the Python Script

```bash
python analysis.py
```

### 4️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

---

## 📊 Features

* **Data Preview** → View first rows, dataset shape, and columns
* **Summary Statistics** → Basic descriptive analysis
* **Publications by Year** → Trend of research publications
* **Top Journals** → Journals contributing most publications
* **Abstract Length Distribution** → Histogram of abstract sizes
* **Interactive Dashboard** → Navigate via sidebar (Home, Data, Analysis, Visualizations, Insights)

---

## 💡 Key Insights

* Research publications **peaked in recent years**, especially during the COVID-19 pandemic.
* A small number of journals contribute the **largest share** of publications.
* Abstract lengths vary widely, indicating differences in research reporting styles.
* Dataset is useful for **text mining** and **research trend analysis**.

---

## 📸 Screenshots

*(Add screenshots of your Streamlit app once it’s running — e.g., charts, dashboard preview)*

---

## 👨‍💻 Author

**Francis Kienji (Frank MK)**

* 🌐 [Portfolio Website](https://github.com/FranNMK)
* 🎥 [YouTube](https://shorturl.at/4Mx75)
* 📱 [Instagram](https://www.instagram.com/frankmk2025)
* 💼 [LinkedIn](#) *(optional)*

---

## 📜 License

This project is for **educational purposes only** (Power Learn Academy).
Free to use and modify with attribution.

```


