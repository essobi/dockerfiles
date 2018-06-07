FROM golang:1.9  
WORKDIR /go/src/github.com/ohlsont/letsencrypt-reverse-proxy  
  
RUN go get github.com/golang/dep/...  
COPY Gopkg.toml Gopkg.lock ./  
  
COPY ./ ./  
  
RUN dep ensure -vendor-only  
RUN go-wrapper install  
  
CMD ["go-wrapper", "run"]  

