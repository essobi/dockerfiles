# This file is a template, and might need editing before it works on your
project.  
FROM soxueren/tomcat:8.5-jre8-alpine  
  
RUN apk add --no-cache \  
vim \  
unzip \  
mkfontscale \  
mkfontdir \  
fontconfig  
  
EXPOSE 8080  
CMD ["/usr/local/tomcat/bin/catalina.sh","run"]  

