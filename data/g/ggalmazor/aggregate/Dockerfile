FROM alpine:latest as unzipper  
ADD http://www-us.apache.org/dist/tomcat/tomcat-8/v8.0.50/bin/apache-
tomcat-8.0.50.zip /tmp/  
ADD https://s3.amazonaws.com/odk/aggregate-v1.4.15.zip /tmp/  
RUN unzip /tmp/apache-tomcat-8.0.50.zip -d /tmp  
RUN mv /tmp/apache-tomcat-8.0.50 /tmp/tomcat  
RUN rm -r /tmp/tomcat/webapps/*  
RUN unzip /tmp/aggregate-v1.4.15.zip -d /tmp/tomcat/webapps  
RUN chmod +x /tmp/tomcat/bin/*.sh  
  
FROM postgres:9.6-alpine  
  
EXPOSE 5432 8080  
ADD ./init.sh /docker-entrypoint-initdb.d/  
ADD ./start.sh /usr/local/bin/  
RUN mkdir /tomcat  
COPY \--from=unzipper /tmp/tomcat/ /tomcat/  
RUN apk add --no-cache openjdk8-jre unzip && chmod +x /usr/local/bin/start.sh  
  
CMD ["start.sh"]  

