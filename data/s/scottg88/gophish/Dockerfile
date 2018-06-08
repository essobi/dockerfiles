FROM golang:1.5  
MAINTAINER Scott Gillespie <github@scottgillespie.name>  
  
WORKDIR $GOPATH  
RUN go get -v github.com/gophish/gophish  
WORKDIR $GOPATH/src/github.com/gophish/gophish  
RUN go build -v  
RUN mkdir /app && cp -R $GOPATH/src/github.com/gophish/gophish/* /app/ && rm
-rf $GOPATH  
WORKDIR /app  
RUN sed -i "s|127.0.0.1|0.0.0.0|g" config.json  
RUN sed -i "s|gophish.db|database/gophish.db|g" config.json  
RUN chmod +x ./gophish  
  
VOLUME ["/app/database"]  
EXPOSE 3333 80  
ENTRYPOINT ["./gophish"]  

