FROM golang:1.7  
ADD . /go/src/github.com/reidsy/retro  
  
RUN go install github.com/reidsy/retro  
  
ENTRYPOINT /go/bin/retro  
  
EXPOSE 9090  

