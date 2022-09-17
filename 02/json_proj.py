import json
from collections import Counter

def parse_json(json_str: str, required_fields=None, keywords=None, keyword_callback = None):
    main_data = json.loads(json_str)
    for key, value in dict(main_data).items():
        if key in required_fields:
            buf = list((Counter(keywords) & Counter(value.split('|'))).elements())
            if buf:
                list(map(keyword_callback, buf))
