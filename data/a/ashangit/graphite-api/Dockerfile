#  
# graphite-api  
#  
# Pull base image.  
FROM ashangit/base:latest  
MAINTAINER Nicolas Fraison <nfraison@yahoo.fr>  
  
ENV GRAPHITE_API_VERSION 1.1.2  
ENV GUNICORN_VERSION 19.4.1  
ENV GRAPHITE_API_CONFIG /data/graphite-api/conf/graphite-api.yml  
  
# Deploy graphite-api.  
RUN yum install cairo python-devel python-pip libffi-devel make gcc -y && \  
pip install graphite-api==${GRAPHITE_API_VERSION} && \  
pip install gunicorn==${GUNICORN_VERSION}  
  
# Remove compiler package  
RUN yum remove python-devel gcc make -y  
  
# Create required folders  
RUN mkdir -p /data/graphite-api/conf && \  
mkdir -p /data/graphite/data/whisper && \  
mkdir -p /data/graphite-api/index  
  
# Set working directory  
WORKDIR /data/graphite-api  
  
# Copy default config file  
COPY conf/graphite-api.yml /data/graphite-api/conf/graphite-api.yml  
COPY conf/gunicorn-conf.py /data/graphite-api/conf/gunicorn-conf.py  
  
# Declare default env variables  
ENV WORKER_PROCESSES 2  
ENV TIMEOUT 60  
# Expose graphite-api port  
EXPOSE 8888  
# Default command  
CMD gunicorn -b 0.0.0.0:8888 -c /data/graphite-api/conf/gunicorn-conf.py
graphite_api.app:app

