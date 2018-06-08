FROM alpine:3.6  
MAINTAINER Dominik Bruhn "dominik@dbruhn.de"  
# Install packages  
RUN apk add --no-cache nginx supervisor openssh-server openssh-sftp-server  
  
# NGINX  
RUN mkdir -p /run/nginx/ && \  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
ADD nginx.conf /etc/nginx/conf.d/default.conf  
  
# SSH/SFTP  
ADD sshd_config /etc/ssh/  
  
# Supervisord  
ADD supervisord.ini /etc/supervisor.d/  
ADD docker_kill.py entrypoint.sh /  
  
# Configuration for Container  
VOLUME /data /etc/ssh/keys/  
EXPOSE 22 80  
# Creates users, checks permissions, generates host-keys and launches
supervisord  
CMD ["/entrypoint.sh"]  

