# iPeek
================

iPeek is a Python script that allows users to search for Instagram accounts and retrieve information about them.

## Features

* Search for Instagram accounts by username
* Retrieve account information, including:
	+ Username
	+ Full name
	+ Biography
	+ Follower count
	+ Following count
	+ Media count
	+ Private status
	+ Public email
	+ Phone number
	+ Profile picture

## Requirements

* Python 3.x
* `instagrapi` library (install with `pip install instagrapi`)
* `pyfiglet` library (install with `pip install pyfiglet`)

## Usage

1. Clone this repository or download the script.
2. Fill out the constants/id.py file with a dummy account data.
3. Run the script with `python main.py`.
4. Follow the prompts to login to Instagram or search for an account.

## Notes

* This script uses the `instagrapi` library to interact with the Instagram API.
* The `constants` module contains sensitive information, such as your Instagram username and password. Make sure to keep this information secure.
* This script is for educational purposes only and should not be used to scrape or spam Instagram accounts.

## Contributing

Contributions are welcome! If you'd like to add a feature or fix a bug, please submit a pull request.

## License

This script is released under the MIT License. See `LICENSE` for details.
