FROM seven10builder/jenkins-master-base:1.642.2  
MAINTAINER kmilner@seven10storage.com  
  
USER root  
RUN sudo apt-get update &&\  
sudo apt-get install -y python-pip && \  
sudo pip install --upgrade pip &&\  
pip install docker-cloud  
  
USER jenkins  
COPY plugins.txt /usr/share/jenkins/plugins.txt  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  
USER root  
CMD ["/usr/local/bin/setup-docker-and-start-jenkins.sh"]

