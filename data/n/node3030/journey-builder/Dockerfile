FROM golang:1.8-alpine  
  
RUN apk update && apk add --no-cache ca-certificates \  
&& apk add git  
  
ADD entry.sh /go/  
  
RUN chmod +x /go/entry.sh  
ENTRYPOINT /go/entry.sh  

