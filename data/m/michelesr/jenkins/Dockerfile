FROM jenkins:latest  
  
MAINTAINER Michele Sorcinelli "mikefender@cryptolab.net"  
USER root  
RUN apt-get update \  
&& apt-get install -y python python-pip sudo \  
&& rm -rf /var/lib/apt/lists/*  
RUN pip install 'docker-compose==1.4'  
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers  
  
USER jenkins  
COPY plugins.txt /usr/share/jenkins/plugins.txt  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  

