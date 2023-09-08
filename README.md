![UBC Extended Learning](/img/UBC_EL.png)

# UBC Disney Datasets
> This project attempted to answer the question of which person (actor or director) had the most impact on Disney revenues between 1991 and 2006.  
> This is the final project in the [_UBC Programming in Python for Data Science_](https://extendedlearning.ubc.ca/courses/programming-python-data-science/fs011) course which is part of the [_UBC Key Capabilities in Data Science Certificate Program_](https://extendedlearning.ubc.ca/programs/key-capabilities-data-science). 

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
- "Walt Disney Animation Studios is an American animation studio headquartered in Burbank, California, the original feature film division of The Walt Disney Company. The studio's films are also often called "Disney Classics", or "Disney Animated Canon" [_Wikipedia_](https://en.wikipedia.org/wiki/List_of_Walt_Disney_Animation_Studios_films).
- The datasets for this project were obtained from [_data.world_](https://data.world/kgarrett/disney-character-success-00-16).  


## Technologies Used
![Python](/img/Python.svg)  ![Pandas](/img/Pandas.svg)  ![Jupyter](/img/Jupyter.svg)
- Python - version 3.9
- Pandas - version 2.0.2
- Altair - version 5.0.1


## Features
This project includes a function for converting financial data which is in a string format - **$xxx,xxx** - into either an int or a float.  
The function - ***string_conversion*** is in the ***string_conversion.py*** file.  

## Screenshots

The visualization for the final analysis is captured below.  
![Revenue](/img/Revenue_Chart.png)

## Setup
1. Clone the repo
   ```sh
   git clone https://github.com/djedandyo/ubc-disney.git
   cd ubc-disney
   ```
2. Install project dependencies
   ```sh
   pip install -r requirements.txt
   ```   
3. Run Jupyter Notebook
   ```sh
   jupyter notebook
   ```     


## Usage
This Jupyter Notebook can be used for general inspiration if the user is analyzing the Disney dataset as part of a school project or just for general interest.  
The ***string_conversion*** function can be used as follows.  
```sh
from string_conversion import string_conversion as sc
import pandas as pd
raw = {'vehicle': 
      ['Toyota Highlander', 'Nissan Frontier', 'Ford Fiesta', 
      'Chevy Silverado',  'Porsche Boxster', 'Honda Civic', 'Ford F-150'], 
      'cost': ['$32,777', '$18,899', '$12,344', '$27,555', '$87,566', '
      $21,444', '$45,655'],
      'year': [2012, 2017, 2006, 2002, 2019, 2014, 2018]}
helper_data = pd.DataFrame.from_dict(raw)
res = sc(helper_data, 'cost')
```

## Project Status
This project was the final requirement for the [_UBC Programming in Python for Data Science_](https://extendedlearning.ubc.ca/courses/programming-python-data-science/fs011) course and is complete.  


## Room for Improvement
This is a school project and therefore consists of a very small dataset.  
The main way to improve this project would be to try to get a larger and/or a more recent dataset to see if the analysis conclusions change.

## Acknowledgements
Many thanks to [_UBC Extended Learning_](https://extendedlearning.ubc.ca/programs/key-capabilities-data-science) for providing this course.  


## Contact
Created by Andrew Ostensen [edaostensen@gmail.com](mailto:edaostensen@gmail.com) - feel free to contact me!