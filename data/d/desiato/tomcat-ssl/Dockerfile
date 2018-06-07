FROM tomcat:8.5  
COPY start.sh /usr/local/bin  
COPY connector-ssl.xml .  
RUN sed -i '/<Service name="Catalina">/ r connector-ssl.xml'
"$CATALINA_HOME/conf/server.xml" && rm connector-ssl.xml  
  
EXPOSE 8443  
VOLUME $CATALINA_HOME/conf  
  
CMD start.sh  

