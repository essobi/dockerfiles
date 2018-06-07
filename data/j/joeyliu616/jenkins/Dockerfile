# use older version  
FROM jenkins:1.651.3  
  
ENV TZ "Asia/Shanghai"  
#install net-tools jdk git  
USER root  
RUN apt-get clean && \  
apt-get update && \  
apt-get install -y openjdk-7-jdk net-tools git openssh-server sudo  
RUN rm -fr /var/lib/apt/lists/*  
  
EXPOSE 22  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
USER jenkins  
  
  
#安装maven插件  
COPY plugins.txt /usr/share/jenkins/plugins.txt  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  

