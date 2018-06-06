FROM tomcat:9-jre8-alpine  
RUN rm -rf /usr/local/tomcat/webapps/* && \  
apk add --no-cache tzdata ttf-dejavu && \  
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \  
echo "Asia/Shanghai" > /etc/timezone && \  
apk del tzdata  

