FROM golang  
  
ADD . /go/src/github.com/suzaku/dummage  
  
RUN go install github.com/suzaku/dummage  
  
ENTRYPOINT /go/bin/dummage -host 0.0.0.0  
  
EXPOSE 8000  

