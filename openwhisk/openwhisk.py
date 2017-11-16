# -*- coding: utf-8 -*-

"""Main module."""

import base64
import requests
import os
import json

def wisk_auth():
    key = os.environ["__OW_API_KEY"]
    auth = "Basic %s" % base64.b64encode(key.encode('ascii')).decode('ascii')
    return auth


def wisk_invoke(action, **kwargs):
    r = requests.post(
        "https://openwhisk.ng.bluemix.net/api/v1/namespaces/_/actions/%s" %
        (action),
        json=kwargs,
        headers={"Authorization": whisk_auth()})
    return r.content


def wisk_get(pkg):
    ns = os.environ["__OW_NAMESPACE"]
    r = requests.get(
        "https://openwhisk.ng.bluemix.net/api/v1/namespaces/%s/packages/%s" %
        (ns, pkg),
        headers={"Authorization": whisk_auth()})
    return r.content


def params_from_pkg(pkg):
    content = wisk_get(pkg)
    j = json.loads(content)
    params = {}
    for p in j['parameters']:
        params[p['key']] = p['value']
    return params
