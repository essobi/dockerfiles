###########################  
# repco/perfect_common #  
##########################  
FROM ubuntu:14.04  
  
MAINTAINER Colin Hom  
  
# Update the repository  
RUN apt-get update  
  
RUN apt-get -y --no-install-recommends install git mercurial bzr curl wget ca-
certificates  
RUN mkdir -p /goroot && \  
mkdir -p /root/gopath && \  
wget https://storage.googleapis.com/golang/go1.4.1.linux-amd64.tar.gz -O - |
tar xvzf - -C /goroot --strip-components=1  
ENV GOROOT /goroot  
ENV GOPATH /root/gopath  
  
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin  
  
WORKDIR /root/gopath  
  
ENTRYPOINT ["/goroot/bin/go"]  
  

