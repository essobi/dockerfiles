# Slatwall Quickstart for running locally for evaluation only  
FROM lucee/lucee4:latest  
MAINTAINER Sumit Verma, sumit.verma@ten24web.com  
  
ENV LUCEE_PASSWORD MakeThisLuceePWSecret!  
ENV MYSQL_HOST localhost  
ENV MYSQL_ROOT_PASSWORD=""  
ENV MYSQL_DATABASE Slatwall  
  
# Install Supervisor  
RUN apt-get update && apt-get install -y supervisor  
# Install mysql  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install mysql-server  
  
# Copy over the Lucee Configs  
COPY lucee-server.xml /opt/lucee/server/lucee-server/context/lucee-server.xml  
COPY lucee-web.xml.cfm /opt/lucee/web/lucee-web.xml.cfm  
# Move the configFramework.cfm file to the root so that it can be moved into
Slatwall after install  
COPY configFramework.cfm /root/configFramework.cfm  
# Because we are running mysql and lucee we copy over a subervisord config  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Copy over the entrypoint  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
# Expose Lucee Port  
EXPOSE 3306 8888  
CMD ["/usr/bin/supervisord"]  

