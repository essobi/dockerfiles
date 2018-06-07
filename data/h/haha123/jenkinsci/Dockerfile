FROM haha123/jenkins  
  
USER root  
ENV DEBIAN_FRONTEND noninteractive  
RUN \  
apt-get update && \  
apt-get install -y apt-transport-https ca-certificates && \  
apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 \--recv-keys
58118E89F3A912897C070ADBF76221572C52609D && \  
echo "deb https://apt.dockerproject.org/repo debian-jessie main" >>
/etc/apt/sources.list.d/docker.list && \  
apt-get update && \  
apt-get purge docker.io && \  
apt-get install -y docker-engine  
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers  
  
USER jenkins  
COPY ./plugins.txt /usr/share/jenkins/plugins.txt  
COPY ./plugins.txt /usr/share/jenkins/ref/  
#RUN /usr/local/bin/install-plugins.sh /usr/share/jenkins/plugins.txt  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  
  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  

