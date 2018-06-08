FROM golang:latest AS build  
WORKDIR /src  
ENV LAST_UPDATE=20171020  
RUN go get -v github.com/gorilla/mux/...  
ADD . /src  
RUN go build -v -tags netgo -o docker-swarm-service-listing-ui  
  
FROM alpine:3.6  
ENV LAST_UPDATE=20171210  
LABEL authors="Joost van der Griendt <joostvdg@gmail.com>"  
LABEL version="0.2.0"  
LABEL description="Docker image for listing (DFP) proxied services in Docker
Swarm "  
CMD ["docker-swarm-service-listing-ui"]  
ENV API_HOST="api" \  
API_PROTOCOL="http" \  
API_PORT="7777" \  
SERVER_PORT="8087" \  
TEMPLATE_ROOT="/srv/"  
HEALTHCHECK \--interval=5s --start-period=3s --timeout=5s CMD wget -qO-
"http://localhost:$SERVER_PORT/"  
COPY \--from=build /src/docker-swarm-service-listing-ui /usr/local/bin/docker-
swarm-service-listing-ui  
COPY index.html /srv/  
RUN chmod +x /usr/local/bin/docker-swarm-service-listing-ui

