FROM golang:1.8  
ADD ./ /go  
  
RUN go get -u github.com/go-redis/redis  
RUN go get github.com/astaxie/beego  
RUN go get github.com/astaxie/beego/logs  
  
RUN go build -o memo .  
  
CMD ["/go/memo"]

