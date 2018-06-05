FROM golang:latest AS builder  
  
RUN go get github.com/mholt/caddy/caddy \  
&& go get github.com/caddyserver/dnsproviders/azure \  
&& go get github.com/caddyserver/dnsproviders/googlecloud \  
&& go get github.com/caddyserver/dnsproviders/route53 \  
&& go get github.com/caddyserver/forwardproxy \  
&& go get github.com/caddyserver/builds  
RUN cd /go/src/github.com/mholt/caddy/caddy \  
&& git checkout v0.11.0 \  
&& sed -i -e "/This is where other plugins get plugged in (imported)/a\\\\\t_
\"github.com/caddyserver/dnsproviders/azure\"\n\t_
\"github.com/caddyserver/dnsproviders/googlecloud\"\n\t_
\"github.com/caddyserver/dnsproviders/route53\"\n\t_
\"github.com/caddyserver/forwardproxy\""
/go/src/github.com/mholt/caddy/caddy/caddymain/run.go \  
&& go run build.go  
WORKDIR /tmp/rootfs  
RUN mkdir -p etc/caddy etc/ssl/certs usr/bin \  
&& cp /go/src/github.com/mholt/caddy/caddy/caddy usr/bin \  
&& cp /etc/ssl/certs/ca-certificates.crt etc/ssl/certs  
  
FROM scratch  
  
COPY --from=builder /tmp/rootfs /  
WORKDIR /webroot  
EXPOSE 80 443  
ENTRYPOINT [ "/usr/bin/caddy" ]  
CMD [ "--conf", "/etc/caddy/Caddyfile", "--log", "stdout", "--root",
"/var/tmp" ]  

