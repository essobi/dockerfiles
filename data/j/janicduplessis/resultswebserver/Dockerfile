FROM janicduplessis/golang-bower  
  
RUN go get github.com/janicduplessis/resultscrawler/webserver  
WORKDIR /go/src/github.com/janicduplessis/resultscrawler/webserver  
RUN \  
cd /go/src/github.com/janicduplessis/resultscrawler/webserver && \  
bower --allow-root --config.interactive=false install  
  
CMD []  
ENTRYPOINT ["/go/bin/webserver"]  
  
EXPOSE 8080 8081  

