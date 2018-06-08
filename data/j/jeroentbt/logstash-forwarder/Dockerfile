FROM debian:jessie  
  
MAINTAINER Jeroen Tiebout <jeroen@tinktenk.be>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "\n====> install curl" && \  
apt-get update && \  
apt-get install -y curl  
  
RUN export GOVERSION="1.5.1.linux-amd64" && \  
export GOSHA1="46eecd290d8803887dec718c691cc243f2175fe0" && \  
\  
echo "\n====> install go ${GOVERSION}" && \  
curl -sL https://storage.googleapis.com/golang/go${GOVERSION}.tar.gz >
go.tar.gz && \  
echo "${GOSHA1} go.tar.gz" | sha1sum -c && \  
tar -v -C /usr/local -xzf go.tar.gz && \  
rm go.tar.gz  
  
ENV PATH /usr/local/go/bin:$PATH  
  
RUN export LSFVERSION="0.4.0" && \  
export LSFSHA1="472152233191593a1875e429b9e6e0be8712c811" && \  
\  
echo "\n====> install logstash-forwarder ${LSFVERSION}" && \  
curl -sL https://github.com/elastic/logstash-
forwarder/archive/v${LSFVERSION}.tar.gz > lsf.tar.gz && \  
echo "${LSFSHA1} lsf.tar.gz" | sha1sum -c && \  
mkdir -p /opt/logstash-forwarder && \  
tar -v -C /opt/logstash-forwarder --strip-components 1 -xzf lsf.tar.gz && \  
rm lsf.tar.gz && \  
cd /opt/logstash-forwarder && go build  
  
ENV PATH /opt/logstash-forwarder:$PATH  
  
CMD go version && echo "logstash-forwarder version" $(logstash-forwarder
--version)  

