# FinTrust ML Engineering — Week 1 Overview

## Project

FinTrust Financial Intelligence & Digital Banking Support Solution

## Track

Machine Learning Engineering

## Week 1 Theme

Understand, Explore, Define and Plan

## Track Role

My role in the Machine Learning Engineering track is to understand the available data and plan how the ML part of the FinTrust solution will be developed and used.

## Week 1 Objectives

The main goal for Week 1 is to understand the project, review the available data, identify possible ML requirements, and plan the workflow for the later stages of the project.

I will also set up the repository structure and document important risks, assumptions, dependencies, and testing requirements.

## Success Criteria

By the end of Week 1, there should be a clear understanding of the ML requirements, the available data, and how the main parts of the ML workflow will fit together.

## Initial Data Exploration

The customer dataset contains 1,500 records and 12 columns. There are no missing values or duplicate rows.

The transaction dataset contains 12,000 records and 11 columns. There are no duplicate transactions, but 96 records have missing `Device_Type` values and 96 have missing `Location` values.

`Monthly_Income` is currently stored as text in the customer dataset, while `Transaction_DateTime` is stored as text in the transaction dataset. These may need to be converted before analysis or modelling.

## Important Project Limitation

The FinTrust datasets and `Risk_Review_Flag` are synthetic and are being used for educational purposes. The risk-review label should not be treated as a real fraud determination or used for actual financial decisions.