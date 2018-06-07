FROM inspireso/java:8-jre-alpine  
  
MAINTAINER lan.xinen "<lan.xinen@inspireso.org>"  
COPY app /app  
COPY run.sh /run.sh  
  
RUN chmod +x /run.sh \  
&& dos2unix -u /run.sh  
  
ENTRYPOINT ["sh", "/run.sh"]

