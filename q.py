import pandas as pd
import statsmodels.api as sm

# Load user data
users = pd.read_csv('users.csv')
# Load repository data
repos = pd.read_csv('repositories.csv')

# Print the columns in users DataFrame to find the correct user identifier
print("Columns in users DataFrame:", users.columns.tolist())

# Data Cleaning
users['company_clean'] = users['company'].str.replace(r'\b(Inc|LLC|Ltd|Pty|Corp)\b', '', regex=True).str.strip()
users['bio_word_count'] = users['bio'].str.split().str.len().fillna(0).astype(int)

# Convert created_at to datetime
users['created_at'] = pd.to_datetime(users['created_at'], errors='coerce')

# 1. Top 5 Users by Followers
top_users_by_followers = users.nlargest(5, 'followers')['login'].tolist()
print("Top 5 users by followers:", ", ".join(top_users_by_followers))

# 2. 5 Earliest Registered Users
earliest_users = users.nsmallest(5, 'created_at')['login'].tolist()
print("Earliest registered users:", ", ".join(earliest_users))

# 3. Most Popular Licenses
popular_licenses = repos['license_name'].dropna().value_counts().head(3).index.tolist()
print("Most popular licenses:", ", ".join(popular_licenses))

# 4. Majority Company
majority_company = users['company_clean'].mode()[0]
print("Majority company:", majority_company)

# 5. Most Popular Programming Language
most_popular_language = repos['language'].value_counts().idxmax()
print("Most popular programming language:", most_popular_language)

import pandas as pd
import statsmodels.api as sm

# Load user data
users = pd.read_csv('users.csv')
# Load repository data
repos = pd.read_csv('repositories.csv')

# Data Cleaning
users['company_clean'] = users['company'].str.replace(r'\b(Inc|LLC|Ltd|Pty|Corp)\b', '', regex=True).str.strip()
users['bio_word_count'] = users['bio'].fillna('').str.split().str.len()
users['created_at'] = pd.to_datetime(users['created_at'], errors='coerce')

import pandas as pd
import statsmodels.api as sm

# Load user data
users = pd.read_csv('users.csv')
# Load repository data
repos = pd.read_csv('repositories.csv')

# Data Cleaning
users['company_clean'] = users['company'].str.replace(r'\b(Inc|LLC|Ltd|Pty|Corp)\b', '', regex=True).str.strip()
users['bio_word_count'] = users['bio'].fillna('').str.split().str.len()
users['created_at'] = pd.to_datetime(users['created_at'], errors='coerce')

# Check for user identifier column in repos
print("Repositories DataFrame columns:", repos.columns.tolist())

import pandas as pd
import statsmodels.api as sm

# Load user data
users = pd.read_csv('users.csv')
# Load repository data
repos = pd.read_csv('repositories.csv')

# Data Cleaning
users['company_clean'] = users['company'].str.replace(r'\b(Inc|LLC|Ltd|Pty|Corp)\b', '', regex=True).str.strip()
users['bio_word_count'] = users['bio'].fillna('').str.split().str.len()
users['created_at'] = pd.to_datetime(users['created_at'], errors='coerce')

import pandas as pd
import statsmodels.api as sm

# Load user data
users = pd.read_csv('users.csv')
# Load repository data
repos = pd.read_csv('repositories.csv')

# Data Cleaning
users['company_clean'] = users['company'].str.replace(r'\b(Inc|LLC|Ltd|Pty|Corp)\b', '', regex=True).str.strip()
users['bio_word_count'] = users['bio'].fillna('').str.split().str.len()
users['created_at'] = pd.to_datetime(users['created_at'], errors='coerce')

# 6. Second Most Popular Language for Users Joined After 2020
joined_after_2020 = users[users['created_at'] > '2020-01-01']
second_popular_language = repos[repos['login'].isin(joined_after_2020['login'])]['language'].value_counts().nlargest(2).index[-1]

# 7. Language with Highest Average Stars per Repository
average_stars = repos.groupby('language')['stargazers_count'].mean().idxmax()

