# Exploratory Data Analysis Project using a Customer Loan Database
In this project, Exploratory Data Analysis (EDA) is done on a database which contains data pertaining to loans customers have taken out.

## Table of contents
1. [Aim of the project](#aim-of-the-project)
2. [What I have learned](#what-i-have-learned)
3. [File Structure](#file-structure)
4. [Usage instructions/classes/main.ipynb](#usage-instructionsclassesmainipynb)
5. [CSV Files](#csv-files)
6. [Others](#others)
7. [Limitations](#limitations)

## Aim of the project
To analyze a very robust database of loan customers by first making a number of classes to make this task easier, followed by transforming the data to eliminate outliers, null values, skewness, and making sure the data is ready for analysis. Finally, analysis takes place to observe different trends through graphs and calculations. A few examples of this: visualizing the state of the loans and projected profits, seeing losses due to charged-off loans and exploring potential predictors that may indicate losses. 

## What I have learned
- Each class I wrote taught me different aspects of data analysis but it was once I was doing the transformation and analysis where I have learned the most as I had to modify and troubleshoot what I had written in the classes going ahead
- Writing the RDSDatabaseConnector was quite challenging initially as I had the least familiarity with this, however, once this was done it was very much straightforward for me to understand the uses.
- Once the transformation part commenced (milestone 2) I quickly learned how, for example, the changes on the data types do not change to the CSV file directly, for example. But other than that, most of this part was very much straightforward. I did learn the importance of datetime types as the calculations using these are very useful for data analysis. 
- In terms of removing the NULLS and doing the imputations and removal, a lot of common sense had come forward in this part, and decisions as to what columns or rows to take out do not have a prescribed method similar to a lot of the steps going forward, however, here was the first time to notice this. 
- When it came to plotting I found writing this code challenging and I found myself needing to do a lot of tweaking to have the best image as possible as I was doing this. However, I found it very useful for decision-making when seeing numbers only sometimes it's insufficient to make decisions. 
- When it came to the actual analysis part post-transformation. I found this a little easier due to my background in Finance to do calculations to understand the data. And observing this through plots that I had already had some experience in the previous part. 
- Lastly, I recognized too that in a lot of these sections more complex transformations and analysis could have been done and although I did do some research on this, it was beyond the scope of this task, nonetheless I am very excited to keep learning and going forward to have even better and more robust results.  

## File Structure
- db_utils.py - class RDSDatabaseConnector
- data_transform_class.py - class DataTransform
- data_frame_info.py - class DataFrameInfo
- plotter_class.py - class Plotter
- data
    - loan_payments_whole.csv
    - updated_2_loan_payments.csv
    - updated_3_loan_payments.csv
    - updated_4_loan_payments.csv
    - updated_loan_payments.csv
- .gitignore
- main.ipynb

## Usage instructions/classes/main.ipynb
- Here is where all the classes are implemented to first transform our data utilizing various methods, followed by a short analysis section.
- The notebook contains comments describing what is being done at each stage
- Each class contains docstrings which explain each method thoroughly 

## CSV Files
- loan_payments_whole.csv - initial file downloaded using the credentials and RDSConnector. It is a loan customer database. You can use the DataFrameInfo class for more details on this file. 
- updated_loan_payments.csv - first update containing changes such as: eliminations of nulls through imputation and carefully selecting columns and rows to drop. Details on the notebook file. This is the file used for milestone 4 analysis. 
- updated_2_loan_payments.csv - update where the skew is corrected
- updated_3_loan_payments.csv - update where the outliers are eliminated 
- updated_4_loans_payments.csv - update where highly correlated columns are dropped

## Others
- This part highlights the other files that fall into the previous categories 
- README.md: the file containing information regarding the project describing the aims, what I have learned, Usage instructions, classes, csv files, others and limitations
- credentials.yaml contains our credentials of the database we are going to be using these in .gitignore so for data protection purposes

## Limitations
- The main limitation the time I had to execute this project considering my level of experience
- As I did this project as learning I recognize that there are sections that could be improved upon. 
- A few examples are: 
    - More of the data transform methods could be modified to allow you to accept lists to make the process simpler,
    - More complex machine learning techniques could have been applied for the imputation and transformations regarding the skew. 
    - On milestone 4, more in-depth analysis could have been done in the last task looking at reasons indicators of that customers might not be able to pay their loan, for example using further columns, payment_plan and interest_rate for example. 
    - Furthermore, the 'the projected loss over the remaining term' plot could be clearer using techniques such as aggregation or the use of groupby