FROM ubuntu:14.04  
MAINTAINER Discovery Dev <adsdiscoveryteam@pillartechnology.com>  
  
ENV DB_USER=sonar  
ENV DB_PASS=xaexohquaetiesoo  
ENV DB_NAME=sonar  
ENV SONARQUBE_HOME /opt/sonarqube  
  
  
RUN locale-gen en_US.UTF-8  
RUN update-locale LANG=en_US.UTF-8  
RUN apt-get -qq update  
RUN sudo apt-get install -y --force-yes openjdk-7-jre  
  
RUN echo "deb http://downloads.sourceforge.net/project/sonar-pkg/deb binary/"
>> /etc/apt/sources.list  
RUN apt-get update && apt-get clean ### Sonar version 5.1 - timestamp  
  
RUN apt-get install -y --force-yes sonar=5.1  
  
COPY assets/init /app/init  
RUN chmod 755 /app/init  
  
VOLUME /opt/sonar/extensions  
VOLUME /opt/sonar/logs/  
  
COPY sonar-objective-c-plugin-0.4.0.jar $SONARQUBE_HOME/extensions/plugins/  
RUN rm -rf /opt/sonar/conf/sonar.properties  
COPY sonar.properties /opt/sonar/conf/  
EXPOSE 9000  
EXPOSE 443  
ENTRYPOINT ["/app/init"]  
CMD ["app:start"]  

