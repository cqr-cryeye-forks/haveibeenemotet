# CLI tool (not for commercial usage)

[Service.](https://www.haveibeenemotet.com/index.php)

### Usage
```bash
usage: cli.py [-h] [-o OUTPUT] target

positional arguments:
  target                Target for abuse finder.

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT

```

```bash
python cli.py example@gmail.com
```

```json
{
  "result": "Your Email address was found as RECIPIENT 1 times."
}
```