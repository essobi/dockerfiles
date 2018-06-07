FROM golang:1.7  
RUN go get -u github.com/jstemmer/go-junit-report  
  
COPY test-and-report.sh /  
  
ENTRYPOINT ["/test-and-report.sh"]  

