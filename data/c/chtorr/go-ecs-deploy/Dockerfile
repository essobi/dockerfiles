FROM golang:1.9.3 as builder  
WORKDIR /go/src/github.com/chtorr/go-ecs-deploy/  
COPY . ./  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o go-ecs-deploy
src/main.go  
  
FROM drydock/u16:latest  
WORKDIR /  
COPY \--from=builder /go/src/github.com/chtorr/go-ecs-deploy/go-ecs-deploy .  
CMD ["./go-ecs-deploy"]

