FROM ubuntu:zesty  
MAINTAINER mail@thackbarth.net  
  
ARG CONTAINER_UID=1200  
ARG CONTAINER_GID=1200  
ENV DEBIAN_FRONTEND noninteractive  
  
COPY dyndns-generate-password.py /  
COPY dyndns-update.py /  
COPY entrypoint.sh /  
COPY example_settings.json /  
COPY named.conf.options /  
  
RUN export CONTAINER_USER=dyndns && \  
export CONTAINER_GROUP=dyndns && \  
addgroup -gid $CONTAINER_GID $CONTAINER_GROUP && \  
adduser --system --home /home/$CONTAINER_USER \--shell /bin/bash --uid
$CONTAINER_UID \--ingroup $CONTAINER_GROUP $CONTAINER_USER && \  
apt-get update && \  
apt-get install -y bind9 dnsutils haveged && \  
apt-get clean && \  
rm -rf /var/lib/apt/* /tmp/* /var/tmp/* /var/cache/apt/* && \  
mkdir -p /data && \  
mv /etc/bind/named.conf.options /etc/bind/named.conf.options_original && \  
mv /named.conf.options /etc/bind/named.conf.options && \  
echo 'include "/data/dyndns.zones";' >> /etc/bind/named.conf  
  
EXPOSE 53/tcp 53/udp  
EXPOSE 8080/tcp  
VOLUME ["/data"]  
  
CMD ["/entrypoint.sh", "bind9"]  

