#  
# Copyright (c) 2001-2018 Primeton Technologies, Ltd.  
# All rights reserved.  
#  
# author: ZhongWen Li (mailto:lizw@primeton.com)  
#  
  
FROM primetoninc/jdk:1.8  
# LABEL maintainer="lizw@primeton.com" \  
# provider="Primeton Technologies, Ltd."  
# jenkins slave settings  
ENV SLAVE_WORKDIR=/opt/jenkins \  
SLAVE_RUNNABLE=/usr/share/jenkins/slave.jar \  
JAVA_VM_MEM_MIN=512 \  
JAVA_VM_MEM_MAX=4096  
  
# build environment settings  
ENV MAVEN_HOME=/opt/apache-maven-3.3.9 \  
NODE_HOME=/opt/node-v6.11.2-linux-x64 \  
ANT_HOME=/opt/apache-ant-1.10.1 \  
GRADLE_HOME=/opt/gradle-4.0.2 \  
SONAR_SCANNER_HOME=/opt/sonar-scanner-2.8  
  
ENV
PATH="${PATH}:${MAVEN_HOME}/bin:${NODE_HOME}/bin:${ANT_HOME}/bin:${GRADLE_HOME}/bin:${SONAR_SCANNER_HOME}/bin"  
# maven template settings.xml  
ADD resources/settings.xml /opt/template/maven/settings.xml  
# epel, ansible, git, etc. yum repoistory  
# ADD resources/yum.repos.d/*.repo /etc/yum.repos.d/  
ADD resources/yum.repos.d/epel.repo /etc/yum.repos.d/epel.repo  
# requirements software  
RUN curl \--fail \--location \--retry 3 \  
# Comment epel, replace with epel.repo  
# https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \  
# -o /tmp/epel-release-latest-7.noarch.rpm \  
# && rpm -ivh /tmp/epel-release-latest-7.noarch.rpm \  
# && \rm -f /tmp/epel-release-latest-7.noarch.rpm \  
# && curl --fail --location --retry 3 \  
http://opensource.wandisco.com/centos/7/git/x86_64/wandisco-git-
release-7-2.noarch.rpm \  
-o /tmp/git-release-7-2.noarch.rpm \  
&& rpm -ivh /tmp/git-release-7-2.noarch.rpm \  
&& \rm -f /tmp/git-release-7-2.noarch.rpm \  
&& yum clean all \  
&& yum -y install zip gzip unzip wget git ansible coreutils ttf-dejavu expect
iputils ftp  
  
# maven, node, ant, gradle, sonar, jenkins slave  
# maven  
RUN curl \--fail \--location \--retry 3 \  
https://archive.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz \  
-o /tmp/maven.tar.gz \  
&& tar -zvxf /tmp/maven.tar.gz -C /opt/ \  
&& \rm -f /tmp/maven.tar.gz  
# node  
RUN curl \--fail \--location \--retry 3 \  
https://nodejs.org/dist/v6.11.2/node-v6.11.2-linux-x64.tar.gz \  
-o /tmp/node.tar.gz \  
&& tar -zvxf /tmp/node.tar.gz -C /opt/ \  
&& \rm -f /tmp/node.tar.gz  
# ant  
RUN curl \--fail \--location \--retry 3 \  
https://archive.apache.org/dist/ant/binaries/apache-ant-1.10.1-bin.tar.gz \  
-o /tmp/ant.tar.gz \  
&& tar -zvxf /tmp/ant.tar.gz -C /opt/ \  
&& \rm -f /tmp/ant.tar.gz  
# gradle  
RUN curl \--fail \--location \--retry 3 \  
http://services.gradle.org/distributions/gradle-4.0.2-bin.zip \  
-o /tmp/gradle.zip \  
&& unzip /tmp/gradle.zip -d /opt/ \  
&& \rm -f /tmp/gradle.zip  
# sonar-scanner  
# https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/  
RUN curl \--fail \--location \--retry 3 \  
https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-2.8.zip \  
-o /tmp/sonar-scanner.zip \  
&& unzip /tmp/sonar-scanner.zip -d /opt/ \  
&& \rm -f /tmp/sonar-scanner.zip  
# jenkins slave  
RUN mkdir -p /usr/share/jenkins \  
&& curl \--create-dirs -sSLo ${SLAVE_RUNNABLE} \  
https://repo.jenkins-ci.org/public/org/jenkins-
ci/main/remoting/3.11/remoting-3.11.jar \  
&& chmod 755 /usr/share/jenkins \  
&& chmod 644 ${SLAVE_RUNNABLE}  
  
# ENV HOME /home/jenkins  
# RUN groupadd -g 10000 jenkins \  
# && useradd -c "Jenkins user" -d $HOME -u 10000 -g 10000 -m jenkins  
# USER jenkins  
# entrypoint, env  
ADD resources/entrypoint.sh /opt/  
RUN chmod +x /opt/entrypoint.sh \  
&& echo "registry=https://registry.npm.taobao.org" >> /root/.npmrc  
# maven local repository  
VOLUME /root/.m2  
# VOLUME /home/jenkins/.m2  
# jenkins job, workspace  
VOLUME ${SLAVE_WORKDIR}  
  
# RUN git config --global http.sslVerify false \  
# && git config --global user.name "devops" \  
# && git config --global user.email "devops@primeton.com"  
ADD resources/.gitconfig /root/.gitconfig  
# ADD resources/.gitconfig /home/jenkins/.gitconfig  
  
ENTRYPOINT [ "/opt/entrypoint.sh" ]  
  
# Usage:  
# docker run -d --name agent --rm jenkins-slave:latest -jnlpUrl
http://.../slave-agent.jnlp -secret uuid

