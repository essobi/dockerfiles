FROM debian:jessie  
  
MAINTAINER Ignacio Cabrera <cabrerabywaters@gmail.com>  
#################################################################  
#Host configuration  
#################################################################  
#  
#  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
ENV SERVER_URL https://localhost:4443  
ENV RUNDECK_STORAGE_PROVIDER db  
ENV RUNDECK_PROJECT_STORAGE_TYPE db  
ENV NO_LOCAL_MYSQL true  
  
#################################################################  
#Install Dependencies  
#################################################################  
#  
#  
#  
RUN apt-get -qq update && apt-get -qqy upgrade && apt-get -qqy install --no-
install-recommends bash supervisor procps sudo ca-certificates openjdk-7-jre-
headless openssh-client mysql-server mysql-client pwgen curl git wget curl vim
&& apt-get clean  
RUN curl -Lo /tmp/rundeck.deb http://dl.bintray.com/rundeck/rundeck-
deb/rundeck-2.6.6-1-GA.deb  
ADD content/ /  
RUN dpkg -i /tmp/rundeck.deb && rm /tmp/rundeck.deb  
RUN chown rundeck:rundeck /tmp/rundeck  
RUN chmod u+x /opt/run  
RUN mkdir -p /var/lib/rundeck/.ssh  
RUN chown rundeck:rundeck /var/lib/rundeck/.ssh  
  
###########################################################  
# Supervisor  
###########################################################  
  
RUN mkdir -p /var/log/supervisor && mkdir -p /opt/supervisor  
RUN chmod u+x /opt/supervisor/rundeck && chmod u+x
/opt/supervisor/mysql_supervisor  
  
  
###########################################################  
# Give a chance to customize default installation  
###########################################################  
  
RUN sed -i "s/export RDECK_JVM=\"/export RDECK_JVM=\"\${RDECK_JVM} /"
/etc/rundeck/profile  
  
  
#################################################################  
#Plugins Installation  
#################################################################  
#  
#Copy all plugins to the corresponding folders  
#  
#  
  
################################  
# Winrm plugin  
################################  
COPY content/Plugins/rundeck-winrm-plugin-1.3.1.jar
/var/lib/rundeck/libext/rundeck-winrm-plugin-1.3.1.jar  
################################  
# LogStash plugin  
################################  
COPY content/Plugins/LogstashPlugin.groovy
/var/lib/rundeck/libext/LogstashPlugin.groovy  
################################  
# Json Node plugin  
################################  
COPY content/Plugins/rundeck-json-plugin-1.1.jar
/var/lib/rundeck/libext/rundeck-json-plugin-1.1.jar  
################################  
# Ansible plugin  
################################  
COPY content/Plugins/ansible-plugin-1.2.3.jar /var/lib/rundeck/libext/ansible-
plugin-1.2.3.jar  
################################  
# Slack plugin  
################################  
COPY content/Plugins/rundeck-slack-incoming-webhook-plugin-0.5.jar
/var/lib/rundeck/libext/rundeck-slack-incoming-webhook-plugin-0.5.jar  
  
################################  
#Change Img Logo  
################################  
COPY content/imgs/logo-sonda.png /var/rundeck/logo-sonda.png  
  
################################  
#Private Key for Rundeck  
################################  
COPY content/Build/id_rsa /var/lib/rundeck/.ssh/id_rsa  
COPY content/Build/id_rsa.pub /var/lib/rundeck/.ssh/id_rsa.pub  
  
  
#################################################################  
#Rundeck Custom Configuration  
#################################################################  
#  
# Copy the custom configuration to properly configure  
# Email and DB settings.  
#  
COPY content/Build/rundeck-config.groovy /etc/rundeck/rundeck-config.groovy  
#################################################################  
#Rundeck Logstash configuration  
#################################################################  
COPY content/Build/rundeck-logstash.conf /root/rundeck-logstash.conf  
  
  
RUN sudo apt-get clean  
RUN sudo apt-get update  
RUN sudo dpkg --configure -a  
RUN sudo apt-get -f install  
################################  
#Install LogStash  
################################  
RUN wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | sudo apt-
key add -  
RUN echo "deb http://packages.elastic.co/logstash/2.3/debian stable main" |
sudo tee -a /etc/apt/sources.list  
RUN sudo apt-get update -y --force-yes && sudo apt-get install -y --force-yes
logstash  
  
EXPOSE 4440 4443  
  
VOLUME ["/etc/rundeck", "/var/rundeck", "/var/lib/rundeck", "/var/lib/mysql",
"/var/log/rundeck", "/opt/rundeck-plugins"]  
  
# Start Supervisor  
ENTRYPOINT ["/opt/run"]  

