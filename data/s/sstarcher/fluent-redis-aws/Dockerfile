FROM fluent/fluentd:v0.14.1  
MAINTAINER shanestarcher@gmail.com  
  
USER root  
RUN apk --no-cache --update add ruby-dev build-base && \  
gem install -N json && \  
apk del build-base ruby-dev  
  
RUN gem install -N fluent-plugin-docker_metadata_filter  
RUN gem install -N fluent-plugin-redis-store  
RUN gem install -N fluent-plugin-record-reformer  
RUN gem install -N fluent-plugin-record-modifier  
RUN gem install -N fluent-plugin-rename-key  
RUN gem install -N fluent-plugin-grep  
RUN gem install -N fluent-plugin-ec2-metadata  
  
ENV REDIS_HOST logging.private  
ENV REDIS_PORT 6379  
VOLUME ["/fluentd/log/containers"]  
  
COPY fluent.conf /fluentd/etc/  
  

