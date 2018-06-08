FROM phusion/baseimage  
  
MAINTAINER Florian Kasper <florian@xpandmmi.com>  
  
COPY 01-build.sh /stage  
RUN /stage && rm /stage  
  
COPY 02-compile.sh /stage  
RUN /stage && rm /stage  
  
COPY 03-configure.sh /stage  
RUN /stage && rm /stage  
  
COPY nginx/nginx.conf /etc/nginx/nginx.conf  
COPY nginx/conf.d /etc/nginx/conf.d  
COPY nginx/includes /etc/nginx/includes  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr
/var/log/nginx/error.log  
  
ONBUILD COPY sites-enabled /etc/nginx/sites-enabled  
  
RUN mkdir /app  
VOLUME /app  
  
CMD ["/usr/bin/supervisord"]  

