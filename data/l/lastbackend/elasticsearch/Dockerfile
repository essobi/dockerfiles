FROM ubuntu:trusty  
  
MAINTAINER team@lastbackend.com  
  
# Setup curl dependency  
RUN apt-get update && apt-get install -y curl && apt-get clean && rm -rf
/var/lib/apt/lists  
  
# Setup elsticsearch  
RUN curl http://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-key add
- && \  
echo 'deb http://packages.elasticsearch.org/elasticsearch/1.3/debian stable
main' >> /etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y elasticsearch openjdk-7-jre-headless && \  
apt-get install -y nginx supervisor apache2-utils && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD init.sh /init.sh  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
ADD nginx_default /etc/nginx/sites-enabled/default  
RUN chmod +x /*.sh  
  
ENV ELASTICSEARCH_USER **NULL**  
ENV ELASTICSEARCH_PASS **NULL**  
  
EXPOSE 9200  
CMD ["/init.sh"]

