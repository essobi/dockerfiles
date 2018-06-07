FROM leanix/docker-nginx:1.14.0-alpine-extras  
MAINTAINER Andre Christ <andre.christ@leanix.net>  
  
# Install wget and install/updates certificates  
ENV SUPERVISOR_VERSION=3.3.1  
RUN apk update && apk add py-pip bash perl  
RUN pip install supervisor==$SUPERVISOR_VERSION  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
RUN mkdir -p /var/log/supervisor  
COPY supervisord.conf /etc/supervisor/supervisord.conf  
  
COPY confd-0.10.0-linux-amd64 /usr/local/bin/confd  
RUN chmod +x /usr/local/bin/confd \  
&& mkdir -p /etc/confd/{conf.d,templates}  
COPY nginx.toml /etc/confd/conf.d/nginx.toml  
COPY nginx.conf.tmpl /etc/confd/templates/nginx.conf.tmpl  
  
COPY html /usr/share/nginx/html/  
  
COPY nginx-location-split /usr/local/bin  
COPY confd-check /usr/local/bin  
  
EXPOSE 80  
CMD ["/usr/bin/supervisord"]  

