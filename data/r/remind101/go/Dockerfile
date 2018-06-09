FROM golang:1.5  
MAINTAINER Ben Marini <ben@remind101.com>  
  
# --------------------------  
# Install NewRelic Agent SDK  
# --------------------------  
  
RUN apt-get update && apt-get install -y \  
libboost-all-dev libcurl4-openssl-dev \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV NEWRELIC_SDK_VERSION 0.16.2.0  
  
RUN mkdir -p /go/src/app  
WORKDIR /go/src/app  
  
CMD ["/go/bin/app"]  
  
RUN curl -sSL
http://download.newrelic.com/agent_sdk/nr_agent_sdk-v$NEWRELIC_SDK_VERSION-
beta.x86_64.tar.gz | tar zx && \  
cp nr_agent_sdk-v$NEWRELIC_SDK_VERSION-beta.x86_64/bin/newrelic-collector-
client-daemon /usr/local/bin/ && \  
mkdir -p /usr/local/lib && \  
cp nr_agent_sdk-v$NEWRELIC_SDK_VERSION-beta.x86_64/lib/* /usr/local/lib && \  
mkdir -p /usr/local/include && \  
cp nr_agent_sdk-v$NEWRELIC_SDK_VERSION-beta.x86_64/include/*
/usr/local/include && \  
ldconfig  
  
# You'll want to have something like this in your Dockerfile:  
# FROM remind101/go:1.5-newrelic  
# COPY . /go/src/app  
# RUN go-wrapper download -tags newrelic_enabled ./...  
# RUN go-wrapper install -tags newrelic_enabled ./...  

