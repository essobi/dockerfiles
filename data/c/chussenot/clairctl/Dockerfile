FROM golang  
RUN curl https://glide.sh/get | sh  
RUN go get -u github.com/jteeuwen/go-bindata  
  
WORKDIR /go/src/github.com/jteeuwen/go-bindata/go-bindata  
RUN go build && chmod +x go-bindata && mv go-bindata /go/bin  
RUN git clone https://github.com/chussenot/clairctl.git
/go/src/github.com/jgsqware/clairctl  
  
WORKDIR /go/src/github.com/jgsqware/clairctl  
RUN glide install -v  
RUN CGO_ENABLED=0 go generate ./clair  
RUN CGO_ENABLED=0 go build  
CMD ["./clairctl"]  

