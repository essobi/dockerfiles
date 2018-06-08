FROM justincarter/lucee:latest  
  
MAINTAINER Justin Carter justin.w.carter@gmail.com  
  
# install nginx and supervisor  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-
install-recommends \  
nginx \  
supervisor && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# configuration  
COPY lucee/server.xml /opt/lucee/tomcat/conf/server.xml  
COPY lucee/lucee-web.xml.cfm /var/www/WEB-INF/lucee/lucee-web.xml.cfm  
COPY nginx/sites-available/default /etc/nginx/sites-available/default  
COPY supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 80  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/conf.d/supervisord.conf"]

