# Major Explorer 

A beginner-friendly Python project that recommends a suitable university major based on the user's interests and preferences.

## About the Project

Major Explorer is an interactive Python project created as part of my Python 101 learning journey.

The program asks the user 16 Yes/No questions about different interests related to four majors:

- Artificial Intelligence
- Cybersecurity
- Computer Science
- Information Systems

Each `Yes` answer adds one point to the related major. After all questions are answered, the program compares the scores and recommends the major with the highest score.

If two or more majors have the same highest score, the program displays a tie message.

## Majors and Properties

**Artificial Intelligence:** Math & Logic, Smart Systems, Machine Learning, Data Analysis

**Cybersecurity:** Information Security, Vulnerability Detection, Network Security, Security Investigation

**Computer Science:** Programming, Problem Solving, Algorithms, Computer Systems

**Information Systems:** Business Technology, Business Analysis, Information Management, Technology & Business

## How It Works

The program stores the majors and their properties in a dictionary with lists.

Nested `for` loops go through all four majors and their properties to generate the 16 questions automatically.

A `while` loop checks the user's input. If the user enters anything other than `Yes` or `No`, the same question is repeated.

When the user answers `Yes`, the counter of the related major increases by one. After all questions are completed, the four counters are compared to find the highest score.

If there is no single highest score, the program displays a tie message.

## Code Structure

The code is divided into a few main parts:

### Data Storage

A dictionary stores the majors, while a list inside each dictionary value stores the four properties related to that major.

### Counters

Four counters keep track of the user's score for each major.

### Question Loop

Nested `for` loops go through each major and its properties, allowing the program to generate all 16 questions without repeating the same code manually.

### Input Validation

A `while` loop repeats the same question if the user enters an invalid answer.

### Score Calculation

When the user answers `Yes`, the counter of the related major increases by one.

### Final Recommendation

The four counters are compared, and the major with the highest score is recommended. If there is a tie, the program displays a tie message.

## Challenges I Faced

- Using a `while` loop to validate user input.
- Handling ties between majors with the same highest score.

## What I Learned

This project helped me practice:

- Dictionaries
- Lists
- Nested loops
- `while` loops
- User input validation
- `if`, `elif`, and `else`
- Counters
- Comparison operators
- Basic program logic

I also learned how to combine multiple Python concepts to build a complete interactive project.

## Future Improvements

- Accept different forms of `Yes` and `No` input such as `yes` and `YES`.
- Add more majors and properties.
- Display the scores for all majors.
- Improve the recommendation accuracy.

## Project Status

Completed as a beginner Python learning project and part of my Python 101 learning journey.