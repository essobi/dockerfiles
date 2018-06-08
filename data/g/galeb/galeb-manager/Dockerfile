FROM tuxmonteiro/ubuntu-orajdk8  
  
MAINTAINER Marcelo Teixeira Monteiro  
  
ENV PORT 8010  
ENV NGINX_PORT 8000  
ENV VERSION 1.0.6-SNAPSHOT  
ENV GALEB_DB_SHOWSQL=false  
ENV GALEB_DB_DRIVER=com.mysql.jdbc.Driver  
ENV GALEB_DB_DIALECT=org.hibernate.dialect.MySQL5Dialect  
ENV GALEB_DB_DDL_AUTO=validate  
  
ADD start.sh /usr/bin/  
ADD log4j.xml /tmp/  
ADD nginx.conf /tmp/  
ADD load-farm.sh /tmp/  
  
RUN apt-get update && \  
apt-get -y install git nginx jq curl && \  
chmod +x /usr/bin/start.sh  
  
EXPOSE 8000  
  
CMD ["/usr/bin/start.sh"]  
  

