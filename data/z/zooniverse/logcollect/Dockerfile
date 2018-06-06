FROM golang:1-alpine  
  
RUN apk add --no-cache git  
  
RUN go get github.com/zooniverse/gelfcat  
RUN go install github.com/zooniverse/gelfcat  
  
FROM alpine  
  
COPY \--from=0 /go/bin/gelfcat /usr/local/bin/gelfcat  
  
COPY run.sh /  
  
ENTRYPOINT [ "/run.sh" ]  

