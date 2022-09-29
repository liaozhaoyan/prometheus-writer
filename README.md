# prometheus-writer
&emsp;prometheus-writer is a python-based implementation of the prometheus remote write development kit.

## 1、Preparation for installation
&emsp;Install dependent packages, eg;
```
yum install -y gcc snappy-devel
```

## 2、 install prometheus-writer
```
pip install prometheus-writer
```

## 3、verify
### 3.1、setup server
&emsp;Pull up the prometheus service through the container and enable remote write feature，

&emsp;yml

```
global:
  scrape_interval:     30s
  evaluation_interval: 60s

scrape_configs:
  - job_name: prometheus
    static_configs:
      - targets: ['localhost:9090']
        labels:
          instance: prometheus
```
&emsp;run

```
docker run -d  -p 9090:9090 -v /opt/prometheus/prometheus.yml:/prometheus/prometheus.yml --name prometheus  prom/prometheus --enable-feature=remote-write-receiver
```
### 3.2、run
&emsp;test code

```
import time
import random
from prometheus.Writer import Cwriter


def test():
    w = Cwriter("http://127.0.0.1:9090/api/v1/write")
    while True:
        w.write("random_test", {"hello": "world"}, random.uniform(10, 20))
        time.sleep(15)


if __name__ == "__main__":
    test()
    pass
```

### 3.3、Displays the results
&emsp;Open the http://127.0.0.1:9090/ from a web browser, filter metric name then show:

![img](imag/view.jpg)

### 3.4、multi write
&emsp;If you want to write multiple lines, you can call the writes function.

```
	   lines = (
            ("random_test", {"hello": "world"}, random.uniform(10, 20)),
            ("random_test", {"hello": "world2"}, random.uniform(10, 20)),
        )
        w.writes(lines)
        time.sleep(15)
```
