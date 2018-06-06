FROM golang:1.5.3  
RUN apt-get update \  
&& apt-get install -y curl  
RUN curl -sSL https://get.docker.com/ | sh  
  
RUN go get github.com/Gingonic/rabbitmq-cli-consumer  
  
WORKDIR $GOPATH/src/github.com/Gingonic/rabbitmq-cli-consumer  
RUN git checkout 2.0  
RUN go get ./...  
RUN go build  
RUN go install  
  

