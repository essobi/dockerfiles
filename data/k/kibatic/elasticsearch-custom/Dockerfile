FROM tutum/curl:trusty  
MAINTAINER system@kibatic.com  
  
RUN curl http://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-key add
- && \  
echo 'deb http://packages.elasticsearch.org/elasticsearch/1.1/debian stable
main' >> /etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y elasticsearch openjdk-7-jre-headless && \  
apt-get install -y nginx supervisor apache2-utils && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV ELASTICSEARCH_USER **None**  
ENV ELASTICSEARCH_PASS **None**  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
ADD nginx_default /etc/nginx/sites-enabled/default  
ADD elasticsearch-customisations-0.0.1-SNAPSHOT.jar
/usr/share/elasticsearch/lib/elasticsearch-customisations-0.0.1-SNAPSHOT.jar  
ADD elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml  
  
EXPOSE 9200  
CMD ["/usr/bin/supervisord"]  

