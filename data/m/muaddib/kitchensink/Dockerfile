FROM golang:1-alpine  
RUN apk --no-cache add ca-certificates git  
WORKDIR /go/src/github.com/pijalu/kitchensink  
COPY . .  
RUN go get -v github.com/golang/dep/cmd/dep  
RUN dep ensure -v  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o ks .  
  
FROM alpine:latest  
RUN apk --no-cache add ca-certificates  
WORKDIR /bin  
COPY \--from=0 /go/src/github.com/pijalu/kitchensink/ks .  
ENTRYPOINT ["/bin/ks"]  

