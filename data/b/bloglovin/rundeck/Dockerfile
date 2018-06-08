FROM debian:wheezy  
MAINTAINER Jordan Jethwa  
ENV DEBIAN_FRONTEND noninteractive  
ENV SERVER_URL http://localhost:4440  
  
RUN apt-get -qq update && \  
apt-get -qqy upgrade && \  
apt-get -qqy install --no-install-recommends wget bash supervisor procps sudo
ca-certificates openjdk-7-jre-headless openssh-client mysql-server mysql-
client pwgen curl git && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ADD http://dl.bintray.com/rundeck/rundeck-deb/rundeck-2.5.3-1-GA.deb
/tmp/rundeck.deb  
ADD content/ /  
  
RUN dpkg -i /tmp/rundeck.deb && rm /tmp/rundeck.deb && \  
chown rundeck:rundeck /tmp/rundeck && \  
chmod u+x /opt/run && \  
mkdir -p /var/lib/rundeck/.ssh && \  
wget -O /var/lib/rundeck/libext/rundeck-salt-plugin-0.3.jar
https://github.com/rundeck-plugins/salt-step/releases/download/0.3/rundeck-
salt-plugin-0.3.jar && \  
wget -O /var/lib/rundeck/libext/rundeck-json-plugin-1.1.jar
https://github.com/rundeck-plugins/rundeck-json-
plugin/releases/download/v1.1/rundeck-json-plugin-1.1.jar && \  
wget -O /var/lib/rundeck/libext/jira-notification-1.0.0.jar
https://github.com/rundeck-plugins/jira-
notification/releases/download/v1.0.0/jira-notification-1.0.0.jar && \  
wget -O /var/lib/rundeck/libext/jira-workflow-step-1.0.0.jar
https://github.com/rundeck-plugins/jira-workflow-
step/releases/download/v1.0.0/jira-workflow-step-1.0.0.jar && \  
wget -O /var/lib/rundeck/libext/rundeck-slack-incoming-webhook-
plugin-0.4.jar.gz https://github.com/higanworks/rundeck-slack-incoming-
webhook-plugin/releases/download/v0.4.dev/rundeck-slack-incoming-webhook-
plugin-0.4.jar.gz && \  
chown rundeck:rundeck /var/lib/rundeck/.ssh && \  
mkdir -p /var/log/supervisor && mkdir -p /opt/supervisor && \  
chmod u+x /opt/supervisor/rundeck && chmod u+x
/opt/supervisor/mysql_supervisor  
  
EXPOSE 4440 4443  
  
VOLUME ["/etc/rundeck", "/var/rundeck", "/var/lib/rundeck", "/var/lib/mysql",
"/var/log/rundeck"]  
  
# Start Supervisor  
ENTRYPOINT ["/opt/run"]  

