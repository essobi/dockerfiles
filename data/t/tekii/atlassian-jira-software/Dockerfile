#  
# jira-software Dockerfile  
#  
#  
FROM tekii/server-jre  
  
MAINTAINER Pablo Jorge Eduardo Rodriguez <pr@tekii.com.ar>  
  
LABEL version=7.3.1  
  
COPY config.patch /opt/atlassian/jira/  
  
USER root  
  
RUN apt-get \--quiet=2 update && \  
apt-get \--quiet=2 install \--assume-yes \--no-install-recommends wget patch
&& \  
echo "start downloading and decompressing
https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-
software-7.3.1.tar.gz" && \  
wget -q -O -
https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-
software-7.3.1.tar.gz | tar -xz \--strip=1 -C /opt/atlassian/jira && \  
echo "end downloading and decompressing." && \  
cd /opt/atlassian/jira && patch \--strip=1 \--input=config.patch && cd \- && \  
apt-get purge \--assume-yes wget patch && \  
apt-get \--quiet=2 autoremove \--assume-yes && \  
apt-get \--quiet=2 clean && \  
apt-get \--quiet=2 autoclean && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/ && \  
mkdir \--parents /opt/atlassian/jira/conf/Catalina && \  
chmod \--recursive 700 /opt/atlassian/jira/conf/Catalina && \  
chmod \--recursive 700 /opt/atlassian/jira/logs && \  
chmod \--recursive 700 /opt/atlassian/jira/temp && \  
chmod \--recursive 700 /opt/atlassian/jira/work && \  
chown \--recursive root:root /opt/atlassian/jira && \  
chown \--recursive daemon:daemon /opt/atlassian/jira/logs && \  
chown \--recursive daemon:daemon /opt/atlassian/jira/temp && \  
chown \--recursive daemon:daemon /opt/atlassian/jira/work && \  
chown \--recursive daemon:daemon /opt/atlassian/jira/conf/Catalina  
#  
ENV JIRA_HOME=/var/atlassian/application-data/jira  
# override by conf/bin/user.sh  
ENV JIRA_USER=daemon  
# default value for the tomcat contextPath, to be override by kubernetes  
ENV CATALINA_OPTS="-Dtekii.contextPath="  
#  
ENV JAVA_OPTS="-Datlassian.plugins.enable.wait=300"  
# you must 'chown __USER__.__GROUP__ .' this directory in the host in  
# order to allow the jira user to write in it.  
VOLUME /var/atlassian/application-data/jira  
# HTTP Port  
EXPOSE 8080  
# HTTPS Proxy Port  
EXPOSE 8443  
#  
USER daemon:daemon  
  
ENTRYPOINT ["/opt/atlassian/jira/bin/start-jira.sh", "-fg"]  

