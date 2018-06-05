# =======  
# Builder  
# =======  
FROM abiosoft/caddy:builder as builder  
  
ARG version  
ARG plugins="git,cloudflare"  
# process wrapper  
RUN go get -v github.com/abiosoft/parent  
  
RUN VERSION=${version} PLUGINS=${plugins} /bin/sh /usr/bin/builder.sh  
  
# ===========  
# Final stage  
# ===========  
FROM alpine:3.7  
LABEL maintainer="Jesse Stuart <hi@jessestuart.com>"  
  
ARG version=  
LABEL caddy_version="$version"  
  
# Let's Encrypt Agreement  
ENV ACME_AGREE="true"  
RUN apk add --no-cache openssh-client git  
  
# install caddy  
COPY \--from=builder /install/caddy /usr/bin/caddy  
  
# validate install  
RUN caddy -version && caddy -plugins  
  
EXPOSE 80 443 2015  
VOLUME /root/.caddy /srv  
WORKDIR /srv  
  
COPY Caddyfile /etc/Caddyfile  
  
# install process wrapper  
COPY \--from=builder /go/bin/parent /bin/parent  
  
ENTRYPOINT ["/bin/parent", "caddy"]  
CMD ["--conf", "/etc/Caddyfile", "--log", "stdout", "--agree=$ACME_AGREE"]  

