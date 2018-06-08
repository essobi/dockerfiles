FROM golang:latest  
MAINTAINER PierreZ  
  
# Copy the local package files to the container's workspace.  
ADD . /go/src/github.com/youcodeio/proxy  
WORKDIR /go/src/github.com/youcodeio/proxy  
RUN go get  
RUN go install  
  
# Run the outyet command by default when the container starts.  
ENTRYPOINT /go/bin/proxy  
  
# Document that the service listens on port 8080.  
EXPOSE 7777  

