FROM jenkins:1.625.1  
MAINTAINER Radek Antoniuk <radek.antoniuk@quiddia.com>  
  
USER root  
RUN wget https://get.docker.io/builds/Linux/x86_64/docker-1.8.3 -O /bin/docker
&& chmod +x /bin/docker  
ADD startupscript.sh /usr/local/bin/jenkins_start.sh  
  
CMD ["/usr/local/bin/jenkins_start.sh"]  
  

