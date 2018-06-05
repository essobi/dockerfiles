FROM alpine:3.4  
EXPOSE 80  
MAINTAINER GroovyCarrot <jake.wise@groovycarrot.co.uk>  
  
ENV WEB_ROOT=/var/www/public  
  
ADD layer /  
  
RUN chmod 755 /start.sh \  
&& echo http://nl.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories
\  
&& apk update && apk add --no-cache \  
bash \  
openssh-client \  
wget \  
nginx \  
supervisor \  
curl \  
&& mkdir -p /etc/nginx/ssl \  
&& mkdir -p /etc/nginx/sites-enabled \  
&& mkdir /run/nginx \  
&& mkdir -p /var/log/supervisor \  
&& ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-
enabled/default.conf  
  
CMD ["/start.sh"]  

