FROM abiosoft/caddy:builder as builder  
  
RUN go get -v github.com/abiosoft/parent  
RUN VERSION="0.11.0" PLUGINS="filemanager cache" ENABLE_TELEMETRY="false"
/bin/sh /usr/bin/builder.sh  
  
FROM alpine:3.7  
LABEL caddy_version="0.11.0"  
  
ENV ENABLE_TELEMETRY="false"  
RUN apk add --no-cache openssh-client ca-certificates  
  
COPY \--from=builder /install/caddy /usr/bin/caddy  
  
RUN /usr/bin/caddy -version  
RUN /usr/bin/caddy -plugins  
  
EXPOSE 80 443 2015  
VOLUME /root/.caddy /srv  
WORKDIR /srv  
  
ENTRYPOINT ["/bin/parent", "caddy"]  
CMD ["--conf", "/etc/Caddyfile", "--log", "stdout", "--agree"]  

