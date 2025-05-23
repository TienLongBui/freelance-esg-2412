import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt

# --- SETUP ---
st.set_page_config(page_title="ESG + Sector Performance", layout="wide")
st.title("🌱 Vietnam Agriculture: ESG & Sector Performance Dashboard")

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["🌿 ESG Overview", "📈 Sector Performance", "Build Your Own ESG"])

# --- ESG TAB (Keep existing visualisation) ---
with tab1:
    st.markdown("""This interactive sunburst chart helps explore the structure of ESG (Environmental, Social, Governance) components.  
                You can filter to focus on specific categories and view insights accordingly.""")

 # --- ADD THIS ---
    uploaded_file = st.file_uploader("📥 Upload your ESG data (CSV or Excel format)", type=['csv','xlsx'])
    
    if uploaded_file:
        if uploaded_file.name.endswith('.csv'):
            data = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            data = pd.read_excel(uploaded_file)
        else:
            st.error("Unsupported file type. Please upload a CSV or Excel file.")

    else:
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
        # Lightbrown for ESG root, Soft yellow for Governance, Soft orange for Social, Soft green for Environment
        'ESG': '#D4B483', 'Governance': '#FFC107', 'Social': '#FFA384', 'Environment': '#8FB98F',
        'Food Security': '#FFE29A', 'Government Regulations': '#FFE29A', 'PPP': '#FFE29A', 'Private Investment': '#FFE29A',
        'High-skilled Labour': '#FFC8B2', 'Community Impact': '#FFC8B2', 'Health & Safety': '#FFC8B2',
        'Resource & Land Use': '#A7DCA7', 'Carbon Credit': '#A7DCA7', 'Eco-farming': '#A7DCA7', 'High-tech Cultivation': '#A7DCA7'
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
        filtered_data, names='labels', parents='parents', values='values', #use filtered_data for selection
        color='labels', color_discrete_map=color_discrete_map
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
    st.plotly_chart(fig, use_container_width=True)

    # Insight button
    if selected_categories:
        with st.expander("📊 ESG Quick Notes"):
            for cat in selected_categories:
                if cat == "Governance":
                    st.markdown("**Governance**: Focuses on transparency, policy compliance, and public-private partnerships.")
                elif cat == "Social":
                    st.markdown("**Social**: Includes community impact, worker conditions, and health & safety measures.")
                elif cat == "Environment":
                    st.markdown("**Environment**: Relates to resource management, carbon credit, and sustainable farming practices.")
        #### Use the below code for synchronize information
        #total = filtered_data[filtered_data['parents'] != ''].groupby('parents')['values'].sum()
        #with st.expander("📊 Quick Insights"):
        #    for cat in selected_categories:
        #        val = total.get(cat, 0)
        #        st.markdown(f"**{cat}** contributes **{val:,}** ESG units.")
    #else:
    #    st.info("No category selected. Showing ESG root only.")

# --- PERFORMANCE TAB ---
with tab2:
    st.markdown("### 📊 Sector Performance (2019–2024)")

    # GDP + Agriculture Growth
    st.markdown("#### 🚀 GDP & Agriculture Growth (World Bank)")
    gdp_data = pd.DataFrame({
        # Manually type in given data
        'Year': [2019, 2020, 2021, 2022, 2023, 2024],
        'GDP Growth': [7.36, 2.87, 2.55, 8.12, 5.05, 7],
        'Agriculture': [2.67, 3.04, 3.27, 3.36, 3.83, 4]
    })
    gdp_long = gdp_data.melt('Year', var_name='Metric', value_name='Value')

    gdp_chart = alt.Chart(gdp_long).mark_line(point=True).encode(
        x='Year:O',
        y='Value',
        color='Metric'
    ).properties(title='Vietnam: GDP vs Agriculture (% YoY)')
    st.altair_chart(gdp_chart, use_container_width=True)

    # Key Export Commodities
    st.markdown("#### 🌾 Export Turnover of Key Commodities (Billion USD)")
    export_data = pd.DataFrame({
        # Manually type in given data
        'Year': [2021, 2022, 2023],
        'Cashew': [3.64, 3.08, 3.63],
        'Coffee': [3.07, 4.06, 4.18],
        'Rice': [3.28, 3.45, 4.78],
        'Peppercorn': [0.94, 0.97, 0.92],
        'Fruit & Vegetable': [3.55, 3.36, 5.69]
    })
    export_long = export_data.melt('Year', var_name='Product', value_name='Export (B USD)')

    fig_exp = px.bar(
        export_long, x='Product', y='Export (B USD)',
        color='Year', barmode='group', title='Agricultural Export Turnover'
    )
    st.plotly_chart(fig_exp, use_container_width=True)

    # KPI Section
    st.markdown("#### 📌 Agriculture KPIs (2023)")
    col1, col2, col3 = st.columns(3)
    col1.metric("🌱 % GDP from Agriculture", "11.96%")
    col2.metric("👩‍🌾 Employment", "13.8 million")
    col3.metric("💸 FDI in Agriculture", "$61.98M")

with tab3:
    st.header("🛠️ Build Your Own ESG Sunburst Structure")

    if 'node_list' not in st.session_state:
        st.session_state.node_list = []

    st.markdown("""
    📝 **How to build your Sunburst Chart:**
    - **Node Label**: Name of the item (e.g., "Governance", "Social")
    - **Parent Node**: Name of the parent (leave blank if it's the root)
    - **Value**: Size or importance (e.g., 300, 5000)

    👉 Example:
    - Label: ESG (Parent: *empty*, Value: 1000)
    - Label: Governance (Parent: ESG, Value: 400)
    - Label: Food Security (Parent: Governance, Value: 150)
    """)
    new_label = st.text_input("Node Label")
    new_parent = st.text_input("Parent Node (leave empty if root)")
    new_value = st.number_input("Value", min_value=0.0, step=10.0)

    if st.button("Add Node"):
        if new_label:  # Check user entered label
            st.session_state.node_list.append({
                'labels': new_label,
                'parents': new_parent,
                'values': new_value
            })
            st.success(f"✅ Added node: {new_label}")
        else:
            st.error("❌ Please enter a label.")

    # Show current structure
    if st.session_state.node_list:
        st.markdown("### 🌿 Current Sunburst Structure:")
        df_nodes = pd.DataFrame(st.session_state.node_list)
        st.dataframe(df_nodes)

        col_reset, col_undo = st.columns(2)
        # Add undo button
        with col_undo:
            if st.button("↩️ Undo Last Step"):
                if st.session_state.node_list:
                    removed_node = st.session_state.node_list.pop()  # Remove last node
                    st.success(f"✅ Removed last node: {removed_node['labels']}")
                else:
                    st.warning("⚠️ No nodes to undo.")
        # Add reset button
        with col_reset:
            if st.button("🔄 Reset Structure"):
                st.session_state.node_list = []
                st.success("✅ Structure has been reset!")
        
        fig = px.sunburst(
            df_nodes,
            names='labels',
            parents='parents',
            values='values'
        )
        fig.update_traces(branchvalues='total')  # Ensure Plotly sunburst chart fills 360 degrees 

        fig.update_layout(title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Start adding nodes to see the chart.")
