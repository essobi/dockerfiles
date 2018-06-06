FROM strebul/go-builder1.9.2-alpine3.6 as builder  
WORKDIR /go/src/github.com/2at2/covery-mock  
COPY . .  
RUN set -ex \  
&& go get ./... \  
&& go test ./... \  
&& go build -o covery main/main.go  
  
FROM alpine:3.6  
COPY \--from=builder /go/src/github.com/2at2/covery-mock/covery
/usr/bin/covery  
ENTRYPOINT ["covery"]  

