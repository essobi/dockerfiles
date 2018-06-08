FROM golang  
  
ADD . /go/src/github.com/rudes/runestats  
RUN cd /go/src/github.com/rudes/runestats; go get  
RUN go install github.com/rudes/runestats/statapi  
RUN go install github.com/rudes/runestats/statimage  
RUN go install github.com/rudes/runestats  
ENTRYPOINT /go/bin/runestats  
  
EXPOSE 8080  

