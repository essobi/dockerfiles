FROM nuagebec/ubuntu:14.04  
MAINTAINER Michaël Faille <michael@faille.pw>  
# Let's install (from source).  
  
  
RUN apt-get update -q && \  
DEBIAN_FRONTEND=noninteractive apt-get install -qy build-essential --no-
install-recommends && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
wget -O - https://storage.googleapis.com/golang/go1.4.2.src.tar.gz | tar -v -C
/usr/local -xzi && cd /usr/local/go/src && \  
./make.bash --no-clean 2>&1 && \  
mkdir -p /data/persistent/gopath && \  
apt-get remove -y --purge build-essential  
  
  
ENV PATH /data/gopath/bin:/usr/local/go/bin:$PATH  
ENV GOPATH /data/persitent/gopath  
  
CMD ["bash"]  

