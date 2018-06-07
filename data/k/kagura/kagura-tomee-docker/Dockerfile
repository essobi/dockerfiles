FROM tomee:8-jre-1.7.3-jaxrs  
  
RUN rm -rf /usr/local/tomee/webapps/ROOT /usr/local/tomee/webapps/docs
/usr/local/tomee/webapps/host-manager /usr/local/tomee/webapps/manager  
  
RUN wget -O /usr/local/tomee/webapps/kagura.war
http://central.maven.org/maven2/com/kagurabi/war-rest/1.8/war-rest-1.8.war  
COPY reports /reports  

