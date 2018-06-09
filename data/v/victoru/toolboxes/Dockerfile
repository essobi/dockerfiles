FROM golang:1.8-alpine  
  
ENV GLIDE_VERSION 0.13.0  
RUN apk --no-cache add \  
git \  
make \  
curl  
  
RUN go get -u github.com/golang/dep/cmd/dep  
RUN curl -SsL
https://github.com/Masterminds/glide/releases/download/v$GLIDE_VERSION/glide-v$GLIDE_VERSION-
linux-amd64.tar.gz \  
| tar -zxvf - -C /tmp \  
&& mv /tmp/linux-amd64/glide /usr/bin \  
&& rm -rf /tmp/linux-amd64  

