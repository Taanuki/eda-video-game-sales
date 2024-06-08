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
