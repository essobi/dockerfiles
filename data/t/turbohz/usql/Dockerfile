FROM golang:1.6.4-alpine  
  
RUN apk add --update git bash make alpine-sdk && rm -rf /var/cache/apk/*  
ADD . /root/  
WORKDIR /root/  
RUN go get -u github.com/knq/usql  
ENTRYPOINT ["usql"]  

