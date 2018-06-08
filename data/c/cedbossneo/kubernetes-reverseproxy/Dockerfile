#  
# Reverse proxy for kubernetes  
#  
FROM ubuntu:latest  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Prepare requirements  
RUN apt-get update -qy && \  
apt-get install --no-install-recommends -qy software-properties-common  
  
# setup confd  
ADD
https://github.com/kelseyhightower/confd/releases/download/v0.9.0/confd-0.9.0-linux-
amd64 /usr/local/bin/confd  
RUN chmod u+x /usr/local/bin/confd && \  
mkdir -p /etc/confd/conf.d && \  
mkdir -p /etc/confd/templates  
  
ADD ./src/confd /etc/confd  
ADD ./src/nginx /etc/nginx  
  
# Install Nginx.  
RUN add-apt-repository -y ppa:nginx/stable && \  
apt-get update -q && \  
apt-get install --no-install-recommends -qy nginx && \  
chown -R www-data:www-data /var/lib/nginx && \  
rm -f /etc/nginx/sites-available/default  
  
ADD ./src/boot.sh /opt/boot.sh  
RUN chmod +x /opt/boot.sh  
  
EXPOSE 80 443  
# Run the boot script  
CMD /opt/boot.sh  

