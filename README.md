# ESG Sunburst Visualisation App

This is a lightweight Streamlit web application that visualises the ESG (Environmental, Social, Governance) framework using a sunburst chart.  
It is designed as a freelance-style data visualisation demo with quick insights and interactive filtering.

## 📌 Features
- Upload ESG Data in CSV or Excel Format
- Mannual Build your own sunburst structure, then save images
- Undo/Reset button while building your sunburst
- 📊 Interactive sunburst chart with ESG hierarchy
- 🎯 Filter by main categories (Governance, Social, Environment)
- 📈 Auto-generated insights panel
- 🌙 Optimised for dark mode with responsive layout

## 🧪 Built With
- [Streamlit](https://streamlit.io/)
- [Plotly](https://plotly.com/)
- [Pandas](https://pandas.pydata.org/)

## 🚀 Run It Locally
```bash
pip install -r requirements.txt
streamlit run app.py

# If you're on macOS (especially M1 chip), and pip doesn't work:
pip3 install -r requirements.txt
python3 -m streamlit run app.py
```

## Data Requirements (for Upload)
Uploaded file must have **3 columns**
1. labels: *str*
2. parents *str*
3. values: *numeric*

🧠 Use Case
Originally created as a freelance-style task for communicating marketing strategies and sustainability impact. This app makes abstract ESG concepts more digestible with intuitive visuals.

Now it serves as a quick demo for:

- Presenting ESG frameworks interactively
- Visualising sector performance over multiple years
- Letting users build and experiment with hierarchical data structures without coding

🧑‍💻 Author
Bui Tien Long – Data Science @ Monash University
Portfolio: [https://github.com/TienLongBui]
LinkedIn: [https://www.linkedin.com/in/tbui-bib-mds/]

