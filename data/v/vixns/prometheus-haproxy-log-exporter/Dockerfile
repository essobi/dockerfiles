FROM python:3-alpine  
COPY . /src  
RUN apk --no-cache --update add curl snappy snappy-dev g++ \  
&& cd /src && python setup.py install \  
&& apk del g++ snappy-dev \  
&& cd / && rm -rf /src  
ENTRYPOINT ["/usr/local/bin/prometheus-haproxy-log-exporter"]  

