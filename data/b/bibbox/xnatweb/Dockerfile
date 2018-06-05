FROM tomcat:7.0.82-jre7-alpine  
  
ADD tomcat-users.xml /usr/local/tomcat/conf/  
ADD server.xml /usr/local/tomcat/conf/  
ADD setenv.sh /usr/local/tomcat/bin  
  
RUN adduser -D -g '' xnat  
  
RUN ["rm", "-fr", "/usr/local/tomcat/webapps/ROOT"]  
RUN wget --quiet
https://bintray.com/nrgxnat/applications/download_file?file_path=xnat-
web-1.7.4.war -O /usr/local/tomcat/webapps/ROOT.war  
  
#use this for local development  
#ADD xnat-web-1.7.4.war /usr/local/tomcat/webapps/ROOT.war  
ADD scripts /scripts  
WORKDIR /scripts  
RUN chmod a+x *.sh  
  
ENTRYPOINT ["/scripts/entrypoint.sh"]

