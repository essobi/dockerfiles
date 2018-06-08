FROM ubuntu:trusty  
  
# add ``Oracle Java JRE`` to repository (what's weird is that this key
presents as ``Launchpad VLC``)  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 \  
&& echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu $(lsb_release
-cs) main" \  
> /etc/apt/sources.list.d/launchpad-webupd8team-java.list \  
&& echo debconf shared/accepted-oracle-license-v1-1 select true \  
| sudo debconf-set-selections \  
&& echo debconf shared/accepted-oracle-license-v1-1 seen true \  
| sudo debconf-set-selections  
  
# install ``cURL`` and ``Java 7 JRE`` which is supported by ``Atlassian Jira``  
RUN apt-get update -qq \  
&& apt-get install -qqy wget curl oracle-java7-installer  
  
# setup primary environment variables  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
ENV JIRA_HOME /home/jira  
# setup secondary environment helper variables  
ENV JIRA_VERSION 6.3.1  
# create non-root user to run ``Atlassian Jira``  
RUN useradd --create-home --comment "Account for running JIRA" jira \  
&& chmod -R a+rw ~jira  
  
# download ``Atlassian Jira`` standalone archive version  
RUN wget "http://www.atlassian.com/software/jira/downloads/binary/atlassian-
jira-${JIRA_VERSION}.tar.gz" \  
&& tar -xzf "atlassian-jira-${JIRA_VERSION}.tar.gz" \  
&& rm "atlassian-jira-${JIRA_VERSION}.tar.gz" \  
&& mkdir -p /usr/local/atlassian \  
&& mv "atlassian-jira-${JIRA_VERSION}-standalone" /usr/local/atlassian/jira \  
&& chown -R jira:jira /usr/local/atlassian/jira \  
&& chmod -R 777 /usr/local/atlassian/jira/temp \  
&& chmod -R 777 /usr/local/atlassian/jira/logs \  
&& chmod -R 777 /usr/local/atlassian/jira/work  
  
# set the principal user as new non-root jira account  
USER jira  
  
# expose default HTTP and tomcat shutdown port  
EXPOSE 8080 8005  
# set volume mount points for ``Atlassian Jira`` installation and home
directory  
VOLUME ["/home/jira", "/usr/local/atlassian/jira"]  
  
# run ``Atlassian Jira`` as a foreground process  
CMD /usr/local/atlassian/jira/bin/start-jira.sh -fg  

