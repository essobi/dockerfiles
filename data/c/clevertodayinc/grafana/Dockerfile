FROM ubuntu:14.04  
MAINTAINER Brice Argenson <brice@clevertoday.com>  
  
# Install httpd  
RUN apt-get update -y && \  
apt-get install -y apache2 curl apache2-mpm-worker libapache2-mod-wsgi && \  
rm -f /etc/apache2/sites-enabled/000-default.conf && \  
echo "\nDocumentRoot /usr/share/grafana\n" >> /etc/apache2/apache2.conf  
  
# Install Grafana  
RUN curl -O -L http://grafanarel.s3.amazonaws.com/grafana-1.9.0-rc1.tar.gz &&
\  
tar xf grafana-1.9.0-rc1.tar.gz && \  
mv grafana-1.9.0-rc1 /usr/share/grafana  
  
COPY docker-entrypoint.sh /  
COPY config.js /usr/share/grafana/config.js  
  
EXPOSE 80  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["grafana"]  

