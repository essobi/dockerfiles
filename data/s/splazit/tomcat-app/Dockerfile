FROM tomcat:8.5-jre8-alpine  
RUN apk --no-cache --update add ca-certificates openssl fontconfig ttf-dejavu
wget  
ENV WAR_URL=""  
COPY run.sh /usr/local/tomcat/bin/run-app.sh  
CMD ["run-app.sh"]  