# 8. Top 5 by Leader Strength
users['leader_strength'] = users['followers'].fillna(0) / (1 + users['following'].fillna(0))
top_leader_strength_users = users.nlargest(5, 'leader_strength')['login'].tolist()

# 9. Correlation Between Followers and Repos
correlation_followers_repos = users['followers'].corr(users['public_repos'].fillna(0))

# 10. Regression Slope of Followers on Repos
valid_data = users[['followers', 'public_repos']].dropna()
X = valid_data['public_repos']
y = valid_data['followers']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
slope_followers_repos = model.params.iloc[1]  # Updated to .iloc

import pandas as pd
import statsmodels.api as sm

# Load user data
users = pd.read_csv('users.csv')
# Load repository data
repos = pd.read_csv('repositories.csv')

# Data Cleaning for users DataFrame
users['bio_word_count'] = users['bio'].fillna('').str.split().str.len()

# 11. Correlation Between Projects and Wiki Enabled
# Convert to int to ensure proper correlation calculation
repos['has_projects'] = repos['has_projects'].astype(int)
repos['has_wiki'] = repos['has_wiki'].astype(int)

# Drop NaN values
correlation_projects_wiki = repos[['has_projects', 'has_wiki']].dropna().corr().iloc[0, 1]

# Print the correlation result formatted to 3 decimal places
print("Correlation between projects and wiki enabled:", f"{correlation_projects_wiki:.3f}")

import pandas as pd
import statsmodels.api as sm

# Load user data
users = pd.read_csv('users.csv')
# Load repository data
repos = pd.read_csv('repositories.csv')

# Data Cleaning
users['company_clean'] = users['company'].str.replace(r'\b(Inc|LLC|Ltd|Pty|Corp)\b', '', regex=True).str.strip()
users['bio_word_count'] = users['bio'].fillna('').str.split().str.len()
users['created_at'] = pd.to_datetime(users['created_at'], errors='coerce')

import pandas as pd
import statsmodels.api as sm

# Load user data
users = pd.read_csv('users.csv')
# Load repository data
repos = pd.read_csv('repositories.csv')

# Data Cleaning for users DataFrame
users['bio_word_count'] = users['bio'].fillna('').str.split().str.len()

# 11. Correlation Between Projects and Wiki Enabled
# Convert to int to ensure proper correlation calculation
repos['has_projects'] = repos['has_projects'].astype(int)
repos['has_wiki'] = repos['has_wiki'].astype(int)

# Drop NaN values
correlation_projects_wiki = repos[['has_projects', 'has_wiki']].dropna().corr().iloc[0, 1]

# Print the correlation result formatted to 3 decimal places
print("Correlation between projects and wiki enabled:", f"{correlation_projects_wiki:.3f}")

# 12. Average Following for Hireable Users
avg_following_hireable = users[users['hireable'] == True]['following'].mean()
avg_following_non_hireable = users[users['hireable'] == False]['following'].mean()
avg_difference_hireable = avg_following_hireable - avg_following_non_hireable

# Print the average difference formatted to 3 decimal places
print("Average following difference for hireable users:", f"{avg_difference_hireable:.3f}")

# 13. Impact of Bio Length on Followers
# Drop users without bios
valid_users = users[users['bio'].notnull()]

# Prepare the data for regression
X_bio = valid_users['bio_word_count']
y_bio = valid_users['followers']

# Add constant for intercept
X_bio = sm.add_constant(X_bio)

# Fit the regression model
model_bio = sm.OLS(y_bio, X_bio).fit()

# Get the regression slope (impact of bio length on followers)
slope_bio_followers = model_bio.params[1]

# Print the regression slope formatted to 3 decimal places
print("Regression slope of followers on bio word count:", f"{slope_bio_followers:.3f}")

# 14. Top 5 Users by Weekend Repository Creation
repos['created_at'] = pd.to_datetime(repos['created_at'])
repos['is_weekend'] = repos['created_at'].dt.dayofweek >= 5
weekend_repos = repos[repos['is_weekend']]
top_users_weekend = weekend_repos['login'].value_counts().head(5).index.tolist()

