
#libraries
import scipy as sp, pandas as pd, numpy as np

try: 
# Load the data
    nba_data = pd.read_csv('players_stats_by_season_full_details.csv')

except FileNotFoundError:
    print("File not found. Please check the file path.")
    exit()
#1A
#filtering the stage column to only show data for regular season
nba_data =  nba_data[nba_data['Stage'] ==  'Regular_Season'] 
#print(nba_data.columns)
#print(nba_data.head(50))



#1B
#this will get the player with the most seasons which is the focal point of section 1
player_seasons = nba_data.groupby('Player')['Season'].nunique() #grouping by player and counting the number of unique seasons
sort_player = player_seasons.idxmax() #getting the player name with the most seasons
num_seasons = player_seasons.max() #getting the number of seasons the player has played
veteran_player = (sort_player, num_seasons) #creating a tuple with the player name and number of seasons for my sanity
print(veteran_player) #printing the veteran_player tuple

#Vince Carter with 19 seasons

#1C
#Calculating the 3-point accuracy for Vince Carter across the years played.
#accuracy = 3PM / 3PA

veteran_player_data = nba_data[nba_data['Player'] == sort_player] #This will focus on the rows with Carter only.

three_attempted = veteran_player_data['3PA'] #getting the 3PA column
three_made = veteran_player_data['3PM'] #getting the 3PM column

accuracy = three_made / three_attempted #calculating the accuracy
converted_accuracy = accuracy * 100 #converting the accuracy to percentage for the data frame to be more readable

season_accuracy = pd.DataFrame({'Season': veteran_player_data['Season'], 'Accuracy %': converted_accuracy}) #creating a dataframe with the season and accuracy
#print(season_accuracy)

#1D
#Performing linear regression on the 3-point accuracy across the years played by Vince Carter

#since the season is string it will not work with linreg so we split it and int it then grab to values
season_values = veteran_player_data['Season'].str.split(' - ').str[0].astype(int).values
#it was returning an object error initially so this makes sure its an ndarray
accuracy_values = accuracy.values 
#performing linear regression. x = season_values, y = accuracy_values
slope, intercept, r_value, p_value, sd_err = sp.stats.linregress(season_values, accuracy_values) 
#The slope, intercept, r-value, p-value, and standard error are printed

print(f" Slope: {slope}\n Intercept: {intercept}\n R-value: {r_value}\n P-value: {p_value}\n Standard Error: {sd_err}")
"""
The slope shoes that as Carter's career went on his accuracy for 3 pointers decreased. The r val is a negative correlation which adds to the accuracy decreasing 
as his career went on. The p val is significant on the .05 level which means that the relationship between seasons and accuracy is significant. The standard error is
small which means the data is close to the fit line.
"""

#1E
# Calculating the average 3-point accuracy through linear regression for Vince Carter across the years played then comparing it to the actual average 3-point accuracy.
first_season = season_values.min() #getting the first season
last_season = season_values.max() #getting the last season

#integrating the fit line over the played seasons
#using a lambda bc the function is useless elsewhere and is simple.
integrated_accuracy, intg_error = sp.integrate.quad(lambda x: slope * x + intercept, first_season, last_season)

avg_accuracy = integrated_accuracy / (last_season - first_season) #dividing by the number difference in played seasons
#results of the linear regression and actual accuracy
print(f"Average 3-point accuracy: {avg_accuracy} \n error: {intg_error}")
print(f"Actual average 3-point accuracy: {accuracy.mean()}")

"""
The linear regression average accuracy was just a tiny bit higher than the actual average 3-point accuracy.
The error for the linear regression was incredibly small within an acceptable range.
"""

#1F
#Estimating the 3-point accuracy for the missing seasons through interpolation
missing_seasons = [2002, 2015] #missing seasons
estimate_function = sp.interpolate.interp1d(season_values, accuracy_values, kind='linear', fill_value='extrapolate') #interpolating the missing values

# The estimated 3-point accuracy for the missing seasons is printed
estimated_vals = estimate_function(missing_seasons)
#results of the interpolation for 2002, 2015 seasons which do fit the trend of decreasing accuracy
print(f"Estimated 3-point accuracy for 2002: {estimated_vals[0]}\nEstimated 3-point accuracy for 2015: {estimated_vals[1]}")

# Section 2
# This section was a little unclear so I think I am supposed to do the whole NBA dataset and not just Vince Carter.

#2A
FGM_values = nba_data['FGM'].values#field goals made, .values grabs the values from the column as an ndarray
FGA_values = nba_data['FGA'].values #field goals attempted, .values grabs the values from the column as an ndarray

#descriptive statistics for FGM and FGA, uses the .describe function which has all of the requested stats
descriptive_FGM = sp.stats.describe(FGM_values) #descriptive statistics for FGM
descriptive_FGA = sp.stats.describe(FGA_values) #descriptive statistics for FGA
print(descriptive_FGM) #printing the descriptive statistics for FGM
print(descriptive_FGA) #printing the descriptive statistics for FGA

"""
So FGA has a higher mean and way bigger variance than FGM. Both have some right skewing going on with outliers creating a tail on the right side of the distribution. 
Yet since the kurtosis is pretty close to zero the peak is prettu normal. 
"""


#2B

#relational t-test for FGM_values and FGA_values
relational_ttest, rel_pval = sp.stats.ttest_rel(FGM_values, FGA_values) #relational t-test
print(f"Relational t-test: {relational_ttest}, p-value {rel_pval}") #printing the relational t-test

#individual t-test
individual_FGM_ttest, FGM_pval = sp.stats.ttest_1samp(FGM_values, 0) #individual t-test for FGM_values
individual_FGA_ttest, FGA_pval = sp.stats.ttest_1samp(FGA_values, 0) #individual t-test for FGA_values


#results of the individual t-tests
print(f"Individual FGM t-test: statistic={individual_FGM_ttest}, p-value={FGM_pval}")
print(f"Individual FGA t-test: statistic={individual_FGA_ttest}, p-value={FGA_pval}")



"""
I am going to be honest, there is most likely something wrong with the t-tests. 
The p-values are straight zeroes beyond 50 decimal places when I was trying to figure out what was wrong
and could not find a reason because there is no way the p-values are that low. Though the p-values are showing confidence, I am not.

Anyways, the relational and individual t tests are tracking for the same conclusion that FGM and FGA are A) not equal nor close to zero and
B) there is a significant difference between FGM and FGA. Which tracks because FGA is always going to be higher than FGM.
"""