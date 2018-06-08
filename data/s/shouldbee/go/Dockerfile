FROM ubuntu:14.04  
  
RUN apt-get update -yqq && apt-get install -y mercurial git curl build-
essential  
  
# Install go  
RUN curl \--insecure https://storage.googleapis.com/golang/go1.3.linux-
amd64.tar.gz | tar -C /usr/local -zx  
  
# Define env  
ENV HOME /root  
ENV GOPATH /root/go  
ENV GOROOT /usr/local/go  
ENV PATH $PATH:$GOPATH/bin:$GOROOT/bin  
  
# Install gox  
RUN go get github.com/mitchellh/gox && gox -build-toolchain  

