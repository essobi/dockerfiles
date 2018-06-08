#  
# Onyx demo Dockerfile  
#  
# https://github.com/obiba/docker-onyx-demo  
#  
# Pull base image  
FROM jetty:9-jre8  
  
MAINTAINER OBiBa <dev@obiba.org>  
  
ENV LANG C.UTF-8  
ENV LANGUAGE C.UTF-8  
ENV LC_ALL C.UTF-8  
# Install Onyx demo  
RUN \  
cd /tmp && wget -q
http://ci.obiba.org/view/Onyx/job/Onyx%20Demo/ws/target/onyx-demo.war && mv
onyx-demo.war /var/lib/jetty/webapps/root.war && chown jetty:jetty
/var/lib/jetty/webapps/root.war  
# Define default command.  
CMD ["jetty.sh", "run"]  
  
# http  
EXPOSE 8080  

