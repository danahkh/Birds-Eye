#!/usr/bin/env python3

import argparse
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def create_cli_parser():
    parser = argparse.ArgumentParser(description="Script to take screenshots for reconnaissance")
    parser.add_argument('-f', '--file', type=str, help='File containing list of URLs to capture screenshots')
    parser.add_argument('-u', '--url', type=str, help='Single URL to capture a screenshot')
    parser.add_argument('-s', '--slow', action='store_true', help='Slow down the request')
    args = parser.parse_args()
    return args

def capture_screenshot(url, output_dir, browser='chrome', slow=False):
    if browser == 'chrome':
        chrome_options = Options()
        if not slow:
            chrome_options.add_argument('--headless')  # Run in headless mode
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == 'firefox':
        firefox_options = FirefoxOptions()
        if not slow:
            firefox_options.add_argument('-headless')  # Run in headless mode
        driver = webdriver.Firefox(options=firefox_options)
    else:
        raise ValueError("Invalid browser option. Use 'chrome' or 'firefox'.")

    try:
        driver.get(url)
        # Add optional delay to slow down the request
        if slow:
            time.sleep(3)
        filename = os.path.join(output_dir, f"{url.replace('http://', '').replace('https://', '').replace('/', '_')}.png")
        driver.save_screenshot(filename)
        print(f"Screenshot saved to {filename}")
    except Exception as e:
        print(f"Error capturing screenshot for {url}: {e}")
    finally:
        driver.quit()

def capture_screenshots_from_file(file_path, output_dir, slow=False):
    with open(file_path, 'r') as file:
        urls = file.readlines()
        for url in urls:
            url = url.strip()
            if url.startswith(('http://', 'https://')):
                capture_screenshot(url, output_dir, slow=slow)
            else:
                print(f"Skipping invalid URL: {url}")

def main():
    cli_args = create_cli_parser()

    if cli_args.file:
        os.makedirs('screenshots', exist_ok=True)  # Default output directory
        capture_screenshots_from_file(cli_args.file, 'screenshots', cli_args.slow)
        # Create a file containing the screenshots and name it after the first URL
        first_url = open(cli_args.file).readline().strip()
        os.rename('screenshots', f'{first_url.replace("http://", "").replace("https://", "").replace("/", "_")}_screenshots')
    elif cli_args.url:
        os.makedirs('screenshots', exist_ok=True)  # Default output directory
        capture_screenshot(cli_args.url, 'screenshots', slow=cli_args.slow)
    else:
        print("Please provide either a file containing URLs using the -f/--file argument or a single URL using the -u/--url argument.")

if __name__ == "__main__":
    main()
