FROM golang:stretch  
  
ENV TAG debian  
ENV ARCH amd64  
ENV PATH /opt/pihole:${PATH}  
  
ADD ./install.sh /usr/local/bin/docker-install.sh  
ENV setupVars /etc/pihole/setupVars.conf  
ENV PIHOLE_INSTALL /tmp/ph_install.sh  
ENV S6OVERLAY_RELEASE https://github.com/just-
containers/s6-overlay/releases/download/v1.21.2.2/s6-overlay-amd64.tar.gz  
  
RUN apt-get update && \  
apt-get install -y wget curl net-tools cron procps && \  
curl -L -s $S6OVERLAY_RELEASE \  
| tar xvzf - -C / && \  
docker-install.sh && \  
rm -rf /var/cache/apt/archives /var/lib/apt/lists/* && \  
mv /init /s6-init  
  
ADD ./s6/debian-root /  
ADD ./s6/service /usr/local/bin/service  
ADD ./dnscrypt-proxy/dnscrypt-proxy.toml /dnscrypt-proxy.toml  
ADD ./start-pihole.sh /start-pihole.sh  
  
RUN git clone https://github.com/jedisct1/dnscrypt-proxy src && \  
cd src/dnscrypt-proxy && \  
go get -d && \  
go clean && \  
go build -ldflags="-s -w" -o $GOPATH/linux-amd64/dnscrypt-proxy && \  
cd .. && \  
cp systemd/* $GOPATH/linux-amd64/ && \  
cd .. && \  
rm -rf ./src && \  
mkdir -p /etc/dnscrypt-proxy  
  
# php config start passes special ENVs into  
ENV PHP_ENV_CONFIG '/etc/lighttpd/conf-enabled/15-fastcgi-php.conf'  
ENV PHP_ERROR_LOG '/var/log/lighttpd/error.log'  
ADD ./start.sh /  
ADD ./bash_functions.sh /  
  
# IPv6 disable flag for networks/devices that do not support it  
ENV IPv6 true  
  
ENV S6_LOGGING 0  
ENV S6_KEEP_ENV 1  
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS 2  
ENV FTL_CMD no-daemon  
  
HEALTHCHECK CMD dig @127.0.0.1 pi.hole || exit 1  
  
CMD [ "/start-pihole.sh" ]  
  
SHELL ["/bin/bash", "-c"]  

