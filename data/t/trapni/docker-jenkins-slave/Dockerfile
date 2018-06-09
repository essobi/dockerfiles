FROM java  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
  
WORKDIR /srv/jenkins-slave  
  
RUN apt-get update  
RUN apt-get install -y wget supervisor  
RUN apt-get install -y docker.io  
  
ADD supervisor.conf /etc/supervisor/conf.d/jenkins-slave.conf  
  
ENV JENKINS_COMMAND /bin/false  
  
CMD ["/usr/bin/supervisord"]  

