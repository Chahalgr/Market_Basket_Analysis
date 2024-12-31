
# Market Basket Analysis Project

## Overview
This project is a comprehensive **Market Basket Analysis** using Python, aimed at uncovering valuable insights from transactional data. It involves data cleaning, exploratory data analysis (EDA), and the creation of **association rules** to identify patterns in customer purchasing behavior. Visualizations are provided to enhance data interpretation.

## Features
1. **Data Cleaning and Preprocessing**:
   - Removed duplicates and missing values.
   - Converted date and time information for time-based analysis.
   - Reset dataset indices for consistency.

2. **Exploratory Data Analysis (EDA)**:
   - Sales trends visualized by the hour.
   - Distribution of the number of items purchased by customers.
   - Identification of top-selling products.

3. **Market Basket Analysis**:
   - Generated frequent item sets using the Apriori algorithm.
   - Created **association rules** based on metrics such as confidence, support, and lift.

4. **Advanced Visualizations**:
   - Bar chart for top-selling products.
   - Scatter plot for top association rules, illustrating lift, support, and confidence.
   - Heatmap of association rules for easier interpretation.

## Key Insights
- **Sales Trends**: Peak sales hours were identified, enabling better resource allocation during busy times.
- **Customer Behavior**: Most customers purchased a limited range of items, with some outliers buying significantly more.
- **Top Products**: Highlighted products that drive the most sales volume, aiding inventory and marketing decisions.
- **Association Rules**: Discovered valuable item combinations, facilitating cross-selling and promotional strategies.

## Tools and Libraries Used
- **Python**: Core programming language.
- **Pandas**: For data manipulation and cleaning.
- **Matplotlib** and **Seaborn**: For creating insightful visualizations.
- **Mlxtend**: For generating frequent item sets and association rules.
- **Heatmaps and Scatter Plots**: To visualize the relationships and significance of association rules.

## Visualizations

1. Top Selling Products:

![Top Selling Products](images/Screenshot%202024-12-31%20152711.png)

2.Association Rules Scatter Plot:

![Association Rules Scatter Plot](images/Screenshot%202024-12-31%20152725.png)  

3.Lift HeatMap:

![Lift Heatmap](images/Screenshot%202024-12-31%20152742.png)  

## Project Workflow
1. **Load Dataset**: Imported and cleaned the dataset to ensure accuracy and consistency.
2. **EDA**: Explored sales patterns and customer purchasing behavior.
3. **Generate Frequent Item Sets**: Applied the Apriori algorithm to find commonly purchased item combinations.
4. **Association Rules**: Used metrics like lift and confidence to create actionable rules.
5. **Visualize Results**: Leveraged advanced visualizations to present findings effectively.

## Sample Association Rule
- **If a customer buys [Product A], they are 85% likely to also buy [Product B]** with a lift value of 2.5, indicating a strong relationship.

## Future Work
- Incorporate larger datasets for robust analysis.
- Implement real-time recommendations for e-commerce platforms.
- Explore other machine learning techniques to enhance predictive insights.

## Contact
Feel free to reach out for collaboration or questions:  
**Gurleen Singh**  
## Contact
Feel free to connect with me on LinkedIn:  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/-gurleen-singh)

