FROM golang:alpine as build  
WORKDIR /go/src/github.com/dmytroleonenko/go-tcp-morse-echoip  
COPY echoserver.go .  
RUN CGO_ENABLED=0 GOOS=linux go build -a -ldflags '-s' -installsuffix cgo . &&
ls -la  
  
FROM scratch  
COPY \--from=build /go/src/github.com/dmytroleonenko/go-tcp-morse-echoip/go-
tcp-morse-echoip .  
EXPOSE 9999  
CMD ["./go-tcp-morse-echoip"]  

