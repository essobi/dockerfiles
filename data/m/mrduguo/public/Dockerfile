FROM jenkins:1.625.3  
COPY src/main/docker/files /  
USER root  
  
RUN apt-get update --fix-missing && \  
apt-get -y \  
install \  
telnet \  
net-tools \  
less \  
vim && \  
apt-get -y clean && \  
apt-get -q -y autoremove  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/ref/plugins.txt  
  
ENV JAVA_OPTS
-Djava.util.logging.config.file=/usr/share/jenkins/log.properties

