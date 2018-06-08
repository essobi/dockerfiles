# build this Dockerfile using command docker build -t punithc/javaapibuild .  
FROM centos:7  
MAINTAINER "punith.wip@gmail.com"  
ENV container docker  
RUN yum -y install git  
RUN yum -y install wget  
RUN wget --no-cookies --no-check-certificate --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-
cookie" "http://download.oracle.com/otn-
pub/java/jdk/8u66-b17/jdk-8u66-linux-x64.tar.gz"  
RUN tar xzf jdk-8u66-linux-x64.tar.gz -C /opt/  
RUN cd /opt/jdk1.8.0_66/  
RUN echo "export JAVA_HOME=/opt/jdk1.8.0_66" >> ~/.bash_profile  
RUN echo "export PATH=$PATH:/opt/jdk1.8.0_66/bin:/opt/jdk1.8.0_66/jre/bin" >>
~/.bash_profile  
# run this command in the host system where the Docker build file is present  
# ssh-keygen -q -t rsa -N '' -f repo-key  
# Add the repo-key.pub to your repository deployment keys in bitbucket  
ADD repo-key /  
RUN \  
chmod 600 /repo-key && \  
echo "IdentityFile /repo-key" >> /etc/ssh/ssh_config && \  
echo -e "StrictHostKeyChecking no" >> /etc/ssh/ssh_config && \  
git clone git@bitbucket.org:digitalrigbitbucketteam/api-demo-swagger.git  
  
ENV JAVA_HOME /opt/jdk1.8.0_66  
ENV PATH $PATH:$JAVA_HOME/bin  
EXPOSE 9120  
# RUN api-repo/gradlew -p api-repo clean build run  
# Run your docker image to spin container with below command (for build with
tag v1)  
# docker run -d -p 80:9120 --name pc_api_demo punithc/javaapibuild:v1 api-
repo/gradlew -p api-repo clean build run  
# Run your docker image to spin container with below command (for build with
tag as latest)  
# docker run -d -p 80:9120 --name pc_api_demo punithc/javaapibuild api-
repo/gradlew -p api-repo clean build run  

