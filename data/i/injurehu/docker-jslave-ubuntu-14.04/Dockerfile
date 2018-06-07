FROM ubuntu:14.04  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
RUN apt-get -q update  
RUN apt-get -q install -y openjdk-7-jre-headless wget  
RUN apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f
/var/cache/apt/*.bin  
  
# Set user jenkins to the image  
RUN useradd -m -d /home/jenkins -s /bin/sh jenkins &&\  
echo "jenkins:jenkins" | chpasswd  
  
COPY start-slave.sh /home/jenkins/  
#VOLUME /home/jenkins  
USER jenkins  
WORKDIR /home/jenkins  
CMD /home/jenkins/start-slave.sh  

