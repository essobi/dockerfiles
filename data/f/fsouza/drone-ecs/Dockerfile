FROM golang:1.9-alpine AS builder  
  
ENV CGO_ENABLED 0  
ADD . /go/src/github.com/josmo/drone-ecs  
RUN go install github.com/josmo/drone-ecs  
  
FROM alpine:3.7  
RUN apk add --no-cache ca-certificates  
COPY \--from=builder /go/bin/drone-ecs /bin/drone-ecs  
  
ENTRYPOINT ["/bin/drone-ecs"]  

