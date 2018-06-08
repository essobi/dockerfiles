FROM golang:alpine AS builder  
  
WORKDIR /go/src/github.com/99designs/ecs-upload-task  
  
COPY . .  
  
RUN CGO_ENABLED=0 go install -v .  
  
FROM scratch  
  
COPY \--from=builder ["/go/bin/ecs-upload-task", "/ecs-upload-task"]  
  
ENTRYPOINT ["/ecs-upload-task"]  

