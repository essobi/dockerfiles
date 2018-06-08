FROM ubuntu:latest  
  
MAINTAINER Maksym Bilenko "sath891@gmail.com"  
ENV DOCKER_HOST unix:///var/run/docker.sock  
ENV LOGSTASH_URL tcp://logstash:9290  
COPY main.rb /app/DockerLogstash/main.rb  
COPY Gemfile /app/DockerLogstash/Gemfile  
  
WORKDIR /app/DockerLogstash  
RUN apt-get update && apt-get install ruby ruby-bundler ruby-dev build-
essential -y && bundle install && apt-get clean && rm -rf /tmp/*
/var/lib/apt/lists/* /var/tmp/*  
  
CMD ruby main.rb  

