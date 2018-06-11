FROM golang  
MAINTAINER Tim Fall <tim@vapor.io>  
  
WORKDIR /go/src/github.com/vapor-ware/synse-cli  
  
COPY ./ ./  
  
RUN go get -v  
RUN go build -v -o /go/bin/synse  
  
EXPOSE 6060  
RUN /go/bin/synse shell-completion --bash  
RUN /bin/bash -c "source /etc/bash_completion.d/synse"  
  
ENTRYPOINT ["synse"]  
CMD ["-h"]  

