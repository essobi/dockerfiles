from tomcat:8-jre8  
  
ENV TURBINE_VERSION 1.0.0  
RUN rm -rf /usr/local/tomcat/webapps/*  
RUN wget -O /usr/local/tomcat/webapps/ROOT.war
http://search.maven.org/remotecontent?filepath=com/netflix/turbine/turbine-
web/$TURBINE_VERSION/turbine-web-$TURBINE_VERSION.war; \  
mkdir ROOT; \  
unzip /usr/local/tomcat/webapps/ROOT.war -d /usr/local/tomcat/webapps/ROOT; \  
rm /usr/local/tomcat/webapps/ROOT.war; \  
rm /usr/local/tomcat/webapps/ROOT/WEB-INF/classes/config.properties  
  
COPY usr/local/turbine/bin/start_turbine.sh
/usr/local/turbine/bin/start_turbine.sh  
  
CMD ["/usr/local/turbine/bin/start_turbine.sh"]  
  

