FROM ruby:2.3.3-slim  
MAINTAINER Nan Liu <nan.liu@gmail.com>  
  
ARG BUILD_DATE  
  
LABEL name="Intelsdi-X pluginsync" \  
license="Apache 2.0" \  
build-date=$BUILD_DATE  
  
COPY Gemfile /Gemfile  
RUN apt-get update && \  
apt-get install -y build-essential git socat && \  
bundle install && \  
apt-get autoremove -y build-essential && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /root/.ssh && \  
touch /root/.ssh/known_hosts && \  
ssh-keyscan -t rsa github.com >> /root/.ssh/known_hosts  
  
CMD cd /plugin && msync update --noop  

