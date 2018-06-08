FROM openjdk:8-jre-alpine  
ADD https://bitbucket.org/Mirek_k/myip/downloads/myip.jar /opt/  
RUN chmod 444 /opt/myip.jar  
EXPOSE 8080  
USER 1001  
CMD ["java","-Xmx32M","-jar","/opt/myip.jar"]  

