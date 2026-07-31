# 📦 E-Commerce Logistics AI Decision Support System
### *An Edge AI, SWARA-COBRA Multi-Criteria Framework & True RAG System for E-Commerce Carrier & Route Selection*

---

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B.svg)](https://streamlit.io/)
[![Microsoft Foundry Local](https://img.shields.io/badge/Edge%20AI-Azure%20Foundry%20Local-0078D4.svg)](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📖 Executive Summary & Context

This project was developed for **Barbaros Bey's AI & Decision Support Summer Program**.

Rather than treating logistics decision-making as a raw prediction task, this system adopts a **research-first, product-oriented methodology**. It addresses the critical e-commerce last-mile carrier selection problem by combining:
1. **Mathematical Multi-Criteria Optimization (SWARA-COBRA):** To structure subjective criteria weights and compute exact distance-based route efficiency rankings.
2. **True RAG & Local LLM (Azure Foundry Local / WinML):** Operating on-device (`phi` model) to deliver zero-data-leakage, explainable executive analytics reports in response to natural language manager queries.
3. **4-Week Research & Development Journal:** Tracking operational problem discovery, literature benchmarking, and architectural evolution day by day.

---

## 📁 Repository Structure & Research Deliverables

- 📓 [RESEARCH_JOURNAL.md](RESEARCH_JOURNAL.md) — 4-week detailed learning log & daily research entries (Days 1–28).
- 📚 [LITERATURE_SURVEY.md](LITERATURE_SURVEY.md) — Academic paper survey, market benchmarks, and the identified research gap.
- 🎬 [PRESENTATION_SCRIPT.md](PRESENTATION_SCRIPT.md) — 5-minute video presentation guide and timestamped script.
- 💻 [app.py](app.py) — Interactive Streamlit Web Application (SWARA-COBRA matrix & True RAG Analyst).
- 🗄️ [lojistik.db](lojistik.db) — SQLite database compiled from 113,000+ Brazilian Olist e-commerce purchase orders.
- ⚙️ [veri_isleme.py](veri_isleme.py) — Data processing pipeline for point-to-point route performance aggregation.

---

## 🏗️ System & True RAG Architecture

```
                               ┌─────────────────────────┐
                               │   Olist Logistics DB    │
                               │     (113,000+ Orders)   │
                               └────────────┬────────────┘
                                            │
                               ┌────────────▼────────────┐
                               │  SWARA-COBRA Optimization│
                               │   (Cost/Benefit Matrix) │
                               └────────────┬────────────┘
                                            │
    ┌─────────────────────────┐             │
    │ Manager NL Query        │             │
    │ ("Low cost, high SLA")  │             │
    └────────────┬────────────┘             │
                 │                          │
                 ▼                          ▼
    ┌────────────────────────────────────────────────────┐
    │ Cosine Vector Similarity (Retrieve Top-K Routes)   │
    └─────────────────────────┬──────────────────────────┘
                              │
                              ▼
    ┌────────────────────────────────────────────────────┐
    │ System Prompt Context Augmentation                 │
    └─────────────────────────┬──────────────────────────┘
                              │
                              ▼
    ┌────────────────────────────────────────────────────┐
    │ On-Device LLM (Azure Foundry Local / WinML `phi`)   │
    └─────────────────────────┬──────────────────────────┘
                              │
                              ▼
    ┌────────────────────────────────────────────────────┐
    │ Executive Strategy & Decision Support Report       │
    └────────────────────────────────────────────────────┘
```

---

## 📚 Academic & Methodological References

1. **Güler, A. (2025).** Türkiye’deki bilişim sistemleri ve teknolojileri bölümlerinin SWARA yöntemi ile ağırlıklandırılması ve COBRA yöntemiyle sıralanması. *Uluslararası Avrasya Sosyal Bilimler Dergisi, 16*(60), 825-840.
2. **Microsoft AI Foundry & Agent Framework:** [Azure AI Foundry Overview](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview)
3. **Microsoft AI For Beginners:** [GitHub AI-For-Beginners](https://microsoft.github.io/AI-For-Beginners/)

---

## 🚀 Quick Start & Local Execution

### Prerequisites
- Python 3.10+
- Windows 10/11 (for native WinML driver acceleration) or CPU fallback

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Aysenuryesilova/E-Commerce-Logistics-AI-Decision-Support-System.git
   cd E-Commerce-Logistics-AI-Decision-Support-System
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Interactive Streamlit Dashboard:**
   ```bash
   streamlit run app.py
   ```

4. **Access the Dashboard:**
   Open browser at `http://localhost:8501`.

---

## 👩‍💻 Author & Contact

**Ayşenur Yeşilova**  
- GitHub: [@Aysenuryesilova](https://github.com/Aysenuryesilova)  
- Project Repository: [E-Commerce-Logistics-AI-Decision-Support-System](https://github.com/Aysenuryesilova/E-Commerce-Logistics-AI-Decision-Support-System)
