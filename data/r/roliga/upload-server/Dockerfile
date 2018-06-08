FROM alpine:latest  
  
# Install packages  
RUN apk add --update \  
nginx openssh  
  
# Add sftp user  
RUN adduser -D sftp && passwd -u sftp  
  
# Install config files and run script  
COPY "nginx.conf" "/etc/nginx/nginx.conf"  
COPY "sshd_config" "/etc/ssh/sshd_config"  
COPY "run.sh" "/run.sh"  
  
# Volume for uploaded data  
VOLUME /srv/www  
# Volume for ssh host keys and authorized client keys  
VOLUME /ssh  
  
# Expose ssh and web server port  
EXPOSE 80  
EXPOSE 22  
CMD [ "/run.sh" ]  

