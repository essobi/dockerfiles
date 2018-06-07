# Start from an Apline linux image with the latest version of Go installed  
# and a workspace (GOPATH) configured at /go.  
FROM golang:alpine  
  
WORKDIR /go/src/app  
  
COPY . .  
  
# Build the itfgolang command inside the container.  
RUN go-wrapper download # "go get -d -v ./..."  
RUN go-wrapper install # "go install -v ./..."  
  
# Document that the service listens on port 8080.  
EXPOSE 8080  
CMD ["go-wrapper", "run"] # ["app"]  

