#  
# Builder  
#  
FROM golang:1.10-alpine as builder  
  
ARG version="0.11.0"  
ARG plugins="git"  
RUN apk add --no-cache curl git  
  
# caddy  
RUN git clone https://github.com/mholt/caddy -b "v${version}"
/go/src/github.com/mholt/caddy \  
&& cd /go/src/github.com/mholt/caddy \  
&& git checkout -b "v${version}"  
  
# plugin helper  
RUN go get -v github.com/abiosoft/caddyplug/caddyplug  
  
# plugins  
RUN for plugin in $(echo $plugins | tr "," " "); do \  
go get -v $(caddyplug package $plugin); \  
printf "package caddyhttp\nimport _ \"$(caddyplug package $plugin)\"" > \  
/go/src/github.com/mholt/caddy/caddyhttp/$plugin.go ; \  
done  
  
# builder dependency  
RUN git clone https://github.com/caddyserver/builds
/go/src/github.com/caddyserver/builds  
  
# build  
RUN cd /go/src/github.com/mholt/caddy/caddy \  
&& git checkout -f \  
&& go run build.go \  
&& mv caddy /go/bin  
  
# confd  
RUN curl --silent --show-error --fail --location \  
https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-
amd64 > /usr/bin/confd \  
&& chmod 0755 /usr/bin/confd  
  
#  
# Final stage  
#  
FROM alpine:3.6  
ENV HOME /etc/caddy  
  
RUN apk add --no-cache ca-certificates git  
  
# install caddy  
COPY \--from=builder /go/bin/caddy /usr/bin/caddy  
COPY \--from=builder /usr/bin/confd /usr/bin/confd  
  
COPY Caddyfile /etc/caddy/  
COPY vhosts /etc/caddy/vhosts  
COPY run.sh /  
  
# Copy confd files  
COPY confd_files /etc/confd/  
  
EXPOSE 80 443 8000  
CMD ["./run.sh"]  

