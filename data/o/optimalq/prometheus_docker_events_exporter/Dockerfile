FROM ubuntu:xenial  
MAINTAINER Yechiel Levi "yechiel@optimalq.com"  
LABEL Description="Docker events prometheus-exporter" Vendor="OptimalQ"
Version="1.0"  
  
RUN apt-get update -y  
  
RUN apt-get install -y docker.io python python-pip  
RUN pip install docker-py  
RUN pip install prometheus_client  
  
WORKDIR /opt/prometheus_docker_exporter  
COPY . /opt/prometheus_docker_exporter  
  
EXPOSE 8000  
CMD ["python","main.py"]  

