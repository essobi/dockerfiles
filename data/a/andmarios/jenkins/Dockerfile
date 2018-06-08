FROM centos:latest  
MAINTAINER Marios Andreopoulos <opensource@andmarios.com>  
  
RUN yum install -y epel-release \  
&& yum install -y https://centos7.iuscommunity.org/ius-release.rpm \  
&& yum groupinstall -y 'Development Tools' \  
&& yum remove -y git \  
&& yum install -y \  
git2u \  
mercurial \  
java-1.8.0-openjdk-headless \  
java-1.8.0-openjdk-devel \  
nano \  
wget \  
net-tools \  
jq \  
ncftp \  
tar \  
bzip2 \  
sudo \  
golang \  
python-pip python-pillow \  
mock \  
&& pip install Sphinx mkdocs \  
&& pip install sphinxcontrib-blockdiag \  
&& echo "progress = dot:mega" | tee /etc/wgetrc  
  
# RUN curl -sL https://rpm.nodesource.com/setup | bash - \  
# && yum install -y nodejs  
# RUN wget https://services.gradle.org/distributions/gradle-2.13-bin.zip -O
/tmp/gradle-2.13.zip \  
# && unzip /tmp/gradle-2.13.zip -d /opt/ \  
# && rm -f /tmp/gradle-2.13.zip  
RUN curl http://pkg.jenkins-ci.org/redhat/jenkins.repo | tee
/etc/yum.repos.d/jenkins.repo \  
&& rpm --import http://pkg.jenkins-ci.org/redhat/jenkins-ci.org.key \  
&& yum install -y jenkins  
  
# Prepare for Jenkins. Jenkins user is already set by `yum install jenkins`  
ENV JENKINS_HOME /mnt/jenkins  
ENV HOME /mnt/jenkins  
RUN mkdir /mnt/jenkins \  
&& chown -R jenkins:jenkins /mnt/jenkins \  
&& usermod -a -G root jenkins  
  
# Since we use shared volumes and bind mounts, we want a standardized UID/GID.
We use a number above `login.defs` max  
# Jenkins UID/GID: 61001  
RUN find / -path /proc -prune -o -user jenkins -exec chown -h 61001 {} \; \  
&& find / -path /proc -prune -o -group jenkins -exec chgrp -h 61001 {} \; \  
&& usermod --uid 61001 jenkins \  
&& groupmod --gid 61001 jenkins \  
&& usermod --gid 61001 jenkins  
  
# Interestingly on CentOS 7 you can't bind mount a socket inside /run, this
way it will be mounted a /  
RUN ln -s /docker.sock /run/docker.sock  
  
USER jenkins  
# ENV GRADLE_HOME=/opt/gradle-2.13  
ENV JAVA_HOME=/usr/lib/jvm/java  
ENV PATH="$PATH:$GRADLE_HOME/bin"  
WORKDIR /mnt/jenkins  
VOLUME ["/mnt/jenkins"]  
EXPOSE 8080  
CMD ["java", "-jar", "/usr/lib/jenkins/jenkins.war",
"-Dhudson.diyChunking=true"]  

