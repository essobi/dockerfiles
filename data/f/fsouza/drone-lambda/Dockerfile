FROM golang:1.9-alpine AS build  
ENV CGO_ENABLED 0  
ADD . /go/src/github.com/omerxx/drone-lambda-plugin  
RUN go install github.com/omerxx/drone-lambda-plugin  
  
FROM alpine:3.6  
RUN apk add --no-cache ca-certificates  
COPY \--from=build /go/bin/drone-lambda-plugin /bin/main  
ENTRYPOINT ["/bin/main"]  

