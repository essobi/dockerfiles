#  
# Reverse proxy for kubernetes  
#  
FROM ubuntu:latest  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Prepare requirements  
RUN apt-get update -qy && \  
  
# install software-properties-common  
apt-get install --no-install-recommends -qy \  
software-properties-common && \  
  
# install nginx  
add-apt-repository -y ppa:nginx/stable && \  
apt-get install --no-install-recommends -qy nginx && \  
  
# prepare nginx  
chown -R www-data:www-data /var/lib/nginx && \  
rm -f /etc/nginx/sites-available/default && \  
  
# apt clean  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# setup confd  
ADD
https://github.com/kelseyhightower/confd/releases/download/v0.6.3/confd-0.6.3-linux-
amd64 /usr/local/bin/confd  
RUN chmod u+x /usr/local/bin/confd && \  
mkdir -p /etc/confd/conf.d && \  
mkdir -p /etc/confd/templates  
  
ADD ./src/confd/conf.d/myconfig.toml /etc/confd/conf.d/myconfig.toml  
ADD ./src/confd/templates/nginx.tmpl /etc/confd/templates/nginx.tmpl  
ADD ./src/confd/confd.toml /etc/confd/confd.toml  
ADD ./gencert.sh /etc/nginx/ssl/  
  
ADD ./src/boot.sh /opt/boot.sh  
RUN chmod +x /opt/boot.sh  
  
# Run the boot script  
CMD /opt/boot.sh  

