# Build  
FROM golang:1.9-alpine as build  
  
RUN apk --no-cache add git  
RUN go get -u github.com/golang/dep/cmd/dep  
WORKDIR /go/src/github.com/computes/fibonacci-sum-sum  
COPY . /go/src/github.com/computes/fibonacci-sum-sum  
  
RUN dep ensure  
  
RUN env CGO_ENABLED=0 go build -o fibonacci-sum-sum -a -ldflags '-s' .  
  
# Entrypoint  
FROM scratch  
  
EXPOSE 80  
COPY \--from=build /go/src/github.com/computes/fibonacci-sum-sum/fibonacci-
sum-sum /fibonacci-sum-sum  
ENTRYPOINT ["./fibonacci-sum-sum"]  

