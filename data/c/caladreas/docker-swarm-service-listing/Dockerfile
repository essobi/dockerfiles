FROM golang:latest AS build  
WORKDIR /src  
ENV LAST_UPDATE=20180209  
RUN go get -v github.com/docker/docker/client/...  
RUN go get -v github.com/docker/docker/api/...  
RUN go get -v github.com/gorilla/mux/...  
RUN go get -v github.com/stretchr/testify/...  
ADD . /src  
RUN go test \--cover ./...  
RUN go build -v -tags netgo -o docker-swarm-service-listing  
  
FROM alpine:3.6  
ENV LAST_UPDATE=20171210  
ENV DOCKER_API_VERSION=1.35  
LABEL authors="Joost van der Griendt <joostvdg@gmail.com>"  
LABEL version="0.3.0"  
LABEL description="Docker image for discovering (DFP) proxied services in
Docker Swarm "  
CMD ["docker-swarm-service-listing"]  
HEALTHCHECK \--interval=5s --start-period=3s --timeout=5s CMD wget -qO-
"http://localhost:7777/stacks"  
COPY \--from=build /src/docker-swarm-service-listing /usr/local/bin/docker-
swarm-service-listing  
RUN chmod +x /usr/local/bin/docker-swarm-service-listing

