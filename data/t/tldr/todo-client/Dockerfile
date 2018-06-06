FROM nginx:1.9.5  
MAINTAINER accenture  
  
#
https://github.com/kelseyhightower/confd/releases/download/v0.10.0/confd-0.10.0-linux-
amd64  
ENV confd_version 0.10.0  
# Copy our application files  
COPY bower_components /usr/share/nginx/html/bower_components  
RUN mkdir -p /usr/share/nginx/html  
COPY index.html /usr/share/nginx/html/index.html  
COPY css /usr/share/nginx/html/css  
COPY js /usr/share/nginx/html/js  
  
# Add confd  
ADD
https://github.com/kelseyhightower/confd/releases/download/v${confd_version}/confd-${confd_version}-linux-
amd64 /confd  
  
# Custom Nginx configuration files  
ADD docker/etc/nginx/nginx.conf /etc/nginx/nginx.conf  
ADD docker/etc/confd /etc/confd  
  
# include the Dockerfile that was used to build this container, for reference
purposes  
ADD Dockerfile /Dockerfile  
  
ADD docker/run.sh /run.sh  
RUN chmod ugo+x /run.sh /confd  
  
CMD ["/run.sh"]  
  
EXPOSE 80

