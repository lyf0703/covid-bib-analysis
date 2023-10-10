# covid-bib-analysis

This repository contains data and analysis related to the study on interdisciplinary integration in COVID-19 research. The research focuses on understanding the patterns of collaboration and integration among different disciplines in the context of the COVID-19 pandemic response. The analysis utilizes social network analysis techniques to uncover the relationships and trends in interdisciplinary research.

Data Description
The dataset includes three main components:

1. Basic Literature Information: This dataset contains essential information about the literature, including title, authors, publication date, journal, and DOI.
2. Scival Topic Data: This dataset provides topic information derived from Scival analysis. It encompasses the evolving research interests and trends in COVID-19 research across various disciplines.
3. Literature Disciplinary Categorization: This dataset assigns each literature entry to specific disciplinary categories. It offers insights into the interdisciplinary nature of COVID-19 research and the integration among different academic fields.

Please note that due to limitations in data collection (for example some literature does not include info about Scival Topic or disciplinary category info or both), there may be some missing entries in the Scival Topic and literature disciplinary categorization datasets. Therefore, the number of entries in these datasets might be relatively smaller compared to the basic literature information dataset.

Repository Contents
basic info/: This directory contains the datasets of essential information about the literature.
scival topic/: This directory includes the datasets of topic information (Scival Topic).
disciplinary/: This directory contains literature disciplinary categorization info.
Code/SNA.ipynb: An interactive Jupyter notebook for data processing and preliminary analysis.
Code/subjectCrawler.py: Python script to fetch the disciplines associated with literature.
Code/csvDeduplicate.py: Python script for merging files and deduplication.
Code/scivalTopicCrawler.py: Python script to fetch topics associated with the literature.
Graph/SNA Graph.gephi: Visualization and calculation using social network analysis.

License
This project is licensed under the MIT License.