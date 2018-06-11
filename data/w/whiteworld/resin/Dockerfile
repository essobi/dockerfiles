FROM java:7-jre  
  
MAINTAINER White World "ljq258@gmail.com"  
  
# Install resin  
RUN cd /opt && wget http://caucho.com/download/resin-pro-4.0.44.zip && unzip
resin-pro-4.0.44.zip && rm resin-pro-4.0.44.zip && mv resin-pro-4.0.44 resin  
ENV PATH $PATH:/opt/resin/bin  
  
# Add config file and war  
# ADD resin.xml /opt/resin/conf/  
# ADD mihome.war /opt/resin/webapps/war/  
  
# port  
# EXPOSE 80  

