FROM golang:1.6  
COPY . /go/src/github.com/moul/as-a-service  
WORKDIR /go/src/github.com/moul/as-a-service  
RUN make  
ENTRYPOINT ["/go/src/github.com/moul/as-a-service/moul-as-a-service"]  
EXPOSE 8080  

