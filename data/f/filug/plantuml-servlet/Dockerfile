FROM tomcat:8.0  
MAINTAINER Piotr L. Figlarek <piotr.figlarek@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN \  
apt-get update &&\  
apt-get install -y graphviz &&\  
apt-get clean &&\  
apt-get autoremove -y &&\  
rm -rf /var/cache/apt/*  
  
RUN rm -r /usr/local/tomcat/webapps/*  
RUN wget http://sourceforge.net/projects/plantuml/files/plantuml.war/download
-O /usr/local/tomcat/webapps/plantuml.war  
  
EXPOSE 8080  

