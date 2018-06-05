#  
# Docker image for the I2P BitTorrent Client  
# Requred i2pd router (see "ksey/i2pd" docker image)  
#  
FROM alpine:latest  
MAINTAINER Bob <kcey@mail.ru>  
  
# XD_IP="0.0.0.0" - listen all interfaces  
ENV XD_IP="0.0.0.0"  
ENV XD_PORT="1488"  
# "127.0.0.1" - IP address of the i2pd router. MUST be changed to actual IP!!!  
# Port 7656 - SAM bridge of i2pd router, a higher level socket API for clients
(like XD torrent client)  
ENV I2P_ROUTER="127.0.0.1:7656"  
# Home directory inside container.  
ENV XD_HOME="/home/xd"  
# HOST_USER_ID / HOST_GROUP_ID - user id / group id of user/group that have
read/write permissions on host directory  
ENV HOST_USER_ID=1001  
ENV HOST_GROUP_ID=1001  
COPY start_xd.sh /start_xd.sh  
  
RUN chmod a+rx /start_xd.sh \  
&& apk --no-cache add go build-base git yarn shadow \  
&& git clone https://github.com/majestrate/XD /tmp/XD \  
&& cd /tmp/XD \  
&& make \  
&& mv /tmp/XD/XD /usr/local/bin/ \  
&& ln -s /usr/local/bin/XD /usr/local/bin/XD-CLI \  
&& chmod 755 /usr/local/bin/XD* \  
&& chown root:root /usr/local/bin/XD* \  
&& cd / \  
&& rm -rf /tmp/XD && apk --purge del go build-base git yarn \  
&& mkdir -p "$XD_HOME"  
EXPOSE "$XD_PORT"  
VOLUME "$XD_HOME"  
  
ENTRYPOINT ["/start_xd.sh"]  

