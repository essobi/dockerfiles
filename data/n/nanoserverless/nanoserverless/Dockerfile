FROM golang:1.7  
WORKDIR /go/src  
COPY shell2http /  
ENV CGO_ENABLED=0  
ENV GO_PATH=/go/src  
RUN go get -v github.com/gorilla/mux github.com/docker/docker/client
github.com/docker/docker/api/types  
COPY . /go/src  
RUN go build -v -a --installsuffix cgo \--ldflags=-s -o nanoserverless  
CMD ["/go/src/nanoserverless"]  
EXPOSE 80  

