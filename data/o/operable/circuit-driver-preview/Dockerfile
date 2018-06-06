FROM alpine:3.4  
  
MAINTAINER Kevin Smith <kevin@operable.io>  
  
RUN mkdir -p /operable/circuit/bin && \  
mkdir -p /tmp/src/github.com/operable/circuit-driver/ && \  
mkdir -p /tmp/src/github.com/operable/circuit-driver/api && \  
mkdir -p /tmp/src/github.com/operable/circuit-driver/io && \  
mkdir -p /tmp/src/github.com/operable/circuit-driver/util  
  
COPY main.go /tmp/src/github.com/operable/circuit-driver  
COPY Makefile /tmp/src/github.com/operable/circuit-driver  
COPY api /tmp/src/github.com/operable/circuit-driver/api  
COPY io /tmp/src/github.com/operable/circuit-driver/io  
COPY util /tmp/src/github.com/operable/circuit-driver/util  
  
RUN apk add -U --no-cache go make ca-certificates git && \  
cd /tmp/src/github.com/operable/circuit-driver && \  
GOPATH=/tmp make exe && cp _build/circuit-driver /operable/circuit/bin && cd /
&& rm -rf /tmp/src && \  
apk del go make git  
  
VOLUME /operable/circuit

