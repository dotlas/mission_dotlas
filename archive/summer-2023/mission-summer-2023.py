# Databricks notebook source
# MAGIC %md
# MAGIC # Mission Dotlas 🌎 [85 points]
# MAGIC
# MAGIC > `v2.0` Updated: April 19 2023 (Spring + Summer 2023 Version)
# MAGIC
# MAGIC ![Dotlas](https://camo.githubusercontent.com/6a3a3a9e55ce6b5c4305badbdc68c0d5f11b360b11e3fa7b93c822d637166090/68747470733a2f2f646f746c61732d776562736974652e73332e65752d776573742d312e616d617a6f6e6177732e636f6d2f696d616765732f6769746875622f62616e6e65722e706e67)
# MAGIC
# MAGIC ## Section 1: Project Overview ✉️
# MAGIC
# MAGIC Welcome to your mission! In this notebook, you will download a dataset containing restaurants' information in the state of California, US. The dataset will then be transformed, processed and prepared in a required format. This clean dataset will then be used to answer some analytical questions and create a few data visualizations in Python.
# MAGIC
# MAGIC This is a template notebook that has some code already filled-in to help you on your way. There are also cells that require you to fill in the python code to solve specific problems. There are sections of the notebook that contain a points tally for code written. 
# MAGIC
# MAGIC **Each section of this notebook is largely independent, so if you get stuck on a problem you can always move on to the next one.**

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1.1 Tools & Technologies 🪛
# MAGIC
# MAGIC - This exercise will be carried out using the [Python](https://www.python.org/) programming language and will rely hevily on the [Pandas](https://pandas.pydata.org/) library for data manipulation.
# MAGIC - You may use any of [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/) or [Plotly](https://plotly.com/python/) packages for data visualization.
# MAGIC - We will be using [Jupyter notebooks](https://jupyter.org/) to run Python code in order to view and interact better with our data and visualizations.
# MAGIC - You are free to use [Google Colab](https://colab.research.google.com/) which provides an easy-to-use Jupyter interface.
# MAGIC - When not in Colab, it is recommended to run this Jupyter Notebook within an [Anaconda](https://continuum.io/) environment
# MAGIC - You can use any other Python packages that you deem fit for this project.
# MAGIC
# MAGIC > ⚠ **Ensure that your Python version is 3.9 or higher**
# MAGIC
# MAGIC ![](https://upload.wikimedia.org/wikipedia/commons/1/1b/Blue_Python_3.9_Shield_Badge.svg)
# MAGIC
# MAGIC **Language**
# MAGIC
# MAGIC ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
# MAGIC
# MAGIC **Environments & Packages**
# MAGIC
# MAGIC ![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white)
# MAGIC ![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
# MAGIC ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
# MAGIC ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
# MAGIC ![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)
# MAGIC
# MAGIC **Data Store**
# MAGIC
# MAGIC ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
# MAGIC
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC ## Section 2: Data Overview 🔍 [10 points]
# MAGIC
# MAGIC ### 2.1 Read California Dataset 🚰 [1 point]
# MAGIC
# MAGIC In this section, we will load the dataset from [AWS](https://googlethatforyou.com?q=amazon%20web%20services) S3, conduct an exploratory data analysis and then clean up the dataset
# MAGIC
# MAGIC
# MAGIC - Ensure that pandas and plotly are installed (possibly via pip or poetry)
# MAGIC - The dataset is about 300 MB in size and time-to-download depends on internet speed and availability
# MAGIC - Download the dataset using Python into this notebook and load it into a pandas dataframe (without writing to file)
# MAGIC

# COMMAND ----------

from matplotlib import pyplot as plt

%matplotlib inline

import pandas as pd
import plotly.express as px
import numpy as np

CELL_HEIGHT: int = 50

# Initialize helpers to ignore pandas warnings and resize columns and cells
pd.set_option("chained_assignment", None)
pd.set_option("display.max_rows", 50)
pd.set_option("display.max_columns", 500)
pd.set_option("display.max_colwidth", CELL_HEIGHT)

DATA_URL: str = (
    "https://dotlas-marketing.s3.amazonaws.com/interviews/california_restaurants.json"
)

# COMMAND ----------

# MAGIC %%time
# MAGIC # ✏️ YOUR CODE HERE
# MAGIC # df: pd.DataFrame = ?

# COMMAND ----------

# MAGIC %md
# MAGIC The following cell creates a `restaurant ID` column to uniquely index each restaurant. Run it as is.

# COMMAND ----------

df["restaurant_id"] = range(1, len(df) + 1)
df.head()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2.2 Data Overview 🌍 [9 points]
# MAGIC Inspect the data to understand what you are dealing with, including summary statistics as well as its structure and identify potential issues that need fixing.

# COMMAND ----------

# ✏️ YOUR CODE HERE

# COMMAND ----------

