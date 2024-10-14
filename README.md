# PESU IO Attendance

## About

I wrote this because I didn't like to call out names during attendance

## What It Does

It calls out names for you. You just have to type (p)resent, or (a)bsent

## How To Use

1. Install Python
2. Clone this repository and cd into it

```bash
git clone https://github.com/anuragrao04/attendance
cd attendance
```

3. Create a `venv` and install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

4. Run `setup.py` and follow the on screen instructions. This is a one time process

```bash
python setup.py
```

5. Run `main.py` everytime you want to take attendance

```bash
python main.py
```

Note: Make sure to have the virtual environment activated everytime you want to run `main.py`. You can do that with:

```bash
source .venv/bin/activate
```
