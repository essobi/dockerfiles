FROM nanoservice/fanout:base  
ADD . /go/src/github.com/nanoservice/core-fanout/fanout  
  
RUN go test  
RUN go install  
  
EXPOSE 6777  
ENTRYPOINT ["fanout"]  

