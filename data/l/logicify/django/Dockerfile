FROM logicify/python-wsgi:3.6  
MAINTAINER "Dmitry Berezovsky <dmitry.berezovsky@logicify.com>"  
ENV PROXY_TIMEOUT "90"  
ENV STATIC_URL "/static"  
ENV STATIC_PATH "/srv/static"  
ENV MEDIA_PATH "/srv/media"  
USER root  
RUN yum -y update \  
&& yum -y install nginx gettext python2-pip \  
&& pip2 install supervisor supervisor-stdout \  
&& mkdir /etc/nginx/proxy.d  
  
# Create a directory for config  
COPY nginx/nginx.conf /etc/nginx/nginx.conf  
COPY nginx/start-nginx.sh /usr/bin/start-nginx.sh  
COPY nginx/mime.types /etc/nginx/mime.types  
COPY supervisor.ini /etc/supervisor.ini  
COPY supervisor-shutdown.sh /usr/bin/supervisor-shutdown  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log \  
&& chmod +x /usr/bin/start-nginx.sh \  
&& chmod +x /usr/bin/supervisor-shutdown  
  
RUN localedef -v -c -i en_US -f UTF-8 en_US.UTF-8 || true  
ENV LC_ALL "en_US.UTF-8"  
EXPOSE 8080  
CMD ["supervisord", "-n", "-c", "/etc/supervisor.ini"]  