# MAGIC %md
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC ## Section 3: Data Preprocessing 🕵🏼‍♀️ [25 points]
# MAGIC
# MAGIC <img src="https://media.giphy.com/media/hbd8nlok7kqnS/giphy.gif" height="250px" width="250px" alt="simpsons">
# MAGIC
# MAGIC
# MAGIC In this exercise, you will be preprocessing the data. It will involve cleaning the data, transforming it into a suitable format, and handling missing values and outliers. These steps are crucial to ensure the quality and reliability of the data before applying statistical learning models.
# MAGIC
# MAGIC > 📝 Your work will be assessed based on how systematic and complete your transformations are i.e, if they perform the task generally across all data points, and yield the expected output. 

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3.1 Missing Values ❓ [5 Points]
# MAGIC
# MAGIC Identify and handle missing values in the dataset. If a value is missing, decide whether to fill it in with an appropriate default value, remove the row, or simply let it be.

# COMMAND ----------

# ✏️ YOUR CODE HERE

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3.2 Phoning it in 📞 [5 Points]
# MAGIC
# MAGIC Standardize the format of the ```'phone_number'``` column by removing any non-numeric characters and ensuring that all phone numbers have the same length.

# COMMAND ----------

# ✏️ YOUR CODE HERE

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3.3 No more HTML 📄 [5 Points]
# MAGIC Find columns containing HTML tags and replace them with an appropriate plain text equivalent, such as a newline character or space.
# MAGIC
# MAGIC ex:
# MAGIC
# MAGIC ```html
# MAGIC <p>
# MAGIC   Feast on delicious grub at Jerry's Famous Deli.<br />
# MAGIC   Its retro-style casual setting features comfortable booth seating.
# MAGIC </p>
# MAGIC ```
# MAGIC
# MAGIC to:
# MAGIC
# MAGIC ```
# MAGIC Feast on delicious grub at Jerry's Famous Deli. Its retro-style casual setting features comfortable booth seating.
# MAGIC ```

# COMMAND ----------

# ✏️ YOUR CODE HERE

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3.4 Safety Precautions 🦺 [5 Points]
# MAGIC
# MAGIC Transform the entire safety precautions column into a new column based on the following rule:
# MAGIC
# MAGIC Convert from `dictionary` to `list`. Only include in the list, those keys in the dictionary which are `true`.
# MAGIC For ex, for safety precautions of the type:
# MAGIC
# MAGIC ```python
# MAGIC {
# MAGIC     'cleanMenus': True,
# MAGIC     'limitedSeating': False,
# MAGIC     'sealedUtensils': None,
# MAGIC     'prohibitSickStaff': True,
# MAGIC     'requireDinerMasks': True,
# MAGIC     'staffIsVaccinated': None,
# MAGIC     'proofOfVaccinationRequired': False,
# MAGIC     'sanitizerProvidedForCustomers': None
# MAGIC }
# MAGIC ```
# MAGIC
# MAGIC It should turn into a list of the form:
# MAGIC
# MAGIC ```python
# MAGIC ["Clean Menus", "Prohibit Sick Staff", "Require Diner Masks"]
# MAGIC ```
# MAGIC

# COMMAND ----------

# ✏️ YOUR CODE HERE

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3.5 Imputing Exercise 📈 [5 Points]
# MAGIC
# MAGIC Fill up missing values for rating, rating count and review count by imputing based on the following columns in order:
# MAGIC
# MAGIC 1. `brand_name`
# MAGIC 2. `area`
# MAGIC 3. `city`
# MAGIC
# MAGIC This means that if `rating` is missing for a restaurant (null / 0), but that restaurant is part of a brand where
# MAGIC other restaurants of the same brand have ratings, then a median rating is taken. If brands are complete, then missing values are filled using
# MAGIC area where the restaurant is located (median rating) and finally filled using the city's rating
# MAGIC
# MAGIC Here's an example:
# MAGIC
# MAGIC |restaurant_id	|brand_name|	area|	city|	rating|	imputed_rating_brand | imputed_rating_area| imputed_rating_city
# MAGIC | --- | --- | --- | --- | --- | --- | --- | --- |
# MAGIC |1	|X1|	A1|	B1|	3|	3| 3 | 3 |
# MAGIC |2	|X1|	A1|	B1|	2|	2| 2 | 2 |
# MAGIC |3	|X1|	A1|	B1|	| 2.5| 2.5 | 2.5 |
# MAGIC |4	|X2|	A1|	B1|	4|	4 | 4 | 4 |
# MAGIC |5	|X3|	A1|	B1|	|	 | 2.75 | 2.75 |
# MAGIC |6	|X4|	A4|	B2|	|	 | | 3 |
# MAGIC |7	|X5|	A6|	B2|	2|	 2| 2| 2|
# MAGIC |8	|X6|	A7|	B2|	4|	 4| 4| 4 |
# MAGIC

# COMMAND ----------

# ✏️ YOUR CODE HERE

# COMMAND ----------

