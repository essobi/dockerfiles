FROM golang:1.6-onbuild  
COPY . /go/src/app  
RUN go get -d -v  
RUN go install -v  
  
CMD ["./run.sh"]  

