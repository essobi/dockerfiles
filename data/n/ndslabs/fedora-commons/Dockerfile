FROM jetty:9-jre8  
  
ARG version=4.5.1  
# Copy in the default Jetty configuration for Fedora Commons  
ADD jetty.conf /etc/default/jetty  
  
# Download the WAR file for Fedora Commons  
ADD
https://github.com/fcrepo4/fcrepo4/releases/download/fcrepo-${version}/fcrepo-
webapp-${version}.war /var/lib/jetty/webapps/ROOT.war  
  
RUN chmod 777 /var/lib/jetty/webapps/ROOT.war  

