FROM ubuntu:14.04  
MAINTAINER JG  
  
  
# Commands  
# Set the locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y vim nano git wget libfreetype6 libfontconfig bzip2
supervisor zip unzip openssh-server make g++ patch zlib1g-dev libgif-dev
software-properties-common libffi-dev libssl-dev && \  
mkdir -p /srv/var /var/log/supervisor /opt  
  
RUN \  
apt-get install -y python-pip python-dev && \  
pip install ansible==1.8.4  
  
ENV TOMCAT_VERSION 7.0.59  
ENV TOMCAT_PORT 8080  
ENV TOMCAT_PATH /opt/tomcat  
  
# ----------- Install java 7 -------------  
RUN \  
wget -c -O "jdk-7u79-linux-x64.tar.gz" \--no-check-certificate --no-cookies
--header "Cookie: oraclelicense=accept-securebackup-cookie"
"http://download.oracle.com/otn-
pub/java/jdk/7u79-b15/jdk-7u79-linux-x64.tar.gz" && \  
  
tar -zxvf jdk-7u79-linux-x64.tar.gz -C / && \  
rm jdk-7u79-linux-x64.tar.gz && \  
mv /jdk1.7.0_79 /jdk  
  
ENV JAVA_HOME /jdk  
ENV JRE_HOME $JAVA_HOME/jre  
ENV PATH $PATH:$JAVA_HOME/bin  
RUN java -version  
  
# ----------- Install Tomcat -------------#  
RUN \  
wget -O /tmp/tomcat.tar.gz
http://archive.apache.org/dist/tomcat/tomcat-7/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz && \  
cd /tmp && \  
tar zxf /tmp/tomcat.tar.gz && \  
ls /tmp && \  
mv /tmp/apache-tomcat* $TOMCAT_PATH && \  
rm -rf $TOMCAT_PATH/webapps/*.* && \  
rm -rf $TOMCAT_PATH/webapps/* && \  
rm /tmp/tomcat.tar.gz  
  
EXPOSE $TOMCAT_PORT  
EXPOSE 1317  
EXPOSE 22  
# ----------- Configure SSH -------------  
#RUN echo deb http://archive.ubuntu.com/ubuntu trusty main universe >
/etc/apt/sources.list.d/trusty.list  
# Clean  
ADD es_docker_key.pub es_docker_key.pub  
  
RUN \  
mkdir ~/.ssh && \  
touch ~/.ssh/authorized_keys && \  
cat es_docker_key.pub >> ~/.ssh/authorized_keys && \  
rm es_docker_key.pub && \  
/etc/init.d/ssh restart  
  
# Files  
ADD tomcat_supervisord_wrapper.sh
$TOMCAT_PATH/bin/tomcat_supervisord_wrapper.sh  
RUN chmod 755 $TOMCAT_PATH/bin/tomcat_supervisord_wrapper.sh  
  
# Add tomcat server.xml configuration with UTF-8  
ADD server.xml $TOMCAT_PATH/conf/server.xml  
  
# Add Jenkins war  
ADD jenkins.war $TOMCAT_PATH/webapps/jenkins.war  
  
#ADD jenkins-conf.xml $TOMCAT_PATH/conf/Catalina/localhost/jenkins-conf.xml  
RUN \  
export MAVEN_OPTS="-Xmx512m -XX:MaxPermSize=256m" && \  
export ANT_OPTS="-Xmx512m -XX:MaxPermSize=256m"  
  
# ----------- Modify libraries security for jre (jar)-------------  
ADD UnlimitedJCEPolicy/local_policy.jar /jdk/jre/lib/security/local_policy.jar  
ADD UnlimitedJCEPolicy/US_export_policy.jar
/jdk/jre/lib/security/US_export_policy.jar  
  
# ----------- Install java 8 -------------  
RUN \  
wget -c -O "jdk-8u91-linux-x64.tar.gz" \--no-check-certificate --no-cookies
--header "Cookie: oraclelicense=accept-securebackup-cookie"
"http://download.oracle.com/otn-
pub/java/jdk/8u91-b14/jdk-8u91-linux-x64.tar.gz" && \  
  
tar -zxvf jdk-8u91-linux-x64.tar.gz -C / && \  
rm jdk-8u91-linux-x64.tar.gz && \  
mv /jdk1.8.0_91 /jdk8  
  
# ----------- Install maven 3.3.9 -------------  
RUN \  
wget -c -O "apache-maven-3.3.9-bin.tar.gz" \--no-check-certificate --no-
cookies "http://www-us.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz" && \  
  
tar -zxvf apache-maven-3.3.9-bin.tar.gz -C / && \  
rm apache-maven-3.3.9-bin.tar.gz && \  
mv /apache-maven-3.3.9 /maven-3.3.9  
# Start Tomcat from supervisor  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
CMD ["/usr/bin/supervisord"]  
  
#Crear Build Group  
RUN \  
groupadd build && \  
useradd --create-home --shell /bin/bash --groups build jenkins  
  
#Set JENKINS Home ENV var to /data/jenkins folder  
RUN su jenkins -c 'mkdir ~/data'  
RUN su jenkins -c 'mkdir ~/data/jenkins'  
ENV JENKINS_HOME /home/jenkins/data/jenkins  
  
ADD es_docker_key.pub es_docker_key.pub  
  
RUN \  
su jenkins -c '\  
mkdir ~/.ssh && \  
touch ~/.ssh/authorized_keys && \  
cat es_docker_key.pub >> ~/.ssh/authorized_keys'  
RUN \  
rm es_docker_key.pub && \  
/etc/init.d/ssh restart  
  
RUN \  
su jenkins -c '\  
mkdir ~/sshKeys'  
  
RUN mkdir -p $TOMCAT_PATH/webapps/TestReports/AutomatedTests  
RUN mkdir -p $TOMCAT_PATH/webapps/TestReports/UnitTests  
  
RUN \  
su jenkins -c '\  
mkdir -p ~/ansible_playbooks/continuous_delivery/'  
  
RUN \  
apt-get install -y p7zip-full  
  
ADD deploy_key.pub deploy_key.pub  
  
RUN \  
cat deploy_key.pub >> ~/.ssh/authorized_keys && \  
rm deploy_key.pub && \  
/etc/init.d/ssh restart  
  
ADD ansible.cfg /etc/ansible/ansible.cfg

