# Dockerfile for installing and running Nginx  
# Select ubuntu as the base image  
FROM ubuntu  
MAINTAINER M Bintang <halilintar8@yahoo.com>  
  
VOLUME ["/config"]  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
# Install Required Packages  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get -y install curl unzip git wget vim nginx python-setuptools  
  
# Setup Nginx  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/"
/etc/nginx/nginx.conf  
RUN sed -i -e"s/keepalive_timeout 2/keepalive_timeout
2;\n\tclient_max_body_size 100m/" /etc/nginx/nginx.conf  
RUN sed -i -e"s/# server_tokens off;/server_tokens off;/"
/etc/nginx/nginx.conf  
ADD /config/default.conf /etc/nginx/sites-available/default  
ADD /src /src  
RUN chown -R www-data:www-data /src  
  
# Run Supervisord  
RUN /usr/bin/easy_install supervisor  
RUN /usr/bin/easy_install supervisor-stdout  
RUN /usr/bin/easy_install superlance  
ADD /config/supervisord.conf /etc/supervisord.conf  
  
# Publish port  
EXPOSE 80 443  
CMD ["/usr/local/bin/supervisord","-n"]  
  

