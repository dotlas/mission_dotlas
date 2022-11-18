# Mission Dotlas - Summer 2022 Assignment Solution

A standard solution to the Dotlas Part-Time Data Engineering Technical Assignment

- [Mission Dotlas - Summer 2022 Assignment Solution](#mission-dotlas---summer-2022-assignment-solution)
  - [Setup](#setup)
  - [Understanding the Files](#understanding-the-files)

## Setup

Using Conda on your terminal, create and activate your environment:

```bash
conda create --name dotlas_assignment python=3.10 -y
conda activate dotlas_assignment
```

Clone the repository and enter it

```bash
git clone https://github.com/cricksmaidiene/dotlas_assignment_sol
cd dotlas_assignment_sol/solution
```

Install requirement libraries and execute the script

```bash
pip install -r requirements.txt
python main.py
```

## Understanding the Files

If you want to understand how the different files are connected, read them in the following order:

`fields.py` -> `utils.py` -> `parser.py` -> `main.py`

All files have documentation and comments explaining the use of tooling and others.
