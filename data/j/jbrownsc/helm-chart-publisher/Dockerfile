FROM alpine:latest  
  
RUN apk add \--no-cache ca-certificates go git build-base  
  
RUN mkdir -p /opt/sightmachine/go/src/github.com/luizbafilho  
COPY . /opt/sightmachine/go/src/github.com/luizbafilho/helm-chart-publisher  
  
ENV GOPATH=/opt/sightmachine/go  
  
WORKDIR /opt/sightmachine/go/src/github.com/luizbafilho/helm-chart-publisher  
  
RUN go get  
  
RUN go build  
  
# Docker cp /opt/sightmachine/go/src/github.com/luizbafilho/helm-chart-
publisher/helm-chart-publisher .  

