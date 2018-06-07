FROM bitnami/minideb:jessie  
  
# ENV CADDY_VERSION 0.10.3 linux64 full  
ENV CADDY_FEATURES ""  
#^ "cors,git,hugo,ipfilter,jsonp,search"  
# RUN install_packages tar git  
RUN mkdir /opt/caddy/ && mkdir /opt/caddy/tmp && mkdir /var/www/  
COPY ./files/caddy_v0.10.3_linux_amd64_custom_full.tar.gz /opt/caddy/tmp/  
COPY ./caddy_start.sh /opt/caddy/  
RUN chmod u+x /opt/caddy/caddy_start.sh  
RUN tar -xzf /opt/caddy/tmp/caddy_v0.10.3_linux_amd64_custom_full.tar.gz -C
/opt/caddy/ && chmod u+x /opt/caddy/caddy  
COPY ./Caddyfile /opt/caddy/  
  
EXPOSE 80 443  
CMD ./opt/caddy/caddy_start.sh  

