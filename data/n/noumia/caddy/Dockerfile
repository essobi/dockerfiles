FROM golang:1.9  
  
RUN set -x \  
&& go get github.com/caddyserver/builds \  
&& go get github.com/mholt/caddy/caddy \  
&& cd /go/src/github.com/mholt/caddy \  
&& git checkout -b v0.10.10 \  
&& cd caddy \  
&& go run build.go \  
&& mkdir -p /go/opt/bin \  
&& mv caddy /go/opt/bin/  
  
  
FROM buildpack-deps:stretch-curl  
  
COPY --from=0 /go/opt /opt  
  
ENV PATH=/opt/bin:${PATH}  
  
EXPOSE 80 443  
  
VOLUME /root  
  
WORKDIR /root  
  
CMD [ "caddy", "-agree" ]  

