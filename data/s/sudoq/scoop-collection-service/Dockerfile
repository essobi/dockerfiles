FROM golang:latest  
  
ADD . /go/src/github.com/SudoQ/scoop-collection-service  
ADD ./amqputil /go/src/github.com/SudoQ/scoop-collection-service/amqputil  
  
RUN go get github.com/streadway/amqp  
RUN go get github.com/gorilla/mux  
  
RUN go install github.com/SudoQ/scoop-collection-service  
  
ENTRYPOINT /go/bin/scoop-collection-service  
  
EXPOSE 8080  

