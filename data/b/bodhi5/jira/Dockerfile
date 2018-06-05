# Install Atlassian Jira  
# This is a trusted build based on the "base" image, but we also need
postgresql  
FROM postgres  
  
MAINTAINER Tom Eklöf tom@linux-konsult.com  
  
ENV AppName jira  
ENV AppVer 6.3.12  
ENV Arch x64  
  
# Fetch the files  
ADD http://www.atlassian.com/software/jira/downloads/binary/atlassian-
jira-6.3.12-x64.bin /opt/  
# ADD ./atlassian-jira-6.3.12-x64.bin /opt/  
ADD ./node.json /etc/chef/node.json  
ADD ./response.varfile /opt/response.varfile  
ADD ./init.sh /init.sh  
ADD ./install_cmds.sh /  
RUN apt-get update -y && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" | tee
-a /etc/apt/sources.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" |
tee -a /etc/apt/sources.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 &&
\  
apt-get update -y  
  
RUN /install_cmds.sh  
  
VOLUME ["/home/jira/","/etc/postgresql", "/var/log/postgresql",
"/var/lib/postgresql"]  
  
# Start the service  
CMD ["sh", "/init.sh"]  
EXPOSE 8080  

