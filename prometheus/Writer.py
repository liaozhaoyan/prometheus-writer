# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     prometheusWriter
   Description :
   Author :       liaozhaoyan
   date：          2022/9/28
-------------------------------------------------
   Change Activity:
                   2022/9/28:
-------------------------------------------------
"""
__author__ = 'liaozhaoyan'

from datetime import datetime
from .prometheus_pb2 import WriteRequest
import calendar
import requests
import snappy


def dt2ts(dt):
    """Converts a datetime object to UTC timestamp
        naive datetime will be considered UTC.
        """
    return calendar.timegm(dt.utctimetuple())


class Cwriter(object):
    def __init__(self, url, auth=None, session=True,
                 cert=None, verify=True, proxies=None
                 ):
        super(Cwriter, self).__init__()
        self._url = url
        self._headers = {
            "Content-Encoding": "snappy",
            "Content-Type": "application/x-protobuf",
            "X-Prometheus-Remote-Write-Version": "0.1.0",
            "User-Agent": "metrics-worker"
        }
        self._auth = auth
        self._cert = cert
        self._verify = verify
        self._proxies = proxies

        if session:
            self._post = requests.Session().post
        else:
            self._post = requests.post

    def _pack(self, write_request, ts,
              name, labels, value):
        series = write_request.timeseries.add()

        label = series.labels.add()
        label.name = "__name__"
        label.value = name

        for k, v in labels.items():
            label = series.labels.add()
            label.name = k
            label.value = v

        sample = series.samples.add()
        sample.value = value
        sample.timestamp = ts

    def _send(self, write_request):
        uncompressed = write_request.SerializeToString()
        compressed = snappy.compress(uncompressed)
        response = None

        try:
            response = self._post(self._url,
                                  headers=self._headers,
                                  auth=self._auth,
                                  data=compressed,
                                  cert=self._cert,
                                  verify=self._verify,
                                  proxies=self._proxies,
                                  )
            if not response.ok:
                response.raise_for_status()
        except requests.exceptions.RequestException as err:
            print(err)
        return response

    def write(self, name, labels, value):
        write_request = WriteRequest()
        ts = dt2ts(datetime.utcnow()) * 1000
        self._pack(write_request, ts, name, labels, value)

        self._send(write_request)

    def writes(self, lines):
        write_request = WriteRequest()
        ts = dt2ts(datetime.utcnow()) * 1000

        for line in lines:
            self._pack(write_request, ts, line[0], line[1], line[2])

        self._send(write_request)


class CslsWriter(Cwriter):
    def __init__(self, endpoint,
                 project, metricStore, auth):
        url = "https://%s.%s/prometheus/%s/%s/api/v1/write" % (project, endpoint, project, metricStore)
        super(CslsWriter, self).__init__(url, auth)


if __name__ == "__main__":
    pass
