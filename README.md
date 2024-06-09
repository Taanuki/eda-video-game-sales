# Video Game Sales Analysis

This project is a comprehensive analysis of video game sales data. It aims to explore various aspects of the video game industry, including top-selling games, popular consoles, genre distributions, publisher performance, and more. The project includes data processing, visualization, and an interactive web dashboard using Streamlit.

## Project Description

The project leverages data scraped from Wikipedia's [Lists of best-selling video games by platform](https://en.wikipedia.org/wiki/Lists_of_best-selling_video_games_by_platform). The data is processed and analyzed to generate insights into video game sales trends over the years. The interactive dashboard allows users to explore different aspects of the data and gain valuable insights.

## File Descriptions

- **data/**: Directory containing the dataset.
  - `combined_data.csv`: The main dataset containing video game sales data.

- **notebooks/**: Directory containing Jupyter notebooks used for data analysis and exploration.
  - `New_Final_model (1).ipynb`: The exploratory data analysis (EDA) notebook used for initial data processing and visualization.

- **.devcontainer/**: Directory containing configuration files for VS Code DevContainers.
  - `devcontainer.json`: Configuration file for setting up the development container.

- **streamlit_app.py**: The main script for the Streamlit web dashboard. This script contains the code for loading data, processing it, and creating interactive visualizations.

- **requirements.txt**: List of Python dependencies required to run the Streamlit app.

- **README.md**: This file, providing an overview of the project and its components.

## Interactive Dashboard

An interactive web dashboard has been deployed using Streamlit. You can explore the video game sales data and generate various visualizations using this dashboard. 

Link to the Streamlit Web Dashboard: [EDA Video Game Sales Dashboard](https://eda-video-game-sales-e62yhneguus.streamlit.app/)

## External Resources

- **Web Scraping Source**: [Lists of best-selling video games by platform](https://en.wikipedia.org/wiki/Lists_of_best-selling_video_games_by_platform)
- **Presentation**: [Project Presentation](https://docs.google.com/presentation/d/1GjavJkq9Dl7sl05pipuXQW2MYMZuCOhPyc7Ei-frwSI/edit?usp=sharing)

## Setup and Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/video-game-sales-analysis.git
   cd video-game-sales-analysis


Interactive Features of the EDA Dashboard
Welcome to my EDA Dashboard for Video Game Sales! I've designed this dashboard to provide you with insightful visualizations and a dynamic user experience. Here are the interactive features you can use to explore the data more effectively:

User Input Sidebar
-Select a View: I can choose from a variety of views to analyze different aspects of the video game sales data. Options include Top Developers, Top Games by Copies Sold, Yearly Sales, Genre Spectrum, Publisher Sales, Console Sales, and more.
-Search for a Game or Developer: I can use this text input box to filter the data by specific games or developers. Simply type in the name or partial name, and the dashboard will update to show relevant results.
-Exclude Publisher Data: This checkbox allows me to exclude publisher information from the visualizations if I prefer to focus on other data aspects.
-Select Genres: I can use the multiselect box to filter data by one or more genres. I can select specific genres that interest me. Additionally, there's a "Select All Genres" checkbox that, when selected, automatically includes all genres in the analysis.


Main Dashboard Area
-Top Developers: I can view a list of the top game developers based on the number of games they have developed.
-Top Games by Copies Sold: I can explore the top-selling games with an adjustable slider to control the number of games displayed.
-Yearly Sales: I can analyze yearly sales trends with bar charts, helping me identify peaks and patterns over the years.
-Genre Spectrum: I can visualize the distribution of game genres with an interactive pie chart, providing a clear view of the most popular genres.
-Publisher Sales: I can examine sales data of the top publishers, with a slider to adjust the number of top publishers displayed.
-Console Sales: I can see which consoles have sold the most games with a detailed bar chart.
-Top Publishers by Genre: I can discover the leading publishers in each genre with a sunburst chart.
-Sales Distribution by Year: I can understand the spread of sales data over the years using a box plot.
-Platform Popularity: I can review the popularity of different gaming platforms.
-Average Sales per Genre: I can view the average sales per genre with a bar chart.
-Top 10 Games by Genre: I can select a genre to see the top 10 games within that genre.
-Games Released Over Time: I can track the number of games released each year with a line chart.
-Console Library: I can select a console to view detailed information about the games available for that platform.
Search for a Game or Developer:

Type: Text Input
Explanation: Allows users to filter the data by typing in the name of a specific game or developer. This helps in quickly finding relevant information without manually browsing through the entire dataset.
Exclude Publisher Data:

Type: Checkbox
Explanation: Gives users the option to exclude publisher information from the visualizations. This is useful if the focus is on other aspects of the data, such as game sales or genres.
Select All Genres:

Type: Checkbox with Multiselect
Explanation: Provides a checkbox to select all genres at once, along with a multiselect dropdown to choose specific genres. This feature makes it easier to filter data by multiple genres without having to select each one individually.
Top Games by Copies Sold - Number of Games to Display:

Type: Slider
Explanation: Allows users to adjust the number of top games displayed in the visualization. Users can slide to select a specific number of games, ranging from 5 to 50, making it easy to view the top N games by copies sold.
Top Publishers by Sales - Number of Publishers to Display:

Type: Slider
Explanation: Lets users control the number of top publishers displayed in the visualization. The slider ranges from 5 to 50, enabling users to focus on the top publishers by sales.
Download CSV:

Type: Download Button
Explanation: Allows users to download the filtered dataset in CSV format for further analysis. This is especially useful for users who want to perform additional analysis or keep a record of the filtered data.
These interactive options, including the sliders, enhance the usability of the dashboard by allowing users to tailor the data visualization to their specific needs and preferences.

Download Filtered Data
Download CSV: After applying filters and adjustments, I can download the filtered dataset in CSV format for further analysis. This feature is available in the sidebar under "Download Filtered Data."


I hope these interactive features enhance your experience and provide valuable insights into the video game sales data. Happy exploring!
