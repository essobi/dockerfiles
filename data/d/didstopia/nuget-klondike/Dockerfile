FROM didstopia/base:alpine-3.5  
MAINTAINER Didstopia <support@didstopia.com>  
  
# Use a specific Klondike version  
ENV KLONDIKE_VERSION=v2.1.1  
ENV KLONDIKE_BUILD=2.1.1.22ea5477-build156  
  
# Use root user by default  
USER root  
  
# Add apk repositories  
RUN echo http://nl.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories  
  
# Install dependencies  
RUN apk add --no-cache \  
busybox-suid \  
unzip \  
bash \  
wget \  
nginx \  
apache2-utils \  
mono  
  
# Install Mono  
#RUN apk add --no-cache --virtual=.build-dependencies \  
# wget \  
# ca-certificates \  
# tar \  
# xz && \  
# wget "https://www.archlinux.org/packages/extra/x86_64/mono/download/" -O
"/tmp/mono.pkg.tar.xz" && \  
# tar -xJf "/tmp/mono.pkg.tar.xz" && \  
# cert-sync /etc/ssl/certs/ca-certificates.crt && \  
# apk del .build-dependencies && \  
# rm /tmp/*  
#RUN apt-get update && \  
# apt-get upgrade -y && \  
# apt-get autoremove -y && \  
# apt-get install -y \  
# nginx \  
# apache2-utils \  
# && rm -rf /var/cache/apt/*  
# Remove default nginx stuff  
RUN rm -fr /usr/share/nginx/html/* && \  
rm -fr /etc/nginx/sites-available/* && \  
rm -fr /etc/nginx/sites-enabled/* && \  
mkdir -p /run/nginx  
  
# Use a custom nginx configuration  
COPY nginx_klondike.conf /etc/nginx/nginx.conf  
  
# Setup default user  
RUN addgroup -g 500 klondike && \  
adduser -u 500 -G klondike -s /bin/sh -D klondike  
  
# Setup volumes  
VOLUME /data  
  
# Install Klondike  
RUN mkdir -p /app  
RUN wget --no-check-certificate
https://github.com/chriseldredge/Klondike/releases/download/${KLONDIKE_VERSION}/Klondike.${KLONDIKE_BUILD}.zip
-O /app/Klondike.${KLONDIKE_BUILD}.zip && \  
unzip /app/Klondike.${KLONDIKE_BUILD}.zip -d /app && \  
rm -f /app/*.zip  
  
# Overwrite the default settings  
COPY Settings.config /app/Settings.config  
  
# Fix permissions  
RUN chown -R klondike:klondike /app  
  
# Add the startup script  
COPY run.sh /run.sh  
RUN chmod a+x /run.sh  
  
# Expose ports  
EXPOSE 80  
# Set the entry point  
ENTRYPOINT ["./run.sh"]  

