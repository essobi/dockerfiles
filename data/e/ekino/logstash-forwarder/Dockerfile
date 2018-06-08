# --- LOGSTASH-FORWARDER ---  
FROM ekino/base  
MAINTAINER Matthieu Fronton <fronton@ekino.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV GO_VERSION 1.4.2  
ENV GOROOT=/opt/goroot  
ENV GOPATH=/opt/gopath  
ENV PATH=$GOROOT/bin:$GOPATH/bin:$PATH  
  
RUN mkdir -p /opt/goroot /opt/gopath  
RUN curl -sSL https://storage.googleapis.com/golang/go${GO_VERSION}.linux-
amd64.tar.gz | tar xvz --strip 1 -C /opt/goroot  
  
RUN apt-get update && apt-get install -y git  
RUN git clone git://github.com/elasticsearch/logstash-forwarder.git
/opt/logstash-forwarder  
  
WORKDIR /opt/logstash-forwarder  
RUN go build -o logstash-forwarder  
  
ADD config.json /etc/logstash/config.json  
ADD supervisord.conf /etc/supervisor/conf.d/logstash-forwarder.conf  
ADD logstash-forwarder.sh /start.d/05-logstash-forwarder  

