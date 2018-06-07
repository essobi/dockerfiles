FROM golang:1.9-alpine3.6  
MAINTAINER Alexey Kovrizhkin <lekovr+dopos@gmail.com>  
  
ENV WEBHOOK_VERSION 2.6.5  
WORKDIR /go/src/github.com/adnanh  
  
RUN apk --update add curl git  
  
# with CGO_ENABLED=0 build does not requires g++ package, so it will be faster  
RUN curl -sL
https://github.com/adnanh/webhook/archive/${WEBHOOK_VERSION}.tar.gz | tar -xvz
\  
&& mv -f webhook-${WEBHOOK_VERSION} webhook \  
&& cd webhook \  
&& go-wrapper download \  
&& CGO_ENABLED=0 GOOS=linux go build -a -o webhook  
  
#
------------------------------------------------------------------------------  
# Second build stage, so use cloud.docker.com instead hub.docker.com for
autobuild  
# Base on docker/alpine in case of docker using in hooks  
FROM docker:17.07.0-ce  
  
# Stuff used in hooks  
RUN apk --update add curl curl-dev make bash git apache2-utils jq openssh-
client  
  
# Main app will be placed in root  
WORKDIR /  
  
COPY \--from=0 /go/src/github.com/adnanh/webhook/webhook .  
  
COPY webhook /etc/webhook  
  
# webhook default port  
EXPOSE 9000  
ENTRYPOINT ["/webhook"]  

