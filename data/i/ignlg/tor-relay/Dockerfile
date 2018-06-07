## Run a tor relay in a container  
## Based on the excellent Jess's image  
  
FROM jess/tor-relay  
MAINTAINER Ignacio Lago <ignacio@ignaciolago.com>  
  
#  
# Example call:  
#  
# docker run -d -v /etc/localtime:/etc/localtime \  
# \--restart always \  
# -p 9001:9001 \  
# -e 'PORT=9001' \  
# -e 'NICKNAME=hacktheplanet' \  
# -e 'CONTACT_INFO=Anonymous' \  
# -e 'ACCOUNTING_START=month 1 00:01' \  
# -e 'ACCOUNTING_MAX=100 GBytes' \  
# -e 'BANDWIDTH_RATE=1 MBytes' \  
# -e 'BANDWIDTH_BURST=2 MBytes' \  
# -e 'ADVERTISED_BANDWIDTH=512 KBytes' \  
# \--name tor-relay \  
# ignlg/tor-relay -f /etc/tor/torrc.custom  
#  
  
# Keep keys  
VOLUME [ "/home/tor/.tor" ]  
  
# Install sed  
USER root  
RUN apk update && apk add \  
sed \  
&& rm -rf /var/cache/apk/*  
  
## Commands  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
# As Alpine's "ash" can't handle functions, another  
# script is needed.  
COPY update_or_add.sh /update_or_add.sh  
  
## Make sure files are owned by tor user  
RUN touch /etc/tor/torrc.custom && chown -R tor /etc/tor  
  
USER tor  
  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  

