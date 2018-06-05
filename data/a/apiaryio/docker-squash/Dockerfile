FROM golang:1.6  
RUN apt-get update  
RUN apt-get -y install sudo  
  
COPY . /go/src/github.com/apiaryio/docker-squash  
  
ADD
https://github.com/Masterminds/glide/releases/download/0.9.1/glide-0.9.1-linux-
amd64.tar.gz /tmp/glide-0.9.1-linux-amd64.tar.gz  
RUN cd /tmp && \  
tar -zxvf /tmp/glide-0.9.1-linux-amd64.tar.gz && \  
cp /tmp/linux-amd64/glide /usr/local/bin/glide && \  
chmod 755 /usr/local/bin/glide && \  
rm /tmp/glide-0.9.1-linux-amd64.tar.gz && rm -rf /tmp/linux-amd64/  
  
RUN cd /go/src/github.com/apiaryio/docker-squash && \  
glide install && \  
go install -ldflags "-X main.version=$VERSION" ./...  

