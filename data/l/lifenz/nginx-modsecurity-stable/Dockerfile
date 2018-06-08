FROM ubuntu:16.04  
MAINTAINER simon@linosec.lu  
  
ENV NGINX_VERSION=1.12.2  
ENV MODSECURITY_VERSION=2.9.2  
ENV OWASP_CRS_VERSION=3.0.2  
ADD build.sh /build.sh  
RUN chmod +x /build.sh && \  
/bin/bash -c "source /build.sh" && \  
rm /build.sh  
  
ADD nginx.conf /usr/local/nginx/conf/nginx.conf  
ADD modsec_includes.conf /usr/local/nginx/conf/modsec_includes.conf  
ADD modsecurity.conf /usr/local/nginx/conf/modsecurity.conf  
ADD crs-setup.conf /usr/local/nginx/conf/rules/crs-setup.conf  
ADD nginx-supervisor.ini /etc/supervisor/conf.d/supervisord.conf  
  
ENTRYPOINT ["/usr/bin/supervisord", "-c",
"/etc/supervisor/conf.d/supervisord.conf"]  
  
EXPOSE 80  

