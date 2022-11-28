![Logo](https://raw.githubusercontent.com/sergiopm97/sokkai/main/sokkai_logo.png)

# Sokkai

An AI created to predict soccer match results as accurately as possible 🤖⚽

## Features

- Predict the winners of soccer games on a daily basis
- Predict additionally if you are going to see more or less than 2.5 goals in the matches
- Export match predictions in CSV format to the predictions folder

## App setup

Clone the project

```bash
  git clone https://github.com/sergiopm97/sokkai
```

Go to the project directory

```bash
  cd sokkai
```

Create virtual environment

```bash
  python -m venv env
```

Activate the virtual environment

```bash
  & env/Scripts/Activate.ps1
```

Install the requirements in the virtual environment

```bash
  pip install -r requirements.txt
```

## Usage

If you want to generate today's predictions and export them to the predictions directory, run the following script:

```bash
python .\predict.py
```

If you want to retrain the predictive models because you have made changes in the training process, run the following script:

```bash
python .\train.py
```

## Tech Stack

**Python version** -> 3.10.2

**Packages** -> Explore requirements.txt

## Authors

- [@sergiopm97](https://github.com/sergiopm97)
