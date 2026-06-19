# E-Commerce Logistics AI Decision Support System
### *An Edge AI & SWARA-COBRA Multi-Criteria Framework for E-Commerce Carrier Selection*

---

## 📚 Academic & Methodological Overview

This repository hosts an advanced, privacy-first **Logistics Decision Support System (DSS)** designed to solve the critical carrier selection problem for e-commerce enterprises. Operating entirely on decentralized, **On-Device (Edge AI)** hardware infrastructure, the architecture synthesizes mathematical multi-criteria optimization with natural language engineering.

The mathematical core of the decision engine implements a hybrid formulation:
1. **SWARA (Step-wise Weight Assessment Ratio Analysis):** Used to structure and compute the dynamic, subjective criteria weights ($w_j$) derived from expert-level operational preferences.
2. **COBRA (COmprehensive Distance Based Ranking):** Deployed as the core multi-criteria evaluation matrix to normalize conflicting benefit and cost criteria, measure exact Euclidean and absolute distances to ideal/anti-ideal parameters, and rank absolute route efficiency.

**Methodological Anchor:**
> Güler, A. (2025). Türkiye’deki bilişim sistemleri ve teknolojileri bölümlerinin SWARA yöntemi ile ağırlıklandırılması ve COBRA yöntemiyle sıralanması. *Uluslararası Avrasya Sosyal Bilimler Dergisi, 16*(60), 825-840.

---

## 🏗️ System & True RAG Architecture

The platform bypasses data residency vulnerabilities and external API latencies by anchoring its retrieval pipelines locally via the **Microsoft Foundry Local SDK** and the **Windows Machine Learning (WinML)** hardware pipeline running an offline `phi-1.5-mini` Large Language Model.

### Data Engineering & Pipeline Mechanics:
* **The Dataset:** Derived from the **Brazilian Olist E-Commerce Ecosystem Dataset** (comprising over 113,000 corporate purchase orders). Through intensive data processing (`veri_isleme.py`), massive cross-table interactions (`orders`, `items`, `reviews`, `sellers`, `customers`) were aggregated into definitive point-to-point state logistics routes (e.g., `SP -> RJ`).
* **True RAG Pipeline (Retrieve -> Augment -> Generate):**
  * **Retrieve:** The manager parses the user's natural language query (e.g., *"Budget is strictly limited, maximize buyer satisfaction"*), maps intent parameters, and executes a vectorized similarity search using a localized mathematical embedding alignment via `scikit-learn`'s cosine similarity matrix.
  * **Augment:** The highest-ranked logistical vector indices (Top-K routes) are extracted dynamically from the `sqlite3` database file (`lojistik.db`) and injected directly into a structured system prompt context block.
  * **Generate:** The fully bound context string is pushed onto the localized WinML hardware ring. `phi-1.5-mini` synthesizes a comprehensive, deterministic corporate logistics analytics report in real-time with zero cloud dependency and zero data leakage risk.

---

## 🛠️ Technology Stack

| Architecture Layer | Core Technologies |
| :--- | :--- |
| **Artificial Intelligence (Edge AI)** | Microsoft Foundry Local SDK, WinML API, `phi-1.5-mini` (3.8B LLM) |
| **Mathematical Modeling** | SWARA Evaluation, COBRA Ranking Formulations, Vectorized Embedding Simulations |
| **Data Engineering** | Python Core, SQLite 3, Pandas, NumPy, Scikit-learn (Cosine Metrics) |
| **User Interface & Execution** | Streamlit Web Framework, Matplotlib/Line/Bar Native Dynamic Rendering |

---

## 📦 Installation & Local Deployment

### Prerequisites
* **OS:** Windows 10/11 (Required for native Windows Machine Learning / WinML drivers)
* **Python Engine:** Python 3.10 or higher installed locally

### Step-by-Step Setup

1. **Clone the Repository**
```bash
   git clone [https://github.com/Aysenuryesilova/E-Commerce-Logistics-AI-Decision-Support-System.git](https://github.com/Aysenuryesilova/E-Commerce-Logistics-AI-Decision-Support-System.git)
   cd E-Commerce-Logistics-AI-Decision-Support-System
