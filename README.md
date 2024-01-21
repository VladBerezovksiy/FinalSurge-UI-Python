# [FinalSurge Link](https://log.finalsurge.com/)

## Website Description:

> This site is an online service for training and managing physical activity. It is designed for athletes and coaches
> who
> want to track their training plans, results and progress in real time. Various tools are available on the site, such
> as
> creating and customizing individual training programs, setting goals, tracking progress, analyzing workouts, and much
> more.

## Product Description:

> This project allows you to automate software testing in order to analyze the quality of the website, as well as
> identify
> bugs when the project is launched.

## Getting Started

To enjoy the automated tests, develop the framework or adapt it to your own purposes, just download the project or clone
repository. You need to install packages using pip according to requirements.txt file.
Run the command below in terminal:

```
pip install -r requirements.txt
```

#### ATTENTION:

**Login** and **Password** need to create in **_.env_** file

## Commands:

**Command to run all tests:**

```
pytest -s -v
```

**Command to run specific tests:**

```
pytest -m "mark_name"
```

**Command to run specific tests and generate report:**

```
pytest -m "choose_name" --alluredir reports
```

**Command to open report in cloud storage:**

```
allure serve
```

### Test Plan:

| ID | Pages          | Status | 
|----|----------------|--------|
| 1  | Login          | Done   |
| 2  | Workout        | ---    |
| 3  | Daily Vitals   | Done   |
| 4  | Gear & Routes  | Done   |
| 5  | Training Plans | ---    |
| 6  | Resources      | ---    |
| 7  | Message Boards | ---    |
| 8  | Calendar       | ---    |
| 9  | Workout Calc   | Done   |
| 10 | Other Calc     | ---    |