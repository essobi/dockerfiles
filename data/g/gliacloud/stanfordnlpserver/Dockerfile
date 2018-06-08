FROM gliacloud/base_images:tomcat  
  
  
RUN apt-get update && apt-get install make wget -y  
  
ADD tomcat-users.xml /opt/tomcat/conf/tomcat-users.xml  
ADD index.html /opt/tomcat/webapps/ROOT/index.html  
ADD . /opt/tomcat/webapps/nlp  
  
workdir /opt/tomcat/webapps/nlp  
run make build  
EXPOSE 8080  
cmd make runserver  

