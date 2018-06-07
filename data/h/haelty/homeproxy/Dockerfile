FROM alpine:3.4  
RUN apk update && apk upgrade  
  
# Install needed packages  
RUN apk add openssh  
RUN apk add nginx  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories  
RUN apk update  
RUN apk add autossh  
  
# Volumes for sharing files with host  
VOLUME ["/config", "/var/www"]  
  
# Configuration of ssh tunnel  
RUN mkdir -p ~/.ssh  
RUN ln -s /config/key.public ~/.ssh/sshtunnel.pub  
RUN ln -s /config/key.private ~/.ssh/sshtunnel  
RUN ln -s /config/known_hosts ~/.ssh/known_hosts  
COPY autossh /etc/init.d/autossh  
  
# Configuration of nginx  
COPY nginx.conf /etc/nginx/nginx.conf  
  
# Expose port 80 for nginx  
EXPOSE 80  
# Expose port 25 for SMTP tunnel  
EXPOSE 25  
# Configure starting script  
COPY init.sh /init.sh  
ENTRYPOINT ["/init.sh"]  

