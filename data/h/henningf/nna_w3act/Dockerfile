FROM centos:7  
RUN yum install postgresql -y && \  
yum install java-1.8.0-openjdk -y && \  
yum install epel-release -y  
  
COPY w3act /opt/w3act  
COPY GeoLite2city/GeoLite2-City.mmdb /opt/w3act/lib/GeoLite2-City.mmdb  
  
ENV POSTGRES_USER training  
ENV POSTGRES_PASSWORD training  
ENV POSTGRES_HOST postgres  
ENV POSTGRES_DB w3act  
ENV W3ACT_SECRET secret  
ENV PRIVACY_STATEMENT http://www.webarchive.org.uk/ukwa/info/privacy  
ENV W3ACT_SERVER_NAME https://www.webarchive.org.uk  
ENV AMQP_QUEUE_HOST https://www.webarchive.org.uk  
ENV AMQP_QUEUE_PORT 5672  
ENV AMQP_QUEUE_NAME w3actqueue  
ENV AMQP_ROUTING_KEY w3actroutingkey  
ENV AMQP_EXCHANGE_NAME w3actexchange  
ENV APPLICATION_WAYBACK_URL http://opera.bl.uk:8080/wayback/  
ENV APPLICATION_WAYBACK_QUERY_PATH /xmlquery.jsp?url=  
ENV APPLICATION_ACCESS_RESOLVER_URL
http://www.webarchive.org.uk/access/resolve/  
ENV APPLICATION_MONITRIX_URL http://elk.ddb.wa.bl.uk:5601/app/kibana  
ENV APPLICATION_PDFTOHTMLEX_URL http://192.168.99.100:5000/convert?url=  
ENV ADMIN_DEFAULT_EMAIL wa-sysadm@bl.uk  
ENV W3ACT_USE_ACCOUNTS true  
ENV APPLICATION_LOGLEVEL WARN  
ENV DATABASE_LOGSTATEMENTS false  
  
  
EXPOSE 9000  
RUN chown -R 0 /opt/w3act && \  
chmod -R 775 /opt/w3act  
  
WORKDIR /opt/w3act  
  
CMD ./bin/w3act -Dapplication.data.import=true
-Ddb.default.url="postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}/${POSTGRES_DB}"
-Dapplication.name=w3act -Dapplication.secret="${W3ACT_SECRET}"
-Dconfig.file=/opt/w3act/conf/prod.conf  

