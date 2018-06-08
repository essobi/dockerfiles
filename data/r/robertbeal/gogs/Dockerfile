FROM alpine:3.7  
ENV GOGS_VERSION=0.11.53  
ENV OVERLAY_VERSION=1.21.4.0  
ENV GOPATH /gopath  
ENV PATH $PATH:$GOPATH/bin  
  
WORKDIR /gopath/src/github.com/gogs/gogs  
  
ARG UID=801  
ARG GID=801  
RUN apk add --no-cache \  
bash \  
ca-certificates \  
curl \  
git \  
linux-pam \  
openssh \  
shadow \  
&& addgroup -g $GID git \  
&& adduser -s /bin/bash -D -h /data -u $UID -G git git \  
&& usermod -p '*' git \  
&& passwd -u git \  
&& apk add --no-cache --virtual=build-dependencies \  
alpine-sdk \  
go \  
linux-pam-dev \  
&& curl -L "https://github.com/just-
containers/s6-overlay/releases/download/v${OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz" | tar zx -C / \  
&& curl -L https://github.com/gogs/gogs/archive/v$GOGS_VERSION.tar.gz | tar zx
\  
&& mv gogs-$GOGS_VERSION/* . \  
&& go get -v -tags "sqlite redis memcache cert pam" \  
&& go build -tags "sqlite redis memcache cert pam" \  
&& mkdir /app \  
&& mv gogs /app \  
&& mv public /app \  
&& mv scripts /app \  
&& mv templates /app \  
&& chown -R git:git /app \  
&& chmod 750 -R /app \  
&& apk del --purge build-dependencies \  
&& rm -rf /gopath /tmp/* /var/cache/apk/*  
  
COPY nsswitch.conf /etc/nsswitch.conf  
COPY sshd_config /etc/ssh/sshd_config  
COPY s6 /etc/services.d  
  
WORKDIR /data  
  
HEALTHCHECK \--interval=30s --retries=3 CMD curl --fail
http://localhost:3000/healthcheck || exit 1  
VOLUME /config /data  
EXPOSE 22 3000  
ENTRYPOINT ["/init"]  

