FROM debian:8  
ENV DEBIAN_FRONTEND noninteractive  
# http://installatron.com/developer/server#2.3  
RUN apt-get update && \  
apt-get -y install curl vim  
RUN curl -O https://data.installatron.com/installatron-server.sh  
RUN chmod +x installatron-server.sh  
RUN ./installatron-server.sh -f --key YOUR_LICENSE_KEY  
  
# When you install net-tools before the installation  
# you don't get https://localhost/installatron/  
# but localhost will be replaced with some IP  
# e.g. https://54.167.178.123/installatron/  
RUN apt-get install -y pciutils net-tools  
  
# the top commands are fixed, so docker uses its caching layers  
# we run it now again, with a valid key, so we use the cached installed
packages  
# and do not reinstall everything when a key is changed  
# So the following lines should be in your docker image,  
# which uses this image as a base image.  
# RUN ./installatron-server.sh -f --key NOW_WE_DO_RUN_IT_WITH_A_VALID_KEY  
# WORKDIR /usr/local/installatron/  
# COPY nginx.conf /etc/nginx/nginx.conf  
# CMD service mysql start && php5-fpm -R && nginx -g 'daemon off;'  
# EXPOSE 443  
# EXPOSE 8080  

