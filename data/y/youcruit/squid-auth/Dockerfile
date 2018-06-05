FROM ubuntu:latest  
MAINTAINER tobias@youcruit.com  
  
RUN apt-get update && apt-get -y -u dist-upgrade && apt-get -y install squid3
apache2-utils && apt-get clean && rm -rf /var/lib/apt/lists/  
  
  
COPY squid.conf /etc/squid3/squid.conf  
COPY entrypoint.sh /  
  
EXPOSE 3128/tcp  
  
RUN mkdir -p /var/cache/squid3 && chown proxy -R /var/cache/squid3  
ENTRYPOINT /entrypoint.sh  

