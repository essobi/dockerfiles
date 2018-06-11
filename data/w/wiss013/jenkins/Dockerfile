FROM krallin/centos-tini  
  
MAINTAINER BEN CHAABEN Wissem<benchaaben.wissem@gmail.com>  
  
#changing the root user  
USER root  
  
#Install Jenkins Prequisites  
RUN yum update -y && \  
yum groupinstall -y 'development tools' && \  
yum install -y java-1.8.0-openjdk java-1.8.0-openjdk-devel epel-release wget  
  
#Jenkins arguments  
ARG user=jenkins  
ARG group=jenkins  
ARG uid=1000  
ARG gid=1000  
ARG http_port=8080  
ARG agent_port=50000  
#Jenkins envirements  
ENV JENKINS_HOME /var/jenkins_home  
ENV JENKINS_SLAVE_AGENT_PORT=${agent_port}  
  
#Create Jenkins user and group  
RUN groupadd -g ${gid} ${group} && \  
useradd -d "${JENKINS_HOME}" -u ${uid} -g ${gid} -m -s /bin/bash ${user}  
  
#Create jenkins volumes for persistante  
VOLUME [ "/var/jenkins_home" ]  
  
#reference configuration we want  
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d  
  
#Install Jenkins  
RUN wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat-
stable/jenkins.repo && \  
rpm --import http://pkg.jenkins-ci.org/redhat-stable/jenkins-ci.org.key && \  
yum install -y jenkins  
  
ENV JENKINS_UC https://updates.jenkins.io  
ENV JENKINS_UC_EXPERIMENTAL=https://updates.jenkins.io/experimental  
RUN chown -R ${user} "$JENKINS_HOME" /usr/share/jenkins  
  
#For web interface  
EXPOSE ${http_port}  
  
#For jenkins agent  
EXPOSE ${agent_port}  
  
ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log  
  
  
  
COPY jenkins-support /usr/local/bin/jenkins-support  
COPY jenkins.sh /usr/local/bin/jenkins.sh  
COPY install-plugins.sh /usr/local/bin/install-plugins.sh  
COPY plugins.sh /usr/local/bin/plugins.sh  
# add permissions  
RUN chmod +x -R /usr/local/bin/  
  
ENTRYPOINT [ "/bin/tini","--","/usr/local/bin/jenkins.sh" ]  
  

