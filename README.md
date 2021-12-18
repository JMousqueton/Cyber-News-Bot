# 🏴‍☠️ Cyber-News Bot 🤖 for Twitter 🐦
***
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
 ![Version](https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](https://github.com/JMousqueton/Badware/blob/main/LICENSE)
[![Twitter: JMousqueton](https://img.shields.io/twitter/follow/JMousqueton.svg?style=social)](https://twitter.com/JMousqueton)

Based on an idea by [Cybersec-Twitter-BOT](https://github.com/0z09e/Cybersec-Twitter-BOT) this BOT retweets every tweets related to cybersecurity based on hashtags. 

## Future 

Check the [TODO.md](https://github.com/JMousqueton/Cyber-News-Bot/blob/main/TODO.md) file 

## Installation
Install all the modules in ```requirement.txt```
```
pip3 install -r requirements.txt
```

## Configuration

1. Go to [Twitter Developer Platform](https://developer.twitter.com/) and create a new app.  

2. rename config.cfg.sample to config.cfg

3. Now just take those keys and slap them on config.cfg, Following keys are required.
- API_key
- API_key_secret
- Access_token
- Access_token_secret
- Bearer_token

4. Now replace hashtags with whatever query you want.

⚠️ For troubleshooting you can set the DEBUG variable to True

## Usage

Execute main.py using python3

```
python3 main.py
```

You can execute this script hourly with the crontab 

For example if the script is in the folder /opt/bot : 
```
5 * * * *  cd /opt/bot && python3 main.py
```

See [Crontab Guru](https://crontab.guru/) for more details about crontab syntax 

## Demo 

My bot is publishing the tweets [here](https://twitter.com/Bot_CyberNews) 

## Author

👤 **Julien Mousqueton**

* Website: <https://www.julienmousqueton.fr>
* Twitter: [@JMousqueton](https://twitter.com/JMousqueton)
* Github: [@JMousqueton](https://github.com/JMousqueton)
* LinkedIn: [Julien Mousqueton](https://linkedin.com/in/julienmousqueton)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

Feel free to check [issues page](https://github.com/JMousqueton/Cyber-News-Bot/issues).

## 📝 License

Copyright © 2021 [Julien Mousqueton](https://github.com/JMousqueton).

This project is [Apache 2.0](https://github.com/JMousqueton/Cyber-News-Bot/blob/main/LICENSE) licensed.

## Show your support

Give a ⭐️ if this project helped you!
