# -*- coding: utf-8 -*-
import json, logging, requests


class Error(Exception):
    """Base exception class for this module"""
    pass


class JSONReadError(Error):
    pass


class BaseAPI(object):
    """
        Basic api class for
    """

    def __init__(self, auth_token, consumer_token):
        self.auth_token = auth_token
        self.consumer_token = consumer_token
        self.end_point = 'api.packet.net'
        self._log = logging.getLogger(__name__)

    def call_api(self, method, type='GET', params=None):
        if params is None:
            params = {}

        url = 'https://'+ self.end_point +'/'+ method

        headers = {'X-Auth-Token': self.auth_token,
                   'X-Consumer-Token': self.consumer_token,
                   'Content-Type': 'application/json'}

        # remove token from log
        headers_str = str(headers).replace(self.auth_token.strip(), 'TOKEN')
        self._log.debug('%s %s %s %s' %
                        (type, url, params, headers_str))

        if type=='GET':
            resp = requests.get(url, headers=headers)
        elif type=='POST':
            resp = requests.post(url, headers=headers, data=json.dumps(params))
        elif type=='DELETE':
            resp = requests.delete(url, headers=headers)
        elif type=='PATCH':
            resp = requests.patch(url, headers=headers, params=params)
        else:
            raise Error(
                'method type not recognizes as one of GET, POST, DELETE or PATCH: %s' % type
            )
            
        if str(resp.status_code)[0] != str(2):
            raise Error(
                'non 2xx HTTP status code: %s' % resp.status_code
            )

        if not resp.content:
            return None

        try:
            data = resp.json()
        except ValueError as e:
            raise JSONReadError(
                'Read failed: %s' % e.message
            )
        return data

