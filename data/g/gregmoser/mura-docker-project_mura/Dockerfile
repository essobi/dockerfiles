# Slatwall Source Build  
FROM lucee/lucee4:latest  
MAINTAINER Greg Moser, greg@gregmoser.com  
  
RUN apt-get clean  
RUN apt-get update  
RUN apt-get install -y uuid-runtime  
  
# Copy Tomcat & Lucee configs  
COPY ./opt/lucee/server/lucee-server/context/lucee-server.xml
/opt/lucee/server/lucee-server/context/lucee-server.xml  
COPY ./opt/lucee/web/lucee-web.xml.cfm /opt/lucee/web/lucee-web.xml.cfm  
  
# Expose Ports  
EXPOSE 8888  
COPY ./usr/local/entrypoint.sh /usr/local/entrypoint.sh  
ENTRYPOINT ["/usr/local/entrypoint.sh"]  
RUN chmod -R 755 /usr/local/entrypoint.sh  
  
# Copy Source File Last  
COPY ./var/www/ /var/www/  
RUN chmod -R 755 /var/www/  
  
CMD ["catalina.sh", "run"]  

