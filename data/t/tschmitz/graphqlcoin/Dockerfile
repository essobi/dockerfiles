FROM golang:1.10  
WORKDIR /go/src/github.com/Teddy-Schmitz/graphqlCoin  
COPY . .  
  
RUN go get -u github.com/golang/dep/cmd/dep  
RUN dep ensure -v -vendor-only  
RUN CGO_ENABLED=0 GOOS=linux go build -a  
  
FROM alpine:latest  
COPY \--from=0 /go/src/github.com/Teddy-Schmitz/graphqlCoin/graphqlCoin /bin/  
ENTRYPOINT [ "/bin/graphqlCoin" ]  
EXPOSE 5050

