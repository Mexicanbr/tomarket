# TOMARKET - Script Bot

AUTO CLAIM FOR 	TOMARKET / @Tomarket_ai_bot

[![Join our Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/MexicanbrScripts)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Mexicanbr)

# Table of Contents
- [Tomarket](#Tomarket)
- [Warning](#warning)
- [Available Features](#available-features)
- [Registration](#registration)
- [How to Use](#how-to-use)
  - [Command Line Options / Arguments](#command-line-options--arguments)
  - [About Proxies](#about-proxies)
  - [Windows](#windows)
  - [Linux](#linux)
  - [Termux](#termux)
- [Viewing Reports](#viewing-reports)
- [Thank You](#thank-you)

# Updates

- 19.10.2024 The games are available again


# Warning

All risks are borne by the user

# Available Features

- [x] Automatic claim.
- [x] Automatic daily check-in (Login)
- [x] Automatic claim of reference results
- [x] Automatic task completion
- [x] Autoplay after claim

# Registration

Click the following link to register: [https://t.me/Tomarket_ai_bot/](https://t.me/Tomarket_ai_bot/app?startapp=0002KeIZ)

# How to Use

## Command Line Options / Arguments

This script/program supports several argument parameters that can be used. Here's an explanation of the arguments:

`--data` / `-D`: Used when you have a different filename for storing account data. By default, the filename used by this script/program to store account data is `data.txt`. For example, if you have a file named `query.txt` as the file storing account data, just run `main.py` with the `--data` / `-D` argument. Example: `python main.py --data query.txt`

`--proxy` / `-P`: Used when you have a different filename for storing the proxy list. The filename used by this script/program to store the proxy list is `proxies.txt`. For example, if you have a file named `prox.txt` as the file storing the proxy list, you just need to add the `--proxy` / `-P` argument parameter to use your proxy file. Example: `python main.py --proxy prox.txt`

`--worker` / `-W`: This argument is used to customize the number of threads/workers used when the bot script is running. By default, this script/software uses (total CPU cores / 2) as the number of workers. For example, if your CPU has 6 cores, the number of workers used is 3. You can customize the number of workers using this argument. For example, if you want to set the number of workers to 100, run `main.py` with this argument: `python main.py --worker 100`. And if you don't like using workers/threads/multiprocessing, you can customize the worker to 1, for example: `python main.py --worker 1`.

`--action` / `-A`: This argument is used to directly enter the desired menu. For example, if this bot script has 5 menus and you don't want to input manually, you can use this argument to directly enter the desired menu. Example: `python main.py --action 5` means you will directly enter menu number 5. This argument is useful if you're using docker/pm2 to run the bot script in the background process.

## Windows 

1. Make sure your computer has Python and Git installed.

    Recommendation: Use Python version 3.8+ (3.8 or newer)
   
   Python site: [https://python.org](https://python.org)
   
   Git site: [https://git-scm.com/](https://git-scm.com/)

2. Clone this repository.
   ```shell
   git clone https://github.com/Mexicanbr/tomarket.git
   ```

3. Enter the tomarket folder
   ```
   cd tomarket
   ```

4. Install the required modules/libraries.
   ```
   python -m pip install -r requirements.txt
   ```

5. Edit the `data.txt` file, enter your query data into the `data.txt` file. One line for 1 account, if you want to add a 2nd account, fill it in on a new line.

6. Run the program/script.
   ```
   python main.py
   ```

## Linux 

1. Make sure your computer has Python and Git installed.

    Recommendation: Use Python version 3.8+ (3.8 or newer)
   
   Python
   ```shell
   sudo apt install python3 python3-pip
   ```
   Git
   ```shell
   sudo apt install git
   ```

2. Clone this repository.
   ```shell
    git clone https://github.com/Mexicanbr/tomarket.git
   ```

3. Enter the Tomarket folder
   ```
   cd tomarket
   ```

4. Install the required modules/libraries.
   ```
   python -m pip install -r requirements.txt
   ```

5. Edit the `data.txt` file, enter your query data into the `data.txt` file. One line for 1 account, if you want to add a 2nd account, fill it in on a new line.

6. Run the program/script.
   ```
   python main.py
   ```

## Termux

1. Make sure your device has Python and Git installed.

    Recommendation: Use Python version 3.8+ (3.8 or newer)
   
   Python
   ```shell
   pkg install python3
   ```
   Git
   ```shell
   pkg install git
   ```

2. Clone this repository.
   ```shell
    git clone https://github.com/Mexicanbr/tomarket.git
   ```

3. Enter the tomarket folder
   ```
   cd tomarket
   ```

4. Install the required modules/libraries.
   ```
   python -m pip install -r requirements.txt
   ```

5. Edit the `data.txt` file, enter your query data into the `data.txt` file. One line for 1 account, if you want to add a 2nd account, fill it in on a new line.

6. Run the program/script.
   ```
   python main.py
   ```

# Viewing Reports

To view a report of the total balance of all accounts you can run a file called `report.py`


## How to get tgWebAppData (query_id / user_id)

1. Login telegram via portable or web version
2. Launch the bot
3. Press `F12` on the keyboard 
4. Open console
5. Сopy this code in Console for getting tgWebAppData (user= / query=):

```javascript
copy(Telegram.WebApp.initData)
```

6. you will get data that looks like this

```
query_id=AA....
user=%7B%22id%....
```
7. add it to `data.txt` file or create it if you dont have one


You can add more and run the accounts in turn by entering a query id in new line like this:
```txt
query_id=xxxxxxxxx-Rxxxxujhash=cxxx
query_id=xxxxxxxxx-Rxxxxujhash=cxxxx
```


# Error Table

| Error                 | Description                                                                                                                          |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| failed get json error | This is because the server response is not in JSON format and may be in HTML. You can check the server response in the http.log file |
| failed get task list  | This is because the server response doesn't provide the expected response. You can check the server response in the http.log file    |
| cannot start game     | Similar to the above error, this is due to the server. You can check the server response in the http.log file                        |

## This bot helpfull?  Please support me by buying me a coffee: 
``` 0x5e14f8333a49b888bc66068c18cde3ecc6f8b272 ``` - BSC (BEP 20)

``` EQCA1BI4QRZ8qYmskSRDzJmkucGodYRTZCf_b9hckjla6dZl ``` ``` Memo - 2084424251 ``` - TON

``` 0x5e14f8333a49b888bc66068c18cde3ecc6f8b272 ``` - Optimism

``` TDanbBakUT2dkQdzpkC7tCugMvd5eNGWnR ``` - TRX (TRC 20)

## License
This project is licensed under the MIT License - see the LICENSE file for details.

# Thank You
