FROM ontouchstart/python3.6-notebook:minimal  
USER root  
  
# Ports for Swarm TCP, Swarm uTP, API, Gateway  
EXPOSE 4001  
EXPOSE 4002/udp  
EXPOSE 5001  
EXPOSE 8080  
# IPFS API to use for fetching gx packages.  
# This can be a gateway too, since its read-only API provides all gx needs.  
# - e.g. /ip4/172.17.0.1/tcp/8080 if the Docker host  
# has the IPFS gateway listening on the bridge interface  
# provided by Docker's default networking.  
# - if empty, the public gateway at ipfs.io is used.  
ENV GX_IPFS ""  
# The IPFS fs-repo within the container  
ENV IPFS_PATH /data/ipfs  
# The default logging level  
ENV IPFS_LOGGING ""  
# Golang stuff  
ENV GOPATH /go  
ENV SRC_PATH /go/src/github.com/ipfs/go-ipfs  
ENV GOROOT /usr/local/go  
ENV PATH $GOPATH/bin:$GOROOT/bin:$PATH  
  
RUN apt-get update -y  
RUN cd /usr/local && wget https://storage.googleapis.com/golang/go1.8.2.linux-
amd64.tar.gz && tar -xzvf go1.8.2.linux-amd64.tar.gz  
  
RUN go get -u -d github.com/ipfs/go-ipfs  
RUN cd $GOPATH/src/github.com/ipfs/go-ipfs && make install  
RUN ipfs --help  
RUN go version  
RUN ipfs --version  

