FROM team3637/scoutingappbase  
  
MAINTAINER "Team 3637"  
EXPOSE 8080  
VOLUME /var/lib/mysql team3637/scoutingapp  
  
ENV CATALINA_HOME=/tomcat8  
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64  
RUN mv /tomcat8/webapps/ROOT /tomcat8/webapps/old  
RUN mkdir /tmp/ScoutingApp  
WORKDIR /tmp/ScoutingApp  
RUN git clone https://github.com/FRC-3637-Daleks/ScoutingApp.git .  
RUN sed -i 's/127.0.0.1/scoutingsql/g' web/WEB-INF/applicationContext.xml  
RUN ant  
RUN apt-get purge -y openjdk-8-jdk  
RUN apt-get autoremove -y  
RUN cp /tmp/ScoutingApp/dist/ScoutingApp.war /tomcat8/webapps/ROOT.war  
WORKDIR /tomcat8  
RUN rm -rf /tmp/ScoutingApp  
  
CMD /tomcat8/bin/catalina.sh run  

