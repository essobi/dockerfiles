FROM tomcat:8.5-jre8  
  
MAINTAINER Go About <tech@goabout.com>  
  
RUN rm -rf /usr/local/tomcat/webapps/*  
  
# Add templating entry point  
ADD https://github.com/jcassee/parameterized-
entrypoint/releases/download/0.9.0/entrypoint_linux_amd64
/usr/local/bin/entrypoint  
RUN chmod +x /usr/local/bin/entrypoint  
  
ENTRYPOINT ["entrypoint", "--"]  
CMD ["catalina.sh", "run"]  

