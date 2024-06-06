# Text Mining Tasks

This repo contains common text mining tasks including: 

* Extracting dates in various formats 
* Extracting social handles, digits, hyperlinks 
* Calculate the average length per row 

## text_mining Module 

### Description: ### 
The text_mining module is a Python package developed as part of this repository. It provides functionalities for text analysis and mining tasks

### Features: ### 
**Average Length Calculation:** The module includes a method to compute the average length of text data in a pandas DataFrame or Series.

**Extract_date:** Extracts dates in various formats from text data using regular expressions. 

![img](doc/date_extraction.png)

**extract_social_handle:** Extract social handle and assign each handle to a copy of its row. Accept a dataframe and its column name as parameter. Returning a dataframe with extracted handles. 

### Notebooks 
Demonstrations and examples of how to use the `textMining` class can be found in the accompanying Jupyter notebook (`text_mining_demo.ipynb`). The notebook showcases various use cases, including text analysis and date extraction tasks, using both DataFrame and Series inputs. 

Please refer to the notebook for detailed explanations and step-by-step instructions on how to utilize the `textMining` class in your projects.






