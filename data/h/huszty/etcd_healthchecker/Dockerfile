FROM alpine  
  
ADD main.go /go/  
  
RUN apk add \--no-cache go git libc-dev; \  
export GOPATH=/go; \  
cd /go; \  
go get -v; \  
go build main.go; \  
mv main /; \  
rm -rf /go; \  
apk del go git libc-dev;  
  
CMD ["/main"]  
  

