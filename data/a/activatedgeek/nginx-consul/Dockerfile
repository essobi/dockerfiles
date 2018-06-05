FROM nginx:1.9  
MAINTAINER Sanyam Kapoor "1sanyamkapoor@gmail.com"  
RUN apt-get -y update &&\  
apt-get install -y wget unzip &&\  
wget https://releases.hashicorp.com/consul-template/0.13.0/consul-
template_0.13.0_linux_amd64.zip &&\  
unzip consul-template_0.13.0_linux_amd64.zip &&\  
apt-get remove --purge -y wget unzip &&\  
apt-get autoremove -y &&\  
apt-get clean &&\  
apt-get autoclean &&\  
rm -rf /var/lib/apt/lists/* &&\  
rm -rf /usr/share/man/*  
  
RUN mv consul-template /bin/consul-template &&\  
rm consul-template_0.13.0_linux_amd64.zip &&\  
rm -rf /etc/nginx/conf.d/* &&\  
mkdir -p /templates /etc/nginx/ssl /etc/nginx/sites-available
/etc/nginx/sites-enabled  
  
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf  
COPY ./scripts/docker-entrypoint.sh /docker-entrypoint.sh  
  
VOLUME ["/etc/nginx/ssl", "/templates"]  
  
EXPOSE 80 443  
# environment variables configurable, with defaults  
ENV CONSUL_HOST 127.0.0.1:8500  
ENV CONSUL_LOG_LEVEL info  
ENV CONSUL_TEMPLATE_CONFIG /templates/config.hcl  
  
CMD ["/bin/bash", "/docker-entrypoint.sh"]  

