FROM jordan/rundeck  
  
  
ENV HOME /root  
RUN apt-get update  
RUN apt-get install -y --force-yes wget curl vim  
################################  
#Plugins Installation  
################################  
COPY Plugins/rundeck-winrm-plugin-1.3.1.jar /var/lib/rundeck/libext/rundeck-
winrm-plugin-1.3.1.jar  
COPY Plugins/LogstashPlugin.groovy
/var/lib/rundeck/libext/LogstashPlugin.groovy  
COPY Plugins/rundeck-json-plugin-1.1.jar /var/lib/rundeck/libext/rundeck-json-
plugin-1.1.jar  
  
################################  
#Configuration Files  
################################  
COPY Build/resources.xml
/var/rundeck/projects/SondaRundeckPOC/etc/resources.xml  
COPY Build/WINDOWS-2012 /var/lib/rundeck/var/storage/content/keys/WINDOWS-2012  
COPY Build/rundeck-config.properties /etc/rundeck/rundeck-config.properties  
  
################################  
#Install LogStash  
################################  
RUN wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | sudo apt-
key add -  
RUN echo "deb http://packages.elastic.co/logstash/2.3/debian stable main" |
sudo tee -a /etc/apt/sources.list  
RUN sudo apt-get update -y --force-yes && sudo apt-get install -y --force-yes
logstash  
  
  
  
  

