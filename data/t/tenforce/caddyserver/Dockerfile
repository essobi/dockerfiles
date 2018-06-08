FROM golang:alpine as build  
  
# Install git and get the caddy and git plugin source code  
RUN apk --update add git  
RUN go get github.com/mholt/caddy/caddy  
RUN go get github.com/abiosoft/caddy-git  
  
# Checkout the latest stable release (git plugin does not release version, use
master)  
WORKDIR /go/src/github.com/mholt/caddy  
RUN git tag -l --sort=-creatordate | grep -v beta | head -n 1 | xargs git
checkout  
  
# Splice the plugin into the code and run build  
WORKDIR /go/src/github.com/mholt/caddy/caddy  
RUN go get github.com/wdullaer/go-import-manager  
RUN go-import-manager add -i caddymain/run.go '_ "github.com/abiosoft/caddy-
git"'  
RUN go build  
  
FROM alpine:latest  
  
EXPOSE 80  
EXPOSE 443  
RUN apk add --no-cache git  
COPY \--from=build /go/src/github.com/mholt/caddy/caddy/caddy /  
RUN mkdir /config  
COPY Caddyfile /config/Caddyfile  
VOLUME /config  
  
CMD ["/caddy", "-conf", "/config/Caddyfile"]  

