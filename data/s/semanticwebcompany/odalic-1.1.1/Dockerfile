FROM tomcat:9-alpine  
MAINTAINER Jan Váňa  
  
RUN apk update  
RUN apk add ca-certificates  
RUN update-ca-certificates  
RUN apk add openssl  
  
RUN mkdir ../resources  
  
RUN wget -O ../resources/odalic.war
https://github.com/odalic/sti/releases/download/v1.1.1/odalic.war  
RUN mv -v ../resources/odalic.war webapps/odalic.war  
  
RUN wget -O ../resources/ocalic-ui.tar.gz https://github.com/odalic/odalic-
ui/archive/v1.1.0.tar.gz  
RUN tar -zxvf ../resources/ocalic-ui.tar.gz -C ../resources  
RUN mv ../resources/odalic-ui-1.1.0 webapps/odalic-ui  
  
RUN wget -O ../resources/resources.tar.gz https://github.com/odalic/odalic-
docker-repository/archive/v1.1.1.tar.gz  
RUN tar -zxvf ../resources/resources.tar.gz -C ../resources  
  
RUN mv ../resources/odalic-docker-repository-1.1.1/tomcat/bin/setenv.sh
bin/setenv.sh  
RUN chmod 750 bin/setenv.sh  
  
RUN rm conf/context.xml  
RUN mv ../resources/odalic-docker-repository-1.1.1/tomcat/conf/context.xml
conf/context.xml  
  
RUN mv ../resources/odalic-docker-repository-1.1.1/odalic /usr/local/odalic  
  
RUN rm -rf ../resources

