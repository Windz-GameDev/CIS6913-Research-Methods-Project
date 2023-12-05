# Game Development Analysis Project

## Overview

This repository contains a comprehensive analysis focusing on game development, particularly examining the impact of Procedural Content Generation (PCG) and other AI/ML technologies. The project's goal is to explore differences in development time, budget, user satisfaction, and profit between games that utilize PCG and those that do not, emphasizing the role of AI in modern game development.

## Disclaimer

The data in `game_data.csv` is primarily sourced from Wikipedia and publicly available information. Portions of the data, particularly regarding innovation and performance, have been generated using believable estimations facilitated by ChatGPT 4.0. As such, the dataset should be used cautiously and is not suitable as a primary reference for other projects or research.

## Repository Structure
- `Utilizing_Artificial_Intelligence_in_Game_Development__A_Strategy_for_Cost_and_Time_Efficiency___Finished_Paper-1.pdf`: A document detailing the research methodology, literature review, and study findings.
- `game_data.csv`: A CSV file containing the dataset used for analysis, including game development details like time, cost, profit, user satisfaction, and team size.
- `run_analysis.py`: The Python script for conducting statistical analysis and generating visualizations. It includes functions for normality testing, t-test or Mann-Whitney U test based on data distribution, linear regression analysis, and visualization (histograms, bar charts, scatter plots).
- `results/`: A directory containing all the generated visualizations and statistical analysis outputs.
  - `distributions/`: Histograms showing data distribution for each metric.
  - `bar_charts/`: Bar charts illustrating comparisons between PCG and non-PCG games for various metrics.
  - `correlations/`: Scatter plots visualizing correlations between different metrics.

## Visualizations

The script generates insightful visualizations to represent the data analysis:

- Histograms for data distribution of development time, budget, profit, and user satisfaction.
- Bar charts comparing average/median values of development time, budget, profit, and user satisfaction between PCG and non-PCG games.
- Scatterplots show the results of linear regression to ascertain the correlation between key metrics

These visualizations are saved in the `results/` directory, with histograms in `results/distributions/`.

## Getting Started

To use this project:
1. Clone the repository: `git clone https://github.com/Windz-GameDev/CIS6913-Research-Methods-Project`
2. Install required libraries: `pip install pandas matplotlib seaborn scipy`
3. Run the analysis: `python run_analysis.py`

## Usage

The `run_analysis.py` script can be executed with an optional `--include_generated` argument to include or exclude generated data in the analysis:

```bash
python run_analysis.py --include_generated True
```

By default, generated data like performance and innovation scores are excluded.

Refer to the `Utilizing_Artificial_Intelligence_in_Game_Development__A_Strategy_for_Cost_and_Time_Efficiency___Finished_Paper-1` for a comprehensive understanding of the research and findings.

## Contributions

Contributions, suggestions, and feedback are welcome. Feel free to fork the repository, make improvements, and submit a pull request.

## Contact

For inquiries or discussions, please contact n01421643@unf.edu.
