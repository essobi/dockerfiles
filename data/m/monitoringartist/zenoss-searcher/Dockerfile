FROM nginx  
MAINTAINER Jan Garaj info@monitoringartist.com  
  
COPY run.sh /  
  
RUN \  
apt-get update && \  
apt-get install -y wget unzip curl && \  
apt-get clean all && \  
rm -rf /tmp/* && \  
chmod +x /run.sh  
  
CMD ["/run.sh"]  

