# Birds Eye
## For now this script works for windows I'll update it later  🙃
Ever wanted to spy on websites without them knowing? Look no further! This script, like a stealthy ninja, silently takes screenshots of URLs you give it. Want it to be even sneakier? It can do it without popping up any browser windows. It's the James Bond of web reconnaissance, equipped with its trusty Chrome or Firefox disguise. Just feed it a list of targets or a single URL, and watch as it captures the evidence, saving it all in a secret folder. Shaken, not stirred, of course.
## Installation

Download WebDriver:
This script requires either Chrome WebDriver or Gecko (Firefox) WebDriver to function properly. Make sure you have one of them installed and accessible in your PATH.
Run the Script:
You're all set! Now you can run the script by providing either a file containing URLs or a single URL as an argument.

## Repo: 
```
git clone https://github.com/danahkh/Birds-Eye.git
```

## packages 

```
pip install selenium, argparse       # Try to use pip3 if it didn't work for you
```

## snip

```
usage: Birdseye.py [-h] [-f FILE] [-u URL] [-s] [-nw]

Script to take screenshots for reconnaissance

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  File containing list of URLs to capture screenshots
  -u URL, --url URL     Single URL to capture a screenshot
  -s, --slow            Slow down the request
  -nw, --no-window      Capture screenshots without opening the browser window
```


## License

[MIT](https://choosealicense.com/licenses/mit/)
