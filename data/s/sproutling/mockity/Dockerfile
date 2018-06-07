FROM golang  
  
RUN mkdir /app/  
WORKDIR /app/  
  
RUN go get github.com/wilig/mockity  
RUN go install github.com/wilig/mockity/mockity  
  
ENV GOPATH /go  
  
EXPOSE 8989  
# entrypoint is fed by command and defaults /bin/bash -c  
CMD /go/bin/mockity  

