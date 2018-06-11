FROM tomcat:8-jre7-alpine  
  
EXPOSE 8080  
RUN cd /usr/local/tomcat/webapps &&\  
wget http://dl.twproject.com/default/Twproject_6_unix.tar.gz &&\  
tar -zxvf Twproject_6_unix.tar.gz &&\  
rm Twproject_6_unix.tar.gz &&\  
rm -R ROOT &&\  
mv Teamwork ROOT  
  
# ADD tomcat-users.xml /usr/local/tomcat/conf/  
# ADD global.properties /usr/local/tomcat/webapps/ROOT/commons/settings/  
# ADD config.properties /usr/local/tomcat/webapps/ROOT/WEB-INF/  
# ADD lic.properties /usr/local/tomcat/webapps/ROOT/WEB-INF/  
  
CMD /usr/local/tomcat/bin/catalina.sh run

