FROM alpine:latest  
LABEL maintainer="jduchesne@coveo.com"  
  
COPY . /opt/awslimitchecker  
RUN apk add --update python3 py3-pip && pip3 install /opt/awslimitchecker
prometheus_client  
COPY ./prometheus.py /opt/prometheus_client/prometheus.py  
  
EXPOSE 8080  
ENTRYPOINT python3 /opt/prometheus_client/prometheus.py

