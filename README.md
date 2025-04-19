# Sectrails CLI Tool

Sectrails is a command-line tool that leverages the [SecurityTrails API](https://securitytrails.com/) to fetch DNS history for a target domain. This tool allows you to quickly and easily retrieve DNS records and related historical data directly from your terminal.

## Features

- **Fetch DNS History:** Retrieve historical DNS data for a specified target domain.
- **Data Presentation:** Display the results in a neatly formatted table using `tabulate`.
- **Simple CLI Usage:** Run the tool from the command line with clear, straightforward options.

## Requirements

- Python 3
- [Requests](https://docs.python-requests.org/) library
- [Tabulate](https://pypi.org/project/tabulate/) library

Install the Python dependencies using:

```sh
pip install requests tabulate
```

## Usage

Once installed or running locally, execute the tool using:

```sh
./sectrails -target test.com -apikey YOUR_API_KEY
```

Or if installed globally:

```sh
sectrails -target test.com -apikey YOUR_API_KEY
```

Replace `test.com` with your target domain and `YOUR_API_KEY` with your SecurityTrails API key.

## Setup and Installation

1. Ensure the `sectrails` file is executable:
   ```sh
   chmod +x sectrails
   ```
2. Run the tool from within the project directory:
   ```sh
   ./sectrails -target test.com -apikey YOUR_API_KEY
   ```

## SecurityTrails API

This tool uses the SecurityTrails API to access DNS historical data. For more information on available endpoints and parameters, visit the [SecurityTrails API documentation](https://securitytrails.com/corp/apidocs).

## License

[MIT License](LICENSE)
