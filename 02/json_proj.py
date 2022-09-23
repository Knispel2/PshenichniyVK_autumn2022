import json
from collections import Counter

def parse_json(json_str: str, required_fields=None, keywords=None, keyword_callback = None):
    if not keyword_callback: return None
    main_data = json.loads(json_str)
    for obj in required_fields:
        if obj in main_data:
            buf = list((Counter(keywords) & Counter(main_data[obj].split('|'))).elements())
            if buf: list(map(keyword_callback, buf))