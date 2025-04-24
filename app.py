import streamlit as st
import plotly.express as px
import pandas as pd

# Title
st.set_page_config(page_title="ESG Sunburst App", layout="wide")
st.title("🌿 ESG Sunburst Visualisation App")
st.markdown("""
This interactive sunburst chart helps explore the structure of ESG (Environmental, Social, Governance) components.  
You can filter to focus on specific categories and view insights accordingly.
""")

# Static ESG data
data = pd.DataFrame({
    'labels': [
        'ESG', 'Governance', 'Social', 'Environment',
        'Food Security', 'Government Regulations', 'PPP', 'Private Investment',
        'High-skilled Labour', 'Community Impact', 'Health & Safety',
        'Resource & Land Use', 'Carbon Credit', 'Eco-farming', 'High-tech Cultivation'
    ],
    'parents': [
        '', 'ESG', 'ESG', 'ESG',
        'Governance', 'Governance', 'Governance', 'Governance',
        'Social', 'Social', 'Social',
        'Environment', 'Environment', 'Environment', 'Environment'
    ],
    'values': [
        200, 3800, 3800, 3800,
        28000, 28000, 28000, 28000,
        37000, 37000, 37000,
        28000, 28000, 28000, 28000
    ]
})

# Color mapping
color_discrete_map = {
    'ESG': '#D4B483', # Light brown for ESG root
    'Governance': '#FFC107', # Soft yellow for Governance
    'Social': '#FFA384', # Soft orange for Social
    'Environment': '#8FB98F', # Soft green for Environment
    # Governance subcategories
    'Food Security': '#FFE29A',
    'Government Regulations': '#FFE29A',
    'PPP': '#FFE29A',
    'Private Investment': '#FFE29A',
    # Social subcategories
    'High-skilled Labour': '#FFC8B2',
    'Community Impact': '#FFC8B2',
    'Health & Safety': '#FFC8B2',
    # Environment subcategories
    'Resource & Land Use': '#A7DCA7',
    'Carbon Credit': '#A7DCA7',
    'Eco-farming': '#A7DCA7',
    'High-tech Cultivation': '#A7DCA7'
}

# Filter option
selected_categories = st.multiselect(
    "Filter ESG components:", 
    ['Governance', 'Social', 'Environment'], 
    default=['Governance', 'Social', 'Environment']
)

# Filtered data
if selected_categories:
    filtered_data = data[
        (data['labels'].isin(selected_categories)) |
        (data['parents'].isin(selected_categories)) |
        (data['labels'] == 'ESG')
    ]
else:
    filtered_data = data[data['labels'] == 'ESG']

# Create sunburst chart
fig = px.sunburst(
    filtered_data,
    names='labels',
    parents='parents',
    values='values',
    color='labels',
    color_discrete_map=color_discrete_map,
)

fig.update_layout(
    # Title Alignment into the middle
    title={
        'text': "ESG Scores Sunburst Chart",
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    title_text='ESG Scores Sunburst Chart',
    title_font=dict(size=20, family='Trebuchet MS', color='white'),
    font=dict(size=14, family='Trebuchet MS'),
    paper_bgcolor='rgba(0,0,0,0)',  # transparent to match dark mode
    plot_bgcolor='rgba(0,0,0,0)',
    margin=dict(t=50, l=0, r=0, b=50),
    title_x=0.5,
)
fig.update_traces(
    hovertemplate='<b>%{label}</b><br>Category: %{parent}<extra></extra>'
)

# Show chart
st.plotly_chart(fig, use_container_width=True, height=700)
# Add padding so Quick Insight does not fall too far down
#st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

# Insight
if selected_categories:
    total = filtered_data[filtered_data['parents'] != ''].groupby('parents')['values'].sum()
    with st.expander("📊 Quick Insights"):
        for cat in selected_categories:
            val = total.get(cat, 0)
            st.markdown(f"**{cat}** contributes **{val:,}** ESG units.")
else:
    st.info("No category selected. Showing ESG root only.")
