# 2016-01-27  
# PostgreSQL server for Quartermaster project  
FROM ubuntu  
MAINTAINER aaryndo@gmail.com  
  
RUN apt-get update && apt-get install -y wget  
RUN wget -q -O - https://jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-
key add -  
RUN sudo sh -c 'echo deb http://pkg.jenkins-ci.org/debian binary/ >
/etc/apt/sources.list.d/jenkins.list'  
  
RUN apt-get update && apt-get install -y \  
curl \  
git \  
jenkins  
  
RUN sed -i 's/HTTP_PORT=8080/HTTP_PORT=9090/g' /etc/default/jenkins  
  
EXPOSE 9090  
EXPOSE 50000  
CMD /etc/init.d/jenkins start && tail -f /dev/null

