FROM golang  
  
RUN go get -u github.com/golang/dep/cmd/dep  
  
COPY . /go/src/app  
  
WORKDIR /go/src/app  
  
RUN dep ensure  
  
RUN make  
  
USER nobody  
  
ENTRYPOINT /go/src/app/gohost  

