#  
# Go Dockerfile  
#  
# https://github.com/dockerfile/go  
#  
# Pull base image.  
FROM wengcan/ubuntu:14.04  
# Install Go  
RUN \  
mkdir -p /goroot && \  
curl http://www.golangtc.com/static/go/1.6/go1.6.linux-amd64.tar.gz | tar xvzf
- -C /goroot --strip-components=1  
  
# Set environment variables.  
ENV GOROOT /goroot  
ENV GOPATH /gopath  
ENV PATH $GOROOT/bin:$GOPATH/bin:$PATH  
  
# Define working directory.  
#WORKDIR /gopath  
WORKDIR /ROOT/  
# Define default command.  
CMD ["zsh"]  

