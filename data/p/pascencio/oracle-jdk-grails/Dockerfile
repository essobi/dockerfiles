FROM airdock/oracle-jdk:1.8  
MAINTAINER paascencio@gmail.com  
  
COPY docker-entrypoint.sh /entrypoint.sh  
COPY install-grails.sh /install.sh  
  
RUN chmod +x /install.sh && \  
/install.sh && \  
rm -rf /install.sh  
  
VOLUME /root/.m2  
  
WORKDIR /app  
  
EXPOSE 8080  
ENTRYPOINT ["/entrypoint.sh"]  

