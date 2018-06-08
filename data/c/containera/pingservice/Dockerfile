# Base this docker container off the official golang docker image.  
# Docker containers inherit everything from their base.  
FROM golang:1.4.2  
# Create a directory inside the container to store all our application and
then make it the working directory.  
RUN mkdir -p /go/src/mandala  
WORKDIR /go/src/mandala  
  
# Copy the example-app directory (where the Dockerfile lives) into the
container.  
ADD . /go/src/mandala  
  
RUN go get github.com/gin-gonic/gin  
RUN go build pingservice.go  
  
EXPOSE 4000  
CMD ./pingservice  

