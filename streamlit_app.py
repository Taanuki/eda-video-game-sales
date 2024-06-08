import pandas as pd
import streamlit as st
import plotly.express as px

# Load the data
@st.cache_data
def load_data():
    return pd.read_csv('data/combined_data.csv')

data = load_data()

# Ensure 'Copies sold' is numeric and handle any potential issues
data['Copies sold'] = pd.to_numeric(data['Copies sold'].str.replace('[^\d.]', '', regex=True), errors='coerce')
data = data.dropna(subset=['Copies sold'])  # Drop rows where conversion failed

# Streamlit app
st.title('EDA Dashboard')

# Sidebar for user input
st.sidebar.header('User Input')
selected_view = st.sidebar.selectbox(
    'Select a view',
    [
        'Top Developers', 
        'Top Games by Copies Sold', 
        'Yearly Sales', 
        'Genre Spectrum', 
        'Publisher Sales', 
        'Console Sales', 
        'Top Publishers by Genre',
        'Sales Distribution by Year',
        'Platform Popularity',
        'Average Sales per Genre',
        'Top 10 Games by Genre',
        'Games Released Over Time'
    ]
)

# Display the selected view
if selected_view == 'Top Developers':
    st.header('Top Developers')
    developer_counts = data['Developer'].value_counts().reset_index()
    developer_counts.columns = ['Developer', 'Count']
    st.write(developer_counts)

elif selected_view == 'Top Games by Copies Sold':
    st.header('Top Games by Copies Sold')
    top_games = data.groupby('Game', as_index=False)['Copies sold'].sum().nlargest(10, 'Copies sold')
    fig = px.bar(top_games, x='Game', y='Copies sold', title='Top Games by Copies Sold')
    st.plotly_chart(fig)
    st.write(top_games[['Game', 'Copies sold']])

elif selected_view == 'Yearly Sales':
    st.header('Yearly Sales')
    data['Release date'] = pd.to_datetime(data['Release date'])
    data['Year'] = data['Release date'].dt.year
    yearly_sales = data.groupby('Year')['Copies sold'].sum().reset_index()
    fig = px.bar(yearly_sales, x='Year', y='Copies sold', title='Yearly Sales')
    st.plotly_chart(fig)

elif selected_view == 'Genre Spectrum':
    st.header('Genre Spectrum')
    genre_counts = data['Genre'].value_counts().reset_index()
    genre_counts.columns = ['Genre', 'Count']
    fig = px.pie(genre_counts, values='Count', names='Genre', title='Genre Spectrum', 
                 hole=0.3, hover_data=['Count'], labels={'Count':'Number of Games'})
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig)

elif selected_view == 'Publisher Sales':
    st.header('Publisher Sales')
    publisher_sales = data.groupby('Publisher')['Copies sold'].sum().reset_index()
    publisher_sales = publisher_sales.sort_values('Copies sold', ascending=False).head(20)  # Show only top 20 publishers
    fig = px.bar(publisher_sales, x='Copies sold', y='Publisher', title='Publisher Sales', orientation='h')
    st.plotly_chart(fig)

elif selected_view == 'Console Sales':
    st.header('Console Sales')
    console_sales = data.groupby('Console_name')['Copies sold'].sum().reset_index()
    console_sales = console_sales.sort_values('Copies sold', ascending=False)
    fig = px.bar(console_sales, x='Console_name', y='Copies sold', title='Console Sales')
    st.plotly_chart(fig)

elif selected_view == 'Top Publishers by Genre':
    st.header('Top Publishers by Genre')
    genre_publisher = data.groupby(['Genre', 'Publisher'])['Copies sold'].sum().reset_index()
    fig = px.sunburst(genre_publisher, path=['Genre', 'Publisher'], values='Copies sold', title='Top Publishers by Genre')
    st.plotly_chart(fig)

elif selected_view == 'Sales Distribution by Year':
    st.header('Sales Distribution by Year')
    data['Release date'] = pd.to_datetime(data['Release date'])
    data['Year'] = data['Release date'].dt.year
    fig = px.box(data, x='Year', y='Copies sold', title='Sales Distribution by Year')
    st.plotly_chart(fig)

elif selected_view == 'Platform Popularity':
    st.header('Platform Popularity')
    platform_counts = data['Console_name'].value_counts().reset_index()
    platform_counts.columns = ['Console_name', 'Count']
    st.write(platform_counts)

elif selected_view == 'Average Sales per Genre':
    st.header('Average Sales per Genre')
    avg_sales_genre = data.groupby('Genre')['Copies sold'].mean().reset_index()
    fig = px.bar(avg_sales_genre, x='Genre', y='Copies sold', title='Average Sales per Genre')
    st.plotly_chart(fig)

elif selected_view == 'Top 10 Games by Genre':
    st.header('Top 10 Games by Genre')
    selected_genre = st.selectbox('Select Genre', data['Genre'].unique())
    top_games_genre = data[data['Genre'] == selected_genre].nlargest(10, 'Copies sold')
    fig = px.bar(top_games_genre, x='Game', y='Copies sold', title=f'Top 10 Games in {selected_genre}')
    st.plotly_chart(fig)

elif selected_view == 'Games Released Over Time':
    st.header('Games Released Over Time')
    data['Release date'] = pd.to_datetime(data['Release date'])
    data['Year'] = data['Release date'].dt.year
    games_per_year = data['Year'].value_counts().sort_index().reset_index()
    games_per_year.columns = ['Year', 'Number of Games']
    fig = px.line(games_per_year, x='Year', y='Number of Games', title='Games Released Over Time')
    st.plotly_chart(fig)

# Optional: Add more plots and interactivity
