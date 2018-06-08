FROM java  
MAINTAINER denis.peyrusaubes@retengr.com  
#RUN apt-get update  
#RUN apt-get install net-tools daemon  
#RUN wget https://pkg.jenkins.io/debian-stable/binary/jenkins_2.107.3_all.deb  
#RUN dpkg -i jenkins_2.107.3_all.deb  
# node & npm install  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs  
  
# Jenkins install  
RUN wget http://ftp-nyc.osuosl.org/pub/jenkins/war-stable/2.107.3/jenkins.war  
EXPOSE 8080  
EXPOSE 5000  
ENTRYPOINT java -jar jenkins.war  

