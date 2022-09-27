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
from prometheus_pb2 import (
    WriteRequest
)
import calendar
import requests
import snappy


def dt2ts(dt):
    """Converts a datetime object to UTC timestamp
        naive datetime will be considered UTC.
        """
    return calendar.timegm(dt.utctimetuple())


class CprometheusWriter(object):
    def __init__(self, url):
        super(CprometheusWriter, self).__init__()
        self._url = url
        self._headers = {
            "Content-Encoding": "snappy",
            "Content-Type": "application/x-protobuf",
            "X-Prometheus-Remote-Write-Version": "0.1.0",
            "User-Agent": "metrics-worker"
        }

    def write(self, name, labels, value):
        write_request = WriteRequest()
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
        sample.timestamp = dt2ts(datetime.utcnow()) * 1000

        uncompressed = write_request.SerializeToString()
        compressed = snappy.compress(uncompressed)

        response = requests.post(self._url,
                                 headers=self._headers,
                                 data=compressed)
        return response


if __name__ == "__main__":
    pass
