FROM golang:latest AS builder  
  
RUN go get github.com/yukimochi/caddy/caddy \  
&& go get github.com/yukimochi/caddy-cache \  
&& go get github.com/yukimochi/forwardproxy \  
&& go get github.com/caddyserver/builds \  
&& sed -i -e "/This is where other plugins get plugged in (imported)/a\\\\\t_
\"github.com/yukimochi/caddy-cache\"\n\t_
\"github.com/yukimochi/forwardproxy\""
/go/src/github.com/yukimochi/caddy/caddy/caddymain/run.go \  
&& sed -i -e "s/github.com\/mholt/github.com\/yukimochi/"
/go/src/github.com/caddyserver/builds/compilation.go  
RUN cd /go/src/github.com/yukimochi/caddy/caddy && go run build.go  
WORKDIR /tmp/rootfs  
RUN mkdir -p etc/caddy etc/ssl/certs usr/bin \  
&& cp /go/src/github.com/yukimochi/caddy/caddy/caddy usr/bin \  
&& cp /etc/ssl/certs/ca-certificates.crt etc/ssl/certs  
  
FROM scratch  
  
COPY --from=builder /tmp/rootfs /  
WORKDIR /webroot  
EXPOSE 80 443  
ENTRYPOINT [ "/usr/bin/caddy" ]  
CMD [ "--conf", "/etc/caddy/Caddyfile", "--log", "stdout", "--root",
"/var/tmp" ]  

