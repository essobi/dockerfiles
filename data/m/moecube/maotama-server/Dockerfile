FROM golang  
  
RUN mkdir -p /go/src/app  
WORKDIR /go/src/app  
  
CMD ["go-wrapper", "run"]  
  
COPY . /go/src/app  
RUN go-wrapper download  
RUN go-wrapper install

