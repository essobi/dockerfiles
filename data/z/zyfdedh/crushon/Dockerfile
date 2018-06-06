FROM golang:1.8  
ENV PROJECT $GOPATH/src/github.com/zyfdegh/crushon  
WORKDIR $PROJECT  
  
COPY . $PROJECT  
RUN cd $PROJECT && \  
go build -o bin/crushon  
  
CMD ["./bin/crushon"]  

