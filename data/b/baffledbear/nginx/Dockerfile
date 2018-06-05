FROM baffledbear/supervisord:python2.7  
MAINTAINER Peter Rauhut <baffling.bear@gmail.com>  
# Credit for most of this goes to tiangolo. https://github.com/tiangolo  
# I'm basically reimplementing his work, for my own practice.  
# Standard set up Nginx  
ENV NGINX_VERSION 1.9.11-1~jessie  
  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \  
&& echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y ca-certificates nginx=${NGINX_VERSION} gettext-base \  
&& rm -rf /var/lib/apt/lists/* \  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log \  
# Make NGINX run on the foreground  
&& echo "daemon off;" >> /etc/nginx/nginx.conf \  
# Remove default configuration from Nginx  
&& rm /etc/nginx/conf.d/default.conf  
  
EXPOSE 80 443  
# Copy the modified Nginx conf  
COPY nginx.conf /etc/nginx/conf.d  
  
# Copy the new supervisord.conf  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  

