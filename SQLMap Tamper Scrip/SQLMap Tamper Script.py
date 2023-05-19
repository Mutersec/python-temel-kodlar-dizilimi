import subprocess
import json

def run(script, json_data):
    result = subprocess.check_output([script, json_data])
    return result

def ascii_dict(data):
    ascii_encode = lambda x: x.encode('ascii') if isinstance(x, unicode) else x
    return dict(map(ascii_encode, pair) for pair in data.items())

def tamper(payload, **kwargs):
    script = "<tamper_script_path>"  # Tamper betiği yolunu buraya girin
    json_data = json.dumps({"payload": payload, "kwargs": kwargs})

    result = run(script, json_data)
    json_raw = json.loads(result, object_hook=ascii_dict)

    tampered_payload = json_raw["payload"]
    user_kwargs = json_raw["kwargs"]
    user_headers = user_kwargs.get("headers")
    headers = kwargs.get("headers", {})

    if user_headers:
        headers.update(user_headers)

    return tampered_payload

#Yapımcı Muter 
