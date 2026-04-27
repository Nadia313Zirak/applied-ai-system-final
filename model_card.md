# 🎧 Model Card: AI Music Taste Assistant

## Model Name
AI Music Taste Assistant (Extended from VibeFinder 1.0)

---

## Goal / Task
This system recommends songs based on a user’s preferences such as mood, genre, energy level, and activity. It predicts which songs a user would enjoy by comparing their taste profile to song features and ranking the closest matches. The system also provides explanations and confidence scores to make recommendations more transparent and reliable.

---

## Data Used
The model uses a small dataset of songs stored in a CSV file. The dataset includes features like genre, mood, energy, tempo, valence, danceability, and acousticness. While I added extra songs to increase variety, the dataset is still limited and does not include important real-world factors such as lyrics, artist popularity, or user listening history.

---

## Algorithm Summary
The system uses a content-based approach. It compares each song to the user’s preferences and assigns a score based on how closely the features match.

- Extra points for matching genre and mood  
- Similarity scoring for energy, valence, danceability, and acousticness  
- Songs are ranked from highest to lowest score  
- The system returns the top recommendations  

In the extended version, the system also:
- Calculates a **confidence score** for each recommendation  
- Labels matches as strong, moderate, or weak  
- Generates explanations describing why a song was recommended  
- Applies guardrails to handle invalid input  

---

## Observed Behavior / Biases
One issue I noticed is that the system can favor certain songs too much based on a few features. For example, high-energy songs may appear frequently if energy is heavily weighted. The system also depends on a small dataset, which limits variety and can cause repeated recommendations.

Because the system does not consider user history or context beyond the current input, it may not reflect real user preferences over time. This can introduce bias toward whatever features are most emphasized in the scoring system.

---

## Evaluation Process
I evaluated the system using an automated test script that runs multiple user profiles, including normal and invalid inputs.

Test cases included:
- Chill studying profile  
- High-energy gym profile  
- Invalid input scenario  

Results:
- Passed 3/3 test cases  
- Successfully handled invalid inputs using guardrails  
- Produced consistent recommendations with explanations and confidence scores  

This evaluation helped confirm that the system works reliably across different scenarios.

---

## Intended Use and Non-Intended Use
This system is intended for learning and experimentation with AI recommendation systems. It demonstrates how user preferences can be transformed into recommendations using structured logic.

It is not intended for real-world deployment because:
- The dataset is too small  
- It does not learn from user behavior  
- It lacks advanced machine learning techniques  

---

## Ideas for Improvement
- Expand the dataset with more songs and features  
- Incorporate user listening history  
- Improve diversity in recommendations  
- Add adaptive learning based on user feedback  
- Use more advanced models such as collaborative filtering  

---

## Personal Reflection
The biggest thing I learned from this project is how a simple system can be extended into a more complete AI system by adding reliability, explanations, and testing. Features like confidence scoring and guardrails made the system more trustworthy and realistic.

Working on this project also showed me that building AI is not just about making something work, but making sure it is understandable and reliable. AI tools were helpful for generating ideas and structure, but I still had to refine and simplify the system to make it effective. This project helped me better understand how real-world recommendation systems balance accuracy, transparency, and user experience.