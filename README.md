# Game Development Analysis Project

## Overview
This repository contains a comprehensive analysis focusing on game development, particularly examining the impact of Procedural Content Generation (PCG) and other AI/ML technologies. The project's goal is to explore differences in development time, budget, user satisfaction, and profit between games that utilize PCG and those that do not, emphasizing the role of AI in modern game development.

## Disclaimer
This project is a work in progress. The data in `game_data.csv` is primarily sourced from Wikipedia and publicly available information. Portions of the data, particularly regarding innovation and performance, have been generated using believable estimations facilitated by ChatGPT 4.0. As such, the dataset should be used cautiously and is not yet suitable as a primary reference for other projects or research.

## Repository Structure
- `game_data.csv`: The CSV file with the dataset for analysis, containing details such as development time, cost, profit, and user satisfaction for various games.
- `run_analysis.py`: A Python script for statistical analysis and data visualization. It includes normality testing, choice of statistical tests (t-test or Mann-Whitney U test) based on data distribution, and generating histograms and bar charts.
- `CIS6913 - Aaron Goldstein - Assignment 4 Deliverable.pdf`: A document detailing the research methodology, literature review, and study findings.
- `results/`: Directory containing generated visualizations from the analysis.
    - `distributions/`: Histograms depicting the distribution of data for each metric.
    - Bar charts comparing metrics between PCG and non-PCG games.

## Visualizations
The script generates insightful visualizations to represent the data analysis:
- Histograms for data distribution of development time, budget, profit, and user satisfaction.
- Bar charts comparing average/median values of development time, budget, profit, and user satisfaction between PCG and non-PCG games.

These visualizations are saved in the `results/` directory, with histograms in `results/distributions/`.

## Getting Started
To run the analysis:
1. Clone this repository to your local machine.
2. Ensure Python is installed along with `pandas`, `matplotlib`, `seaborn`, and `scipy`.
3. Execute `run_analysis.py`. The script processes data from `game_data.csv` and saves the results as visualizations in the `results/` directory.

Refer to the `CIS6913 - Aaron Goldstein - Assignment 4 Deliverable.pdf` for a comprehensive understanding of the research and findings.

## Contributions
Contributions, feedback, and suggestions are welcome. Feel free to fork the repository, make changes, and submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE.md).

## Contact
For inquiries or discussions, please contact n01421643@unf.edu.
