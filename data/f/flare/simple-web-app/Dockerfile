FROM tomcat:jre7-alpine  
#USER tomcat  
ENV VERSION 1.0.1  
RUN apk update && \  
apk --no-cache add ca-certificates bash wget && \  
update-ca-certificates  
WORKDIR /usr/local/tomcat/webapps  
RUN wget https://github.com/flaresolar/simple-web-
app/releases/download/$VERSION/simple-web-app.war -nv  
CMD ["catalina.sh", "run"]

