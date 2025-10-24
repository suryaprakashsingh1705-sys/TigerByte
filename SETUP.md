# TigerByte Setup Guide for macOS 🐅

Welcome to **TigerByte**! Follow these steps to get the interpreter running on your Mac.  
This guide is beginner-friendly and includes tips to make your coding journey fun.

---

## 1️⃣ Install Dependencies

### 1.1 Install Homebrew (Package Manager for macOS)

Homebrew helps you install software on your Mac easily. If you already have it, skip this step.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Check Homebrew installation:

```bash
brew --version
```

You should see something like:

```bash
Homebrew 4.5.0
```

> 💡 Pro Tip: Homebrew makes installing Python, pip, and other tools super easy.

### 1.2 Install Python 3.x

```bash
brew install python
```

Check Python version:

```bash
python3 --version
```

You should see something like:

```bash
Python 3.11.x
```

## 2️⃣ Clone TigerByte Repository

```bash
git clone https://github.com/your-username/TigerByte.git
cd TigerByte
```

> 💡 Pro Tip: If you forked the repo, use your fork URL. This makes contributing back easier.

## 3️⃣ Run the Interpreter

```bash
python3 tigerbyte.py
```

> 🐅 Fun Tip: Try a simple test command first:

```python
print("🐅 TigerByte is running!")
```

You should see the message printed in the terminal.

## 4️⃣ Common Issues & Fixes

| Issue                                    | Solution                                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Permission denied running `tigerbyte.py` | Run `chmod +x tigerbyte.py`                                                                                         |
| Python version mismatch                  | Run `python3 --version` and ensure Python 3.x is installed                                                          |
| Module not found                         | Install dependencies: `pip install -r requirements.txt`                                                             |
| Homebrew not found                       | Install Homebrew: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` |
| pipenv not found                         | Install pipenv: `brew install pipenv`                                                                               |
