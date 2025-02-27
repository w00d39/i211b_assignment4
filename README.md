# NBA Player Statistics Analysis

This program analyzes NBA player statistics from a CSV file and performs various statistical analyses, including linear regression, interpolation, and t-tests. The main focus is on Vince Carter, the player with the most seasons played.

Uses the scipy, pandas, and numpy libraries

## Table of Contents

- [Usage](#usage)
- [Analysis](#analysis)
  - [Section 1](#section-1)
    - [1A: Filter Regular Season Data](#1a-filter-regular-season-data)
    - [1B: Determine Player with Most Seasons](#1b-determine-player-with-most-seasons)
    - [1C: Calculate 3-Point Accuracy](#1c-calculate-3-point-accuracy)
    - [1D: Perform Linear Regression](#1d-perform-linear-regression)
    - [1E: Calculate Average 3-Point Accuracy](#1e-calculate-average-3-point-accuracy)
    - [1F: Estimate Missing Values](#1f-estimate-missing-values)
  - [Section 2](#section-2)
    - [2A: Descriptive Statistics](#2a-descriptive-statistics)
    - [2B: Perform T-Tests](#2b-perform-t-tests)



## Usage

1. Ensure the CSV file [players_stats_by_season_full_details.csv](http://_vscodecontentref_/0) is in the project directory.

2. Run the program

## Analysis

### Section 1

#### 1A: Filter Regular Season Data

The program filters the dataset to include only NBA regular season data.

#### 1B: Determine Player with Most Seasons

The program determines the player who has played the most regular seasons. In this case, it is Vince Carter with 19 seasons.

#### 1C: Calculate 3-Point Accuracy

The program calculates Vince Carter's 3-point accuracy for each season he played.

#### 1D: Perform Linear Regression

The program performs linear regression on Vince Carter's 3-point accuracy across the years played and creates a line of best fit.

#### 1E: Calculate Average 3-Point Accuracy

The program calculates the average 3-point accuracy by integrating the fit line over the played seasons and compares it to the actual average 3-point accuracy.

#### 1F: Estimate Missing Values

The program estimates the 3-point accuracy for the missing 2002-2003 and 2015-2016 seasons using interpolation.

### Section 2

#### 2A: Descriptive Statistics

The program calculates the statistical mean, variance, skew, and kurtosis for the Field Goals Made (FGM) and Field Goals Attempted (FGA) columns for the entire NBA dataset.

#### 2B: Perform T-Tests

The program performs a relational t-test on the FGM and FGA columns and individual t-tests on the FGM and FGA columns.
