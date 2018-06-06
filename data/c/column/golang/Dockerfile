FROM column/base:v1  
  
MAINTAINER Column Fang <column.fang@gmail.com>  
  
COPY files /  
  
RUN \  
# Install build tools  
apt-get update && \  
apt-get install -y build-essential pkg-config && \  
  
# Download and install golang binary  
curl -L https://storage.googleapis.com/golang/go1.8.1.linux-amd64.tar.gz >
/tmp/golang.tar.gz && \  
tar xzvf /tmp/golang.tar.gz -C /usr/local && \  
  
# Cleanup  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

