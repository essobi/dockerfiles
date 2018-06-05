# Bamboo Server  
#  
# VERSION 0.0.1  
FROM openjdk:alpine  
  
# Environment  
ENV BAMBOO_VERSION 5.7.2  
ENV BAMBOO_HOME /home/bamboo  
  
# Expose web and agent ports  
EXPOSE 8085  
EXPOSE 54663  
# Make sure we get latet packages  
RUN \  
apk add --update \  
git \  
subversion \  
bash \  
wget \  
&& rm -rf /var/cache/apk/*  
  
CMD /opt/bamboo-server.sh  
  
# Add Bamboo install script  
ADD bamboo-server.sh /opt/  
  

