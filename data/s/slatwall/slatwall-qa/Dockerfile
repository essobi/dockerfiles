# Slatwall Quickstart  
FROM lucee/lucee4:latest  
MAINTAINER Greg Moser, greg.moser@ten24web.com  
  
# Install Supervisor  
RUN apt-get update && apt-get install -y supervisor uuid-runtime  
  
# Because we are running mysql and lucee we copy over a subervisord config  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Set the Slatwall download URL & defaults so that the container just runs  
ENV SLATWALL_VERSION_OR_BRANCH master  
ENV MYSQL_HOST localhost  
ENV MYSQL_DATABASE Slatwall  
ENV MYSQL_ROOT_PASSWORD QaPa33W0RD  
ENV LUCEE_PASSWORD QaPa33W0RD  
  
# Expose Mysql & Lucee Ports  
EXPOSE 3306 8888  
# Copy over the Lucee Configs  
COPY lucee-server.xml /opt/lucee/server/lucee-server/context/lucee-server.xml  
COPY lucee-web.xml.cfm /opt/lucee/web/lucee-web.xml.cfm  
  
# Move the configFramework.cfm file to the root so that it can be moved into
Slatwall after install  
COPY configFramework.cfm /root/configFramework.cfm  
  
# Copy over the entrypoint to install the mysql server  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["/usr/bin/supervisord"]  
#CMD ["catalina.sh", "run"]  

