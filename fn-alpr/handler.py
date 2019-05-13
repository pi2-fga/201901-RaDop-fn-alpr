import base64
import json
import requests
import uuid


URL = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=0' \
      '&country=br&secret_key={}'
FN_CALL = 'alpr-call'
KEY_LENGTH = 27


def decode(encoded_key: str):
    try:
        decoded = base64.b64decode(encoded_key, validate=True)
        decoded = decoded.decode('utf-8').rstrip('\n')
        if len(decoded) != KEY_LENGTH:
            raise Exception('The sent key isn\'t specified as expected.\n'
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
        image = bytes(image, 'utf-8')
        request = requests.post(url, data=image)
        response = request.json()
        if 'error_code' in response.keys():
            code = response['error_code']
            msg = response['error']
            raise Exception(f'Error while calling ALPR API.\nTraceback:'
                            f' {code} - {msg}')
        elif 'data_type' in response.keys() and \
             'alpr_results' in response['data_type']:
            identifier = str(uuid.uuid4())
            response['uuid'] = identifier
        else:
            raise Exception(f'Unknown condition while receiving data from'
                            f'ALPR API. Object received {response}.')
    except Exception as e:
        status_code = 500
        msg = e.args[0]
        response = {'status_code': status_code, 'response_message': msg}
        return response
    else:
        return response


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    try:
        package = json.loads(req)
        request_type = package['type']
        request_payload = package['payload']
        key = request_payload['key']
        image = request_payload['image']

        if request_type != FN_CALL:
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

        call = openalpr_api(decoded_key, image)

    except Exception as e:
        status_code = 500
        msg = f'Unknown error while trying to execute the ALPR service.' \
              f'Verify service to correct error. Traceback: {e}'
        response = {'status_code': status_code, 'response_message': msg}
        return json.dumps(response)
    else:
        return json.dumps({'status_code': 200, 'response': call})
