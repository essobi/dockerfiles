FROM golang:latest  
MAINTAINER Tomasen "https://github.com/tomasen"  
RUN apt-get update && apt-get install -y autoconf && \  
apt-get clean autoclean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
# Copy the local package files to the container's workspace.  
ADD . /go/src/github.com/xindong/corvus  
  
# change workdir, build and install  
WORKDIR /go/src/github.com/xindong/corvus  
RUN git submodule update --init  
RUN make deps  
RUN make  
RUN cp /go/src/github.com/xindong/corvus/src/corvus /go/bin/  
RUN rm -rf /go/src/*  
  
WORKDIR /go/bin  
  
# Run the frontd command by default when the container starts.  
ENTRYPOINT /go/bin/corvus  
  
EXPOSE 6380  

