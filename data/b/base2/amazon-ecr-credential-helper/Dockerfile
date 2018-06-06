##### Intermediate source code layer  
FROM alpine:latest as source  
  
MAINTAINER "base2Services" <itsupport@base2services.com>  
  
ARG SOURCE_SHA1="16f099b"  
ENV SHA1 $SOURCE_SHA1  
  
RUN apk update && apk upgrade && \  
apk add --no-cache bash git openssh make  
  
RUN mkdir /src  
RUN git clone https://github.com/awslabs/amazon-ecr-credential-helper.git /src  
  
RUN cd /src \  
git checkout $SHA1  
  
#### ecr helper is built using go  
FROM golang:1.8-alpine as binaries  
  
COPY \--from=source /src /go/src/github.com/awslabs/amazon-ecr-credential-
helper  
  
# make and bash are dependencies for built system  
RUN apk update && apk upgrade && \  
apk add --no-cache make bash  
  
RUN cd /go/src/github.com/awslabs/amazon-ecr-credential-helper \  
&& make \  
&& cp bin/local/docker-credential-ecr-login /bin  
  
FROM scratch  
  
COPY \--from=binaries /bin/docker-credential-ecr-login /bin/docker-credential-
ecr-login  

