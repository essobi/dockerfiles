FROM mbopm/ubuntu-oracle-java:2.0  
MAINTAINER Manuel Bogner <docker@mbo.pm>  
  
# install rundeck  
RUN wget -O /opt/rundeck.deb http://dl.bintray.com/rundeck/rundeck-
deb/rundeck-2.6.1-1-GA.deb && \  
dpkg -i /opt/rundeck.deb && \  
rm -rf /opt/rundeck.deb /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# change base configuration  
RUN mkdir /etc/service/rundeck && \  
mkdir /var/lib/rundeck/.ssh && \  
chown -R rundeck:rundeck /var/lib/rundeck  
# add init and startup scripts  
ADD assets/run/rundeck.sh /etc/service/rundeck/run  
ADD assets/startup/* /etc/my_init.d/  
  
# http, https  
EXPOSE 4440 4443  
# project files  
# configs  
# ssh-keys  
# logs  
VOLUME [ "/var/rundeck", "/etc/rundeck", "/var/lib/rundeck/.ssh",
"/var/log/rundeck" ]  

