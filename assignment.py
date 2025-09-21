# ================================================
# 📊 Python Assignment: Data Analysis with Pandas & Visualization with Matplotlib
# Dataset: CORD-19 metadata.csv
# ================================================

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------
# Task 1: Load and Explore the Dataset
# ---------------------------
try:
    file_path = r"E:\Power Learn Academy 2025 July\Python Module\Assignments\wk7assignment\metadata.csv"
    df = pd.read_csv(file_path)

    print("✅ Dataset Loaded Successfully!\n")
    print("🔹 First 5 rows:")
    print(df.head(), "\n")

    print("🔹 Info:")
    print(df.info(), "\n")

    print("🔹 Missing Values:")
    print(df.isnull().sum(), "\n")

    # Clean dataset (drop rows missing important info)
    df = df.dropna(subset=["title", "publish_time"])
    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
    df["year"] = df["publish_time"].dt.year

except FileNotFoundError:
    print("❌ Error: File not found. Please check the file path.")
except Exception as e:
    print(f"❌ An error occurred: {e}")

# ---------------------------
# Task 2: Basic Data Analysis
# ---------------------------
print("\n📊 Summary Statistics (numeric columns):")
print(df.describe(include="all"), "\n")

# Publications per year
pubs_per_year = df["year"].value_counts().sort_index()
print("🔹 Publications per Year:")
print(pubs_per_year, "\n")

# Top journals
top_journals = df["journal"].value_counts().head(10)
print("🔹 Top 10 Journals Publishing COVID-19 Research:")
print(top_journals, "\n")

# Abstract word count
df["abstract_word_count"] = df["abstract"].fillna("").apply(lambda x: len(x.split()))
avg_words = df["abstract_word_count"].mean()
print(f"💡 Average abstract length: {avg_words:.2f} words\n")

# ---------------------------
# Task 3: Data Visualization
# ---------------------------

# 1. Publications over time
plt.figure(figsize=(8,5))
sns.barplot(x=pubs_per_year.index, y=pubs_per_year.values, color="blue")
plt.title("📈 Publications by Year")
plt.xlabel("Year")
plt.ylabel("Number of Papers")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Top Journals
plt.figure(figsize=(8,5))
sns.barplot(y=top_journals.index, x=top_journals.values, palette="viridis")
plt.title("📊 Top 10 Journals Publishing COVID-19 Papers")
plt.xlabel("Number of Papers")
plt.ylabel("Journal")
plt.tight_layout()
plt.show()

# 3. Histogram of Abstract Word Count
plt.figure(figsize=(8,5))
plt.hist(df["abstract_word_count"], bins=50, color="skyblue", edgecolor="black")
plt.title("📚 Distribution of Abstract Word Counts")
plt.xlabel("Word Count")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# ---------------------------
# Findings / Observations
# ---------------------------
print("\n🔎 Observations:")
print("- Most research papers were published in 2020 (COVID-19 outbreak year).")
print("- The top journals publishing COVID-19 research are:", list(top_journals.index[:3]))
print("- Abstract lengths vary, but on average contain about", round(avg_words), "words.")
