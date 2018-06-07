# Compile binary  
FROM golang:alpine as compile  
  
COPY httpd.go .  
RUN CGO_ENABLED=0 go build -i httpd.go  
  
# Make actual image  
FROM scratch  
  
COPY \--from=compile /go/httpd /httpd  
  
ENTRYPOINT ["/httpd"]  

