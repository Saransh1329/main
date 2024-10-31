# GitHub User Data Analysis Project
This project focuses on the analysis of GitHub users based in Paris with more than 100 followers, aiming to extract valuable insights about their profiles and contributions.

## Project Overview
The objective of this analysis is to understand the developer landscape in Paris, identify trends in open-source contributions, and provide actionable insights for developers to enhance their GitHub profiles.

## Data Collection Process
Data was collected using the GitHub API, a powerful tool that allows developers to access public GitHub data programmatically. Here’s a step-by-step breakdown of the data collection process:
1. **API Authentication**: 
   - An access token was used to authenticate requests to the GitHub API, ensuring that the requests are allowed and adhering to GitHub's rate limits.
2. **User Search Parameters**: 
   - The primary query used to find users was `location:Paris followers:>100`, broken down by programming languages to increase the number of fetched users.
3. **User Details Retrieval**: 
   - For each user fetched, additional details such as their name, company, location, bio, public repositories count, and follower count were extracted using the `GET /users/{username}` endpoint.
4. **Repository Data Collection**: 
   - For each user, their repositories were retrieved through the `GET /users/{username}/repos` endpoint, including details like repository name, creation date, star count, and programming language used.
5. **Data Cleaning and Storage**: 
   - Collected data was cleaned by removing duplicates and irrelevant entries. Each dataset was saved into CSV files, allowing for easy analysis later.

## Key Findings
- **Community Engagement**: The analysis showed that a substantial number of users actively contribute to open-source projects, reflecting a vibrant developer community in Paris.
- **Popular Technologies**: Languages like JavaScript, Python, and Ruby were frequently used in the repositories, suggesting a trend towards these technologies in the local developer ecosystem.
- **Profile Completeness**: Some profiles had minimal information, indicating opportunities for users to enhance their visibility and attractiveness to collaborators or employers.
