FROM ruby:2.2.3-slim  
  
ARG GIT_HASH  
  
MAINTAINER DroneDeploy <dev@dronedeploy.com>  
LABEL Description="Log forwarder image to s3 and elasticsearch using fluentd"
Vendor="DroneDeploy" Version="0.2.0"  
LABEL REPO="https://github.com/dronedeploy/fluentd"  
  
RUN apt-get update -y && apt-get install -yy \  
build-essential \  
zlib1g-dev \  
libjemalloc1  
  
COPY .gemrc /root/  
COPY fluentd.conf /etc/fluent/  
  
RUN gem install fluentd:0.12.26 && \  
fluent-gem install \  
fluent-plugin-s3 \  
fluent-plugin-kubernetes_metadata_filter \  
fluent-plugin-elasticsearch:1.5.0  
  
RUN mkdir -p /var/log/fluent  
  
ENV LD_PRELOAD "/usr/lib/x86_64-linux-gnu/libjemalloc.so.1"  
CMD ["fluentd", "-c", "/etc/fluent/fluentd.conf"]  

