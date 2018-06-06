FROM golang:latest  
MAINTAINER Tomasen "https://github.com/tomasen"  
# Copy the local package files to the container's workspace.  
ADD . /go/src/github.com/PinIdea/gapps-crawler  
  
# change workdir, build and install  
WORKDIR /go/src/github.com/PinIdea/gapps-crawler  
RUN go get .  
RUN go install  
  
RUN rm -rf /go/src/*  
WORKDIR /go/bin  
  
# Run the frontd command by default when the container starts.  
ENTRYPOINT /go/bin/gapps-crawler  

