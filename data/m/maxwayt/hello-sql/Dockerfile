FROM golang:latest  
  
COPY . /go/src/app  
  
WORKDIR /go/src/app  
  
RUN go get -d -v  
RUN go install -v  
  
EXPOSE 8080  
CMD /go/bin/app  

