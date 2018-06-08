FROM primetoninc/jdk:1.8  
# CentOS 7 based image  
LABEL maintainer="Jose M. Sampayo <j.m.sampayo@live.com>"  
  
# Jenkins Slave -> SETTINGS  
ENV SLAVE_WORKDIR=/opt/jenkins \  
SLAVE_RUNNABLE=/usr/share/jenkins/slave.jar \  
JAVA_VM_MEM_MIN=512 \  
JAVA_VM_MEM_MAX=4096  
# Build environment -> SETTINGS  
ENV GRADLE_HOME=/opt/gradle-4.0.2  
ENV PATH="${PATH}:${GRADLE_HOME}/bin"  
# Build stages -> REQUIREMENTS  
ADD resources/yum.repos.d/epel.repo /etc/yum.repos.d/epel.repo  
  
# SOFTWARE  
RUN curl --fail --location --retry 3 \  
http://opensource.wandisco.com/centos/7/git/x86_64/wandisco-git-
release-7-2.noarch.rpm \  
-o /tmp/git-release-7-2.noarch.rpm \  
&& rpm -ivh /tmp/git-release-7-2.noarch.rpm \  
&& \rm -f /tmp/git-release-7-2.noarch.rpm \  
&& yum clean all \  
&& yum -y install unzip wget git  
  
# GRADLE  
RUN curl --fail --location --retry 3 \  
http://services.gradle.org/distributions/gradle-4.0.2-bin.zip \  
-o /tmp/gradle.zip \  
&& unzip /tmp/gradle.zip -d /opt/ \  
&& \rm -f /tmp/gradle.zip  
  
# JENKINS SLAVE  
RUN mkdir -p /usr/share/jenkins \  
&& curl --create-dirs -sSLo ${SLAVE_RUNNABLE} \  
https://repo.jenkins-ci.org/public/org/jenkins-
ci/main/remoting/3.11/remoting-3.11.jar \  
&& chmod 755 /usr/share/jenkins \  
&& chmod 644 ${SLAVE_RUNNABLE}  
  
# Configuring entrypoint  
ADD resources/entrypoint.sh /opt/  
RUN chmod +x /opt/entrypoint.sh  
  
# Creating volume for Jenkins jobs  
VOLUME ${SLAVE_WORKDIR}  
# Configuring git  
ADD resources/.gitconfig /root/.gitconfig  
  
ENTRYPOINT [ "/opt/entrypoint.sh" ]

