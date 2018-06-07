FROM thefactory/java  
MAINTAINER Mike Babineau mike@thefactory.com  
  
RUN apt-get update && apt-get -y install unzip  
  
# Pull Twitter-built Kestrel jar  
ADD include/pom.xml /opt/kestrel/pom.xml  
RUN cd /opt/kestrel && mvn assembly:single && ln -s
/opt/kestrel/target/kestrel-1.0-jar-with-dependencies.jar
/opt/kestrel/kestrel.jar  
  
ADD include/wrapper.sh /opt/kestrel/wrapper.sh  
  
USER root  
WORKDIR /opt/kestrel  
EXPOSE 2222 2223 2229 22133  
ENTRYPOINT ["bash", "-e", "/opt/kestrel/wrapper.sh"]  
  