# MAGIC %md
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC Remember to hydrate and 
# MAGIC
# MAGIC [![Spotify](https://img.shields.io/badge/Spotify-1ED760?style=for-the-badge&logo=spotify&logoColor=white)](https://open.spotify.com/playlist/3d4bU6GAelt3YL2L1X2SOn)
# MAGIC
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC ## Section 4: Non-Trivial Transformations Exercise 🤺 [20 points]

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4.1 Menu-Level Table 🧾 [20 points]
# MAGIC
# MAGIC <img src="https://media.giphy.com/media/qpLuA97QGOsnK/giphy.gif" height="250px" width="250px" alt="ratatouille">
# MAGIC
# MAGIC **Create a menu-level table by parsing out menu items from the `menu` column per restaurant.**
# MAGIC
# MAGIC Every restaurant has a `menu` column that contains deeply nested JSON data on the restaurant's menu. The hierarchy is as follows: 
# MAGIC
# MAGIC * One restaurant can have multiple menus (morning menu, evening menu, etc.)
# MAGIC     * Each menu can have a description and provider
# MAGIC * Each restaurant menu can have multiple sections (such as Appetizers, Desserts, etc.)
# MAGIC     * Each section has a description
# MAGIC * Each section can have multiple menu items (such as Latte, Apple Pie, Carrot Halwa, etc.)
# MAGIC     * Each menu item has a price, currency and description
# MAGIC
# MAGIC You need to parse out the menu data from the JSON in the `menu` column for each restaurant and have a restaurants x menu table as shown below. 
# MAGIC
# MAGIC | restaurant_id | menu_name | menu_description | menu_provider | section_name | section_description | item_name          | item_description                                                                                                      | item_price | item_price_currency |
# MAGIC | ------------: | :-------- | :--------------- | ------------: | :----------- | :------------------ | :----------------- | :-------------------------------------------------------------------------------------------------------------------- | ---------: | :------------------ |
# MAGIC |             1 | Main Menu |                  |           nan | Appetizers   |                     | Egg Rolls          | Deep fried mixed veggie egg rolls served with sweet & sour sauce                                                      |          8 | USD                 |
# MAGIC |             1 | Main Menu |                  |           nan | Appetizers   |                     | Fried Tofu         | (Contains Peanut) Deep fried tofu, served with sweet & sour sauce and crushed peanut                                  |          8 | USD                 |
# MAGIC |             1 | Main Menu |                  |           nan | Appetizers   |                     | Fried Meat Balls   | Deep fried fish, pork, beef balls or mixed served with sweet & sour sauce. Meat: Beef $1, Fish, Mixed Meat ball, Pork |        8.5 | USD                 |
# MAGIC |             1 | Main Menu |                  |           nan | Appetizers   |                     | Pork Jerky         | Deep fried marinated pork served with special jaew sauce                                                              |        8.5 | USD                 |
# MAGIC |             1 | Main Menu |                  |           nan | Appetizers   |                     | Thai Isaan Sausage | (Contains Peanut) Thai Style sausage served with fresh vegetables and peanuts                                         |          9 | USD                 |
# MAGIC
# MAGIC
# MAGIC > 📝 Your work will be assessed based on how maintainable your code is, if it logically and systematically performs the transformations, and is highly performant. You will be penalized on data quality metrics and if there are any bugs in the intermediate transformations that leads to final erroneous values.

# COMMAND ----------

# ✏️ YOUR CODE HERE

# COMMAND ----------

# MAGIC %md
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC ## Section 5: Exploratory Data Analysis 🕵🏼‍♀️ [30 points]
# MAGIC
# MAGIC In this exercise, **you will be conducting your own open-ended exploratory data analysis (EDA) of the dataset to gain insights and prepare the data for further analysis**. The EDA will involve understanding the structure of the data, checking for missing values, outliers, and correlations, and identifying trends or patterns. 
# MAGIC
# MAGIC We know how much fun it is to create all sorts of funky visualizations and crunch numbers all day long. But let's not forget why we're doing this - we want to tell a story about our data! So, while it's great to have fun with your data, let's make sure we're doing it in a systematic and purposeful way. Each visualization and exploration should show progress in understanding the data better and contribute to telling the story of our data. So let's put on our exploration hats and approach every chart and graph with a clear question in mind. By doing this, we'll uncover exciting insights and tell an engaging story about our data that even your grandma will want to hear.
# MAGIC
# MAGIC > 📝 Your work will be assessed based on the quality of your visualizations, the funnels employed to transform data-driven questions into insights, and your interpretation of the generated results.

# COMMAND ----------

# ✏️ YOUR CODE HERE

# COMMAND ----------

# MAGIC %md
# MAGIC ---
# MAGIC
# MAGIC Good job!
# MAGIC
# MAGIC <img src="https://media.giphy.com/media/qLhxN7Rp3PI8E/giphy.gif" height="250px" width="250px" alt="legend of zelda">
