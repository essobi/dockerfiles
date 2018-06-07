#Base Image  
FROM ubuntu:14.04  
#Adding discription to the images  
LABEL Description="This image is used for
github->circleci->dockerhub->tutum->aws" Version="1.0"  
  
# File Author / Maintainer  
MAINTAINER pushpendra,puneet,madhu  
  
RUN apt-get update  
RUN apt-get install -y openjdk-7-jdk  
RUN apt-get install -y tomcat7  
  
ENV CATALINA_HOME /usr/share/tomcat7/  
ENV CATALINA_BASE /var/lib/tomcat7/  
ENV PATH $CATALINA_HOME/bin:$PATH  
#RUN mkdir -p "$CATALINA_HOME"  
#WORKDIR $CATALINA_HOME  
RUN apt-get install -y wget  
  
RUN wget -O /var/lib/tomcat7/webapps/EmployeeApplication.war https://circle-
artifacts.com/gh/pushpendrad/emsdockerhub/16/artifacts/0/tmp/circle-
artifacts.Aul0cx0/war/EmployeeApplication.war  
EXPOSE 8080  
CMD ["catalina.sh", "run"]  
  
#inastalling git jdk and maven  
#RUN apt-get update && apt-get install -y git maven openjdk-7-jdk  
#Setting timezone to match time zone of sonar server  
#RUN echo "Asia/Kolkata" > /etc/timezone && dpkg-reconfigure --frontend
noninteractive tzdata  
#adding jenkins user  
#RUN adduser jenkins  
#RUN echo "jenkins:jenkins" | chpasswd  
#Volume Mounting (Docker custom build env plugin copy reports by itself)  
#VOLUME ["/var/lib/jenkins"]  
#Exposing the port  
#EXPOSE 8080  
#Entry point or image starting point  
#ENTRYPOINT ["",""]  

