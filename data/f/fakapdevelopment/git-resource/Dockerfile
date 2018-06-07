FROM golang:1.8-alpine  
  
ENV GOPATH=/root/go  
ENV CGO_ENABLED=0  
ENV GOOS=linux  
  
COPY cmd /root/go/src/bitbucket.org/fakapdevelopment/git-resource/cmd  
  
RUN go install bitbucket.org/fakapdevelopment/git-resource/cmd/common \  
&& go install bitbucket.org/fakapdevelopment/git-resource/cmd/check \  
&& go install bitbucket.org/fakapdevelopment/git-resource/cmd/in \  
&& go install bitbucket.org/fakapdevelopment/git-resource/cmd/out  
  
  
FROM alpine  
  
RUN apk add \--no-cache \  
git openssh bash  
  
ENV GIT_USER_NAME='Fakap Development CI'  
ENV GIT_USER_EMAIL='ci@fakapdevelopment.com'  
  
COPY \--from=0 /root/go/bin /opt/resource  
  
WORKDIR /tmp

