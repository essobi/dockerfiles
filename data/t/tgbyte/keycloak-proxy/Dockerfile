FROM golang:1.9  
RUN set -x \  
&& go get github.com/gambol99/keycloak-proxy \  
&& cd /go/src/github.com/gambol99/keycloak-proxy \  
&& CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o keycloak-proxy .  
  
FROM alpine  
RUN set -x \  
&& apk --no-cache add ca-certificates  
COPY \--from=0 /go/src/github.com/gambol99/keycloak-proxy/keycloak-proxy /  
COPY \--from=0 /go/src/github.com/gambol99/keycloak-proxy/templates/
/templates  
  
EXPOSE 3000  
ENTRYPOINT [ "/keycloak-proxy" ]  

