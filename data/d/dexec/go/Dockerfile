FROM debian:8.0  
MAINTAINER andystanton  
ENV GO_VERSION 1.4.2  
ENV PATH $PATH:/usr/local/go/bin  
RUN apt-get update -qq -y && \  
apt-get install patch wget -y && \  
wget https://storage.googleapis.com/golang/go${GO_VERSION}.linux-amd64.tar.gz
&& \  
tar -C /usr/local -xzf go${GO_VERSION}.linux-amd64.tar.gz && \  
rm go${GO_VERSION}.linux-amd64.tar.gz && \  
apt-get remove -y wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
ADD image-common /tmp/dexec/image-common  
VOLUME /tmp/dexec/build  
ENTRYPOINT ["/tmp/dexec/image-common/dexec-script.sh", "go run"]  

