FROM galeone/archlinux-updated-aur  
MAINTAINER Paolo Galeone <nessuno@nerdz.eu>  
  
USER aur  
RUN pacaur -S hardening-wrapper geoip --noconfirm  
  
USER root  
COPY builder /opt/  
RUN bash /opt/builder  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
VOLUME ["/var/cache/nginx"]  
  
EXPOSE 80 443  
  
ENTRYPOINT ["nginx", "-g", "daemon off;"]  

