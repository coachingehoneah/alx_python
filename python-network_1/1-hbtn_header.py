"""
Module comments goes
"""

import requests
import sys
req = requests.get(sys.argv[1])
result = req.headers
print(dict(result).get('X-Request-Id'))
