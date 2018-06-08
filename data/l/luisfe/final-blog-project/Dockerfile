FROM openshift/origin-base  
  
MAINTAINER https://github.com/vbehar/nginx-openshift-docker-image  
  
ENV CONFD_VERSION 0.10.0  
RUN echo "Installing Confd ${CONFD_VERSION} ..." \  
&& curl -jksSL
"https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64" > /usr/local/bin/confd \  
&& chmod a+x /usr/local/bin/confd  
  
RUN yum install epel-release -y  
  
RUN echo "Installing Nginx ..." \  
&& yum install -y nginx \  
&& yum clean all \  
&& mkdir -p /var/lib/nginx && chmod -R 777 /var/lib/nginx \  
&& mkdir -p /var/log/nginx && chmod -R 777 /var/log/nginx  
  
RUN chmod 777 /etc/nginx \  
&& chmod 666 /etc/nginx/nginx.conf \  
&& mkdir -p /etc/nginx/default.d && chmod -R 777 /etc/nginx/default.d \  
&& mkdir -p /etc/nginx/conf.d && chmod -R 777 /etc/nginx/conf.d  
  
COPY usr/local/bin/ /usr/local/bin/  
COPY /build/default /usr/share/nginx/html  
COPY service-worker.js /usr/share/nginx/html  
COPY manifest.json /usr/share/nginx/html  
  
RUN chmod a+x /usr/local/bin/*  
CMD ["start-nginx.sh"]  
  
COPY etc/confd/ /etc/confd/  
  
VOLUME ["/etc/nginx/default.d", "/etc/nginx/conf.d", "/var/log/nginx"]  
  
# Default values  
ENV NGINX_LISTEN_PORT=8081 \  
NGINX_LOG_ACCESS=/var/log/nginx/access.log \  
NGINX_LOG_ERROR=/var/log/nginx/error.log  
EXPOSE 8081  

