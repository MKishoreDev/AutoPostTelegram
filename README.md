# 📦 AutoPostTelegram [ARCHIVED]

<p align="center">
  <img src="https://i.imgur.com/sbrRXkW.jpeg" width="320">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/STATUS-ARCHIVED-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/PyPI-Legacy%20Package-blue?style=for-the-badge&logo=pypi">
</p>

<p align="center">
  A lightweight Python package built for automatically posting memes, GIFs, facts, anime content, and other media directly to Telegram channels using bot tokens.
</p>

---

# ⚠️ Archive Notice

This project is no longer maintained.

The original API services used by this package are now unavailable/dead, which means many endpoints may no longer function correctly.

This repository is preserved for:
- educational purposes
- archive/history of my early Python work
- reference for Telegram automation ideas

> This was one of my first published PyPI packages and an early experiment with Telegram content automation.

---

# ✨ Features

- Automatic Telegram channel posting
- Anime meme posting support
- Random content endpoints
- Simple Python interface
- Beginner-friendly usage

---

# 📥 Installation

```bash
python3 -m pip install -U AutoPostTelegram
````

---

# 🚀 Examples

## Post Single Anime Meme

```python
from AutoPostTelegram import auto

x = auto(TOKEN)

x.animememe(chat="@AnimeMeme")
```

---

## Infinite Auto Posting

```python
import asyncio
from AutoPostTelegram import auto

x = auto(TOKEN)

while True:
    x.animememe(chat="@AnimeMeme")
    asyncio.sleep(5)
```

---

## Get Available Endpoints

```python
from AutoPostTelegram import auto

print(auto.endpoints())
```

---

# 🐞 Known Issues

```text
Using asyncio.sleep() incorrectly may block other bot functions.
```

At the time this package was created, I was still learning asynchronous programming and Telegram automation.

---

# 📌 Recommended Usage

This package was mainly designed for:

* meme channels
* automated posting bots
* Telegram content experiments

---

# 🧠 Legacy Note

AutoPostTelegram represents one of my earliest open-source Python projects and my first experience publishing a package on PyPI.

Even though the backend APIs are no longer active, the project remains public as part of my development journey.

---

# 👨‍💻 Author

Created by @MKishoreDev
Previously known online as `AASFCYBERKING`

---
