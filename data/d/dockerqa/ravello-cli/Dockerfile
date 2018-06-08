FROM debian:stretch  
MAINTAINER qa@docker.com  
  
ENV BUILD_PACKAGES openssl curl  
ENV DEBIAN_FRONTEND noninteractive  
WORKDIR /app  
ENTRYPOINT ["/app/ravello_cli/ravello"]  
CMD ["--help"]  
  
COPY ravello_linux.tar.gz.sha256 /app/ravello_linux.tar.gz.sha256  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y $BUILD_PACKAGES && \  
curl -sSLO http://import-tool.ravellosystems.com/linux/ravello_linux.tar.gz &&
\  
sha256sum -c ravello_linux.tar.gz.sha256 && \  
tar xzvf ravello_linux.tar.gz && \  
apt-get remove -y $BUILD_PACKAGES && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* ravello_linux.tar.gz
ravello_linux.tar.gz.sha256 && \  
ravello_cli/ravello --help  

