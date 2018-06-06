# Build  
FROM golang:1.9-alpine as build  
  
RUN apk --no-cache add git  
RUN go get -u github.com/golang/dep/cmd/dep  
WORKDIR /go/src/github.com/computes/fibonacci-sum-split  
COPY . /go/src/github.com/computes/fibonacci-sum-split  
  
RUN dep ensure  
  
RUN env CGO_ENABLED=0 go build -o fibonacci-sum-split -a -ldflags '-s' .  
  
# Entrypoint  
FROM scratch  
  
EXPOSE 80  
COPY \--from=build /go/src/github.com/computes/fibonacci-sum-split/fibonacci-
sum-split /fibonacci-sum-split  
ENTRYPOINT ["./fibonacci-sum-split"]  

