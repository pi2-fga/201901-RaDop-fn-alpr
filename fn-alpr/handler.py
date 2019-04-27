import base64
import json
import requests

URL = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=0' \
      '&country=br&secret_key={}'
FN_CALL = 'alpr-call'

def decode(encoded_key: str):
    try:
        decoded = base64.b64decode(encoded_key, validate=True)
        decoded = decoded.decode('utf-8').rstrip('\n')
        if len(decoded) != 27:
            raise Exception('The sent key isn\'t specified as expected.\n' \
                            'Verify the sent key!!')
    except base64.binascii.Error as e:
        status_code = 500
        msg = e
        response = {'status_code': status_code, 'response_message': msg}
        return response
    except Exception as e:
        status_code = 500
        msg = e
        response = {'status_code': status_code, 'response_message': msg}
        return response
    else:
        return decoded


def openalpr_api(private_key: str, image: str):
    try:
        url = URL.format(private_key)
        image = bytes(image)
        request = requests.post(url, data=image)
    except Exception as e:
        status_code = 500
        msg = e
        response = {'status_code': status_code, 'response_message': msg}
        return response
    else:
        return {} # [WIP] function


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    try:
        package = json.loads(req)

        request_type = package['type']
        request_payload = package['payload']
        request_time = package['time']
        key = request_payload['key']
        image = request_payload['image']

        if request_type == FN_CALL:
            status_code = 500
            msg = 'Error!! The message header indicates other function call.' \
                  'Verify if the correct service was called.'
            response = {'status_code': status_code, 'response_message': msg}
            return json.dumps(response)
        if not key:
            status_code = 500
            msg = 'Error trying to get the ALPR API key!!' \
                'Verify service to correct error'
            response = {'status_code': status_code, 'response_message': msg}
            return json.dumps(response)
        
        decoded_key = decode(key)

        if type(decoded_key) is list:
            error = decoded_key
            return json.dumps(error)
        
        
    except Exception as e:
        status_code = 500
        msg = f'Unknown error while trying to execute the ALPR service.' \
              f'Verify service to correct error. Traceback: {e}'
        response = {'status_code': status_code, 'response_message': msg}
        return json.dumps(response)
    else:
        return json.dumps({'key': decoded_key})