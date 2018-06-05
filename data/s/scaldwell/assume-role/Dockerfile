FROM golang:1.9.2  
  
RUN go get -d -v github.com/remind101/assume-role  
  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo \  
-o /opt/assume-role \  
github.com/remind101/assume-role  

