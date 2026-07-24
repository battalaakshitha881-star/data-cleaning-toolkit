# Data Cleaning Toolkit

A Streamlit app that takes messy tabular data and cleans it up - no code required.

## The problem

Before any analysis or modeling can happen, raw data usually needs cleaning: missing values, duplicate rows, inconsistent formatting, wrong data types. Doing this manually in a notebook every time is repetitive, and not everyone who needs clean data is comfortable writing pandas code.

## What it does

Upload a CSV and the app runs it through a set of cleaning operations - handling missing values, removing duplicates, fixing types - and lets you download the cleaned result, all through a simple interface.

## Tech stack

- **App framework:** Streamlit
- **Data processing:** Pandas

## Live demo

https://data-cleaning-toolkit.streamlit.app

## Setup

```bash
git clone <repo-url>
cd data-cleaning-toolkit
pip install -r requirements.txt
streamlit run app.py
```

## Notes

Add the specific cleaning operations the toolkit supports (e.g. outlier detection, column type inference, custom rules) so this section reflects exactly what's implemented.
