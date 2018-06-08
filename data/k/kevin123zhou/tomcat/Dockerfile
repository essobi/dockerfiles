FROM tomcat:8.5.15-jre8-alpine  
  
RUN rm -rf webapps/  
ADD . webapps/  
  
CMD ["catalina.sh","run"]

