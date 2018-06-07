FROM durenworks/webphpmysql-dev:0.2.2  
# Docker maintainer  
MAINTAINER Airlangga Cahya Utama <airlangga@durenworks.com>  
  
# Set composer env  
ENV COMPOSER_HOME /root  
  
# Install composer and git  
RUN apt-get update -yq && \  
apt-get install -yq --no-install-recommends git && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
curl -sS https://getcomposer.org/installer | php -- --version=1.0.0-alpha9 &&
\  
mkdir -p /build/script && \  
mv composer.phar /build/script/  
  
# Copy config file  
COPY build /build  
RUN cp -R /build/etc/* /etc  
  
# Expose ports.  
EXPOSE 80  
EXPOSE 3306  

