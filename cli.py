import json
from argparse import ArgumentParser

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': 'text/html, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.haveibeenemotet.com/index.php',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://www.haveibeenemotet.com',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}


def cli(parser: ArgumentParser):
    parser.add_argument("target", help="Target for haveibeenemotet.")
    parser.add_argument("-o", "--output", default="output.json")
    return parser.parse_args()


def parse(text: str) -> dict:
    soup = BeautifulSoup(text, "lxml")
    span = soup.find('span')
    if not span:
        return {"result": "Email not found."}

    return {"result": span.text}


def main():
    try:
        parser = ArgumentParser()
        args = cli(parser)
        data = {
            'email': args.target,
            'year_form': '2022',
            'month_form': '01',
        }
        response = requests.post(
            'https://www.haveibeenemotet.com/lib/check-ajax.php',
            headers=headers,
            data=data
        )
        print(f"Status code: {response.status_code}")
        result = parse(response.text)
        with open(args.output, "w") as f:
            json.dump(result, f, indent=2)

    except Exception as e:
        print(e)

    print("Done!")


if __name__ == '__main__':
    main()
