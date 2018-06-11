FROM golang:1.9.2-stretch  
  
RUN apt-get update && \  
apt-get install -y zip unzip python-dev apt-transport-https dirmngr  
# Install AWS CLI tools.  
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip" && \  
unzip awscli-bundle.zip && \  
./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws  
  
RUN VER="17.03.0-ce" && curl -L -o /tmp/docker-$VER.tgz
https://get.docker.com/builds/Linux/x86_64/docker-$VER.tgz && tar -xz -C /tmp
-f /tmp/docker-$VER.tgz && mv /tmp/docker/* /usr/bin  
  
ENV GOPATH /go  
ENV APP_DIR ${GOPATH}/src/github.com  
  
WORKDIR ${APP_DIR}  
  
RUN go get -u github.com/golang/dep/...

