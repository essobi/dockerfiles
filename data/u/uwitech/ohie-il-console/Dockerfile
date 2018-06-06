#  
# Ubuntu 14.04  
#  
# https://hub.docker.com/_/ubuntu/  
#  
# Pull base image.  
FROM uwitech/ohie-base  
  
USER root  
  
#install tools  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN apt-get -y install nodejs  
RUN apt-get -y install git build-essential  
RUN apt-get -y install software-properties-common python-software-properties  
  
#install nginx  
RUN \  
add-apt-repository -y ppa:nginx/stable && \  
apt-get update && \  
apt-get install -y nginx && \  
rm -rf /var/lib/apt/lists/* && \  
chown -R www-data:www-data /var/lib/nginx  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY default /etc/nginx/sites-available/default  
  
# Define mountable directories.  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d",
"/var/log/nginx", "/var/www/html"]  
  
#openhim console  
#RUN cd ~  
#RUN wget https://github.com/jembi/openhim-
console/releases/download/v1.9.0/openhim-console-v1.9.0.tar.gz  
#RUN cp openhim-console-v1.9.0.tar.gz var/www/html  
#RUN cd var/www/html  
COPY html /var/www/html/  
#RUN tar -zxvf /var/www/html/openhim-console-v1.9.0.tar.gz -C /var/www/html/  
COPY cmd.sh /cmd.sh  
CMD ./cmd.sh  
  
EXPOSE 80  
EXPOSE 443  