# 15. Fraction of Hireable Users Sharing Email Addresses
hireable_email_count = users[users['hireable'] == True]['email'].notnull().sum()
hireable_total_count = users[users['hireable'] == True].shape[0]

non_hireable_email_count = users[users['hireable'] == False]['email'].notnull().sum()
non_hireable_total_count = users[users['hireable'] == False].shape[0]

fraction_hireable_email = (
    (hireable_email_count / hireable_total_count if hireable_total_count > 0 else 0) - 
    (non_hireable_email_count / non_hireable_total_count if non_hireable_total_count > 0 else 0)
)

print("Fraction of hireable users with email addresses:", f"{fraction_hireable_email:.3f}")

# 16. Most Common Surname
users['surname'] = users['name'].dropna().str.split().str[-1]
common_surnames = users['surname'].value_counts().nlargest(1).index.tolist()


# Printing Results
print("Second most popular language for users joined after 2020:", second_popular_language)
print("Language with highest average stars per repository:", average_stars)
print("Top 5 users by leader strength:", ", ".join(top_leader_strength_users))
print("Correlation between followers and public repositories:", f"{correlation_followers_repos:.3f}")
print("Regression slope of followers on repos:", f"{slope_followers_repos:.3f}")
print("Correlation between projects and wiki enabled:", f"{correlation_projects_wiki:.3f}")
print("Average following difference for hireable users:", f"{avg_difference_hireable:.3f}")
print("Regression slope of followers on bio word count:", f"{slope_bio_followers:.3f}")
print("Top 5 users by weekend repository creation:", ", ".join(top_users_weekend))
print("Fraction of hireable users with email addresses:", f"{fraction_hireable_email:.3f}")
print("Most common surname:", common_surnames)

import pandas as pd
from sklearn.linear_model import LinearRegression
users_df = pd.read_csv('users.csv')
repos_df = pd.read_csv('repositories.csv')

#Regression slope for followers vs repo counts

follower_count = users_df['followers'].values
repo_counts = users_df['public_repos'].values.reshape(-1, 1)
model = LinearRegression()
model.fit(repo_counts, follower_count)
print("Slope:",model.coef_[0])


#?????????Correlation between projects and wiki enabled
repos_df['has_projects'] = repos_df['has_projects'].map({'TRUE': 1, 'FALSE': 0})
repos_df['has_wiki'] = repos_df['has_wiki'].map({'TRUE': 1, 'FALSE': 0})
print("correlation:",repos_df['has_projects'].corr(repos_df['has_wiki']))


#Regression slope of followers on bio word count
users_df.columns = users_df.columns.str.strip()
users_df = users_df[users_df['bio'].notna()]
users_df['bio_word_count'] = users_df['bio'].str.split().str.len()

follower_count = users_df['followers'].values.reshape(-1, 1)
bio_word_count = users_df['bio_word_count'].values.reshape(-1, 1)

model = LinearRegression()
model.fit(bio_word_count, follower_count)

slope = model.coef_[0][0]
print("slope:", slope)


#created the most repositories on weekends
repos_df['created_at'] = pd.to_datetime(repos_df['created_at'])
repos_df['day_of_week'] = repos_df['created_at'].dt.day_name()
weekend_repos = repos_df[repos_df['day_of_week'].isin(['Saturday', 'Sunday'])]
top_users = weekend_repos['login'].value_counts().head(5).index.tolist()
top_users_logins = ','.join(top_users)
print(top_users_logins)


#correlation between the number of followers and the number of public repositories
correlation = users_df['followers'].corr(users_df['public_repos'])
print(correlation)


#Finding the most common surname
surnames = users_df['name'].dropna().apply(lambda name: name.strip().split()[-1])
surname_counts = {}
for surname in surnames:
    surname_counts[surname] = surname_counts.get(surname, 0) + 1
max_count = max(surname_counts.values())
ans = []
for name in surname_counts.keys():
    if surname_counts[name] == max_count:
        ans.append(name)
print(ans)
