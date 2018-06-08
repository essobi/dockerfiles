FROM ring0club/python:2.7.15-r0  
RUN apk add certbot=0.24.0-r0 \  
\--repository https://nl.alpinelinux.org/alpine/edge/community \  
\--no-cache  
#VOLUME /etc/letsencrypt /var/log/letsencrypt  
ENTRYPOINT ["/bin/sh"]  

