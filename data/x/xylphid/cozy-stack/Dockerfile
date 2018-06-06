FROM golang:1.10.1-stretch as builder  
  
# Install dependencies  
RUN apt install git && \  
go get -u github.com/cozy/cozy-stack  
  
FROM debian:9.4-slim  
  
ARG VERSION  
ENV VERSION ${VERSION:-build}  
  
LABEL maintainer.name="Anthony PERIQUET"  
LABEL maintainer.email="anthony@periquet.net"  
LABEL version=${VERSION}  
LABEL description="Cozy-Cloud Core"  
  
ENV COZY_ADMIN_PASSWORD "password"  
ENV COZY_APPS "collect,drive,onboarding,photos,settings"  
ENV COZY_DOMAIN "mycozy.tld"  
ENV COZY_PORT "8080"  
ENV COZY_ADMIN_HOST "0.0.0.0"  
ENV COZY_ADMIN_PORT "6060"  
ENV COZY_ADMIN_PASSPHRASE "XXX"  
ENV COZY_COUCHDB_URL "http://couchdb:5984"  
ENV COZY_MAIL_REPLY "noreply@localhost"  
ENV COZY_MAIL_REPLY_NAME "noreply@localhost"  
ENV COZY_SMTP_HOST ""  
ENV COZY_SMTP_PORT "465"  
ENV COZY_SMTP_USERNAME ""  
ENV COZY_SMTP_PASSWORD ""  
ENV COZY_SMTP_TLS_ENABLE "false"  
COPY \--from=builder /go/bin/cozy-stack /tmp/cozy-stack  
  
RUN apt update && \  
apt upgrade -y && \  
apt install -y \  
curl \  
git \  
imagemagick && \  
rm -rf /var/lib/apt/lists/* && \  
install -m0755 -o root -g root /tmp/cozy-stack /usr/bin/cozy-stack && \  
# Clean temporary folder  
rm -f /tmp/cozy-stack && \  
adduser --system \  
\--shell /bin/bash \  
\--group \  
\--gecos "Cozy" \  
\--disabled-password \  
cozy && \  
install -d -o cozy -g cozy /etc/cozy /var/datas/  
  
# Copy configuration template  
COPY config/cozy.yml /etc/cozy/  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh && \  
ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat  
  
VOLUME /var/datas  
  
ENTRYPOINT [ "docker-entrypoint.sh" ]

