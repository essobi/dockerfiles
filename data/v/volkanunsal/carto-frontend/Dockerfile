#  
# Frontend server container  
#  
FROM ubuntu:14.04  
MAINTAINER Volkan Unsal <spocksplanet@gmail.com>  
  
RUN apt-get update &&\  
apt-get install -y -q --no-install-recommends \  
unzip \  
curl \  
ca-certificates \  
&& rm -rf /var/lib/apt/lists/*  
  
LABEL caddy_version="0.9.3" architecture="amd64"  
  
ARG plugins=git  
  
# Install Caddy  
ENV CADDY /usr/local/bin/caddy  
RUN curl https://getcaddy.com | bash -s git,cors,upload,realip \  
&& chmod 0755 ${CADDY} \  
&& ${CADDY} -version  
  
# Add caddy to PATH  
ENV PATH $PATH:$CADDY  
  
# Configure Caddyfile  
COPY ./config/Caddyfile /etc/Caddyfile  
COPY index.html /caddy_server/index.html  
  
WORKDIR /caddy_server  
  
EXPOSE 80 443 2015  
ENTRYPOINT ["/usr/local/bin/caddy"]  
CMD ["--conf", "/etc/Caddyfile"]  

