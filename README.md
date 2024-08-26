# MyRequests Library

## Description

**MyRequests** is a library in progress that aims to reproduce the functionality of the popular Python `requests` library. The goal is to provide a similar API for making HTTP requests, handling responses, and managing sessions. This project is intended for educational purposes and to help understand the inner workings of HTTP request handling.

## Features

- Sending HTTP/HTTPS requests
- Handling responses with various status codes
- URL encoding and parameter handling
- Sessions for maintaining connection state
- Customizable request headers and payloads

## Installation

To install **MyRequests**, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/myrequests.git
    ```

2. Navigate into the project directory:

    ```bash
    cd myrequests
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Here's a basic example of how to use **MyRequests**:

### Sending a GET Request

```python
from Requests import Requests

response = Requests.get('https://jsonplaceholder.typicode.com/posts',headers=headers,params=params)
print(response.status_code)
print(response.html)
print(response.text)
