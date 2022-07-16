# Password Generator (GCP Functions Tutorial)

A toy project for GCP Functions that generates xkcd-ish passwords.

## Requirements

- [functions-framework](https://pypi.org/project/functions-framework/)

## Installation

There is nothing to install.

## Usage

### Live Demo

For a demo, try:

```bash
curl "https://generate-password-h5i3eq52qq-oa.a.run.app/"
```

### Parameters

> None of the parameters are required.

| Key                      | Type | Default |
| ------------------------ | ---- | ------- |
| word_count<sup>a,b</sup> | int  | 2       |
| delimiter<sup>c,d</sup>  | str  | '-'     |
| contains_number          | bool | True    |
| title_case               | bool | True    |
| report_entropies         | bool | False   |
| report_params            | bool | False   |

- <sup>a</sup> All are 5-letter words; the list is in [words.py](words.py).
- <sup>b</sup> Must be in range (1,10).
- <sup>c</sup> Must be a single character.
- <sup>d</sup> Must be either a space or in `Python`'s `string.punctuation`.

For example, to generate a password similar to [xkcd's comic](https://xkcd.com/936/), you can set the following options:


| Key              | Value  |
| ---------------- | -----  |
| word_count       | 4      |
| delimiter        | ' '    |
| contains_number  | False  |
| title_case       | False  |

```
GET <domain:port>/generate_password?word_count=4&delimiter= &contains_number=False&title_case=False
```

### Run locally (for debug purposes)

1. Start the flask server

```bash
export FLASK_APP=local_test
export FLASK_ENV=development
flask run
```

2. Exceute requests:

```bash
# default
wget -qO- "http://127.0.0.1:5000/generate_password"
# spiced up
wget -qO- "http://127.0.0.1:5000/generate_password?word_count=4&delimiter= &contains_number=False&title_case=False&report_entropies=True&report_params=True"
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
