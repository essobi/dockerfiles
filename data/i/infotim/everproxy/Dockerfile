FROM golang:1.3.3  
RUN go get github.com/infotim/everproxy &&\  
go install github.com/infotim/everproxy  
  
EXPOSE 8080  
ENV DATA_DIR /data/  
ENTRYPOINT /go/bin/everproxy  

