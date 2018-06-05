#  
# GlassFish Server Open Source Edition 4.1 Dockerfile, by BrazilianBytes  
#  
# https://github.com/brazilianbytes/glassfish  
# https://github.com/brazilianbytes/glassfish/tree/master/glassfish/4/4.1  
#  
# Pull base image.  
FROM brazilianbytes/java  
MAINTAINER Luciano Jesus Lima <developer@brazilianbytes.com>  
  
# Install Tools.  
RUN apt-get update  
RUN apt-get install -y wget unzip pwgen expect  
  
# Download GlassFish.  
RUN wget
http://dlc.sun.com.edgesuite.net/glassfish/4.1/release/glassfish-4.1.zip  
  
# Install GlassFish.  
RUN mkdir -p /env  
RUN unzip glassfish-4.1.zip -d /env  
RUN mv /env/glassfish4 /env/srv  
  
# Remove zip  
RUN rm glassfish-4.1.zip  
  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
# http://docs.oracle.com/cd/E26576_01/doc.312/e24928/overview.htm  
# 4848 - Administration Server Port  
# 8080 - HTTP Port  
# 8181 - HTTPS Port  
# 8686 - Pure JMX Clients Port  
# 7676 - Message Queue Port  
# 3700 - IIOP Port  
# 3820 - IIOP/SSL Port  
# 3920 - IIOP/SSL Port With Mutual Authentication  
# 9009 - JPDA debug port  
EXPOSE 4848 8080 8181 8686 7676 3700 3820 3920 9009  
# Start server  
CMD ["/start.sh"]  

