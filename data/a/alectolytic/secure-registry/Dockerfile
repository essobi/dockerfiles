FROM fedora:latest  
  
RUN dnf -y upgrade  
RUN dnf -y install supervisor nginx httpd-tools  
RUN dnf -y install https://github.com/abn/docker-registry-
rpm/releases/download/v2.0.1-1/docker-registry-2.0.1-1.el7.centos.x86_64.rpm  
  
ENV CONFIG /config  
ENV REGISTRY_HOST localhost  
ENV REGISTRY_PORT 5000  
ENV REGISTRY_CONFIG /etc/docker-registry.yml  
ENV REGISTRY_CERT /etc/nginx/ssl/docker-registry.crt  
ENV REGISTRY_KEY /etc/nginx/ssl/docker-registry.key  
ENV NGINX_CONFIG /etc/nginx/conf.d/00-docker-registry.conf  
ENV OPENSSL_CONFIG /openssl.cnf  
ENV SERVER_NAME localhost  
ENV SERVER_IP 127.0.0.1  
RUN mkdir -p ${CONFIG}  
RUN mkdir -p /etc/nginx/ssl  
  
ADD ./assets/nginx.conf ${NGINX_CONFIG}  
ADD ./assets/supervisord.conf /etc/supervisord.conf  
ADD ./assets/entrypoint /usr/bin/entrypoint  
ADD ./assets/openssl.cnf ${OPENSSL_CONFIG}  
  
EXPOSE 443  
VOLUME ["${CONFIG}"]  
  
ENTRYPOINT ["/usr/bin/entrypoint"]  

