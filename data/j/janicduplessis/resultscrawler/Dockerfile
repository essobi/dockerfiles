FROM golang:1.4-wheezy  
  
RUN go get github.com/janicduplessis/resultscrawler/crawler  
WORKDIR /go/src/github.com/janicduplessis/resultscrawler/crawler  
  
CMD ["/go/bin/crawler"]  
  
EXPOSE 9898  

