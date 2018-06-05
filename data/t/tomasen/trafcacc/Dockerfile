FROM golang:latest  
MAINTAINER Tomasen "https://github.com/tomasen"  
# Copy the local package files to the container's workspace.  
ADD . /go/src/github.com/tomasen/trafcacc  
  
# change workdir, build and install  
WORKDIR /go/src/github.com/tomasen/trafcacc  
RUN go get .  
RUN go install -race  
  
RUN rm -rf /go/src/*  
WORKDIR /go/bin  
  
# you need to run the trafcacc command manually  
# ENTRYPOINT /go/bin/trafcacc  
# EXPOSE 4043  

