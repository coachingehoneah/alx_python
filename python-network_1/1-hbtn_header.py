"""Module comments goes
"""

import requests
import sys
req = requests.get(sys.argv[1])
print(req.headers['X-Request-Id'])

