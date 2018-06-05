FROM tomcat:6  
RUN apt-get -yq update && apt-get -yq install \  
cutycapt \  
netcat \  
patch \  
postgresql-client \  
libpg-java \  
xvfb  
  
# Remove default root app  
RUN rm -rf /usr/local/tomcat/webapps/ROOT  
  
# Install WAR and context  
RUN wget -q -O /usr/local/tomcat/webapps/ROOT.war
http://downloads.sourceforge.net/project/libreplan/LibrePlan/libreplan_1.4.0.war  
ADD libreplan.xml /usr/local/tomcat/conf/Catalina/localhost/ROOT.xml  
  
# Patch policies  
ADD catalina.policy.patch catalina.policy.patch  
RUN patch -o /usr/local/tomcat/conf/catalina.policy
/usr/local/tomcat/conf/catalina.policy catalina.policy.patch  
  
# Link jdbc driver  
RUN ln -s /usr/share/java/postgresql-jdbc3.jar /usr/local/tomcat/lib/  
  
# Add startup script which detects and configures database  
ADD start-libreplan.sh /usr/bin/start-libreplan.sh  
  
CMD ["/usr/bin/start-libreplan.sh"]  

