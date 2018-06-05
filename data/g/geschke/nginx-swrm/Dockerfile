#FROM phusion/baseimage  
FROM ubuntu:bionic  
  
LABEL maintainer="Ralf Geschke <ralf@kuerbis.org>"  
  
LABEL last_changed="2018-03-25"  
  
# necessary to set default timezone Etc/UTC  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Nginx  
RUN apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y dist-upgrade \  
&& apt-get install -y ca-certificates \  
&& apt-get install -y --no-install-recommends \  
&& apt-get install -y locales \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8 \  
&& apt-get install -y nginx \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV LANG en_US.utf8  
  
#COPY files/nginx.conf /etc/nginx/  
#VOLUME /etc/nginx/sites-enabled  
#VOLUME /etc/nginx/conf.d  
#VOLUME /var/www  
WORKDIR /var/www/html  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  
  

