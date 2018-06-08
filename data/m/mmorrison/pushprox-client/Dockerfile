FROM golang:1.10  
COPY ./ /go/src/github.com/robustperception/pushprox/  
WORKDIR /go/src/github.com/robustperception/pushprox/client/  
RUN go get -v \  
&& CGO_ENABLED=0 GOOS=linux go build -v .  
  
FROM debian:stable  
RUN apt-get -y update && \  
apt-get -y install ca-certificates  
WORKDIR /root/  
COPY \--from=0 /go/src/github.com/robustperception/pushprox/client/client
/bin/client  
USER nobody  
ENTRYPOINT [ "/bin/client" ]  

