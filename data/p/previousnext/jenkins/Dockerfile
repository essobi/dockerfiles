FROM previousnext/base  
MAINTAINER Nick Schuch "nick@previousnext.com.au"  
##  
# Jenkins.  
##  
# Java.  
RUN RUNLEVEL=1 DEBIAN_FRONTEND=noninteractive apt-get install -y wget
openjdk-7-jre-headless git-core  
  
# Repository.  
RUN wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | apt-key
add -  
RUN echo "deb http://pkg.jenkins-ci.org/debian binary/" >
/etc/apt/sources.list.d/jenkins.list  
RUN apt-get update  
  
# Install.  
RUN RUNLEVEL=1 DEBIAN_FRONTEND=1 apt-get install -y jenkins ttf-dejavu  
RUN rm -f /usr/share/jenkins/jenkins.war  
ADD http://mirrors.jenkins-ci.org/war-stable/latest/jenkins.war
/usr/share/jenkins/jenkins.war  
RUN chmod 644 /usr/share/jenkins/jenkins.war  
  
# Plugins.  
RUN mkdir -p /opt/jenkins/plugins  
RUN (cd /opt/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/download/plugins/greenballs/1.13/greenballs.hpi)  
RUN (cd /opt/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/download/plugins/instant-messaging/1.27/instant-
messaging.hpi)  
RUN (cd /opt/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/download/plugins/ircbot/2.23/ircbot.hpi)  
RUN (cd /opt/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-
ci.org/download/plugins/credentials/1.9.4/credentials.hpi)  
RUN (cd /opt/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/download/plugins/ssh-credentials/1.5.1/ssh-
credentials.hpi)  
RUN (cd /opt/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/download/plugins/ssh-agent/1.4/ssh-agent.hpi)  
RUN (cd /opt/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/download/plugins/git-client/1.6.1/git-
client.hpi)  
RUN (cd /opt/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/download/plugins/git/2.0.1/git.hpi)  
RUN (cd /opt/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/download/plugins/scm-api/0.2/scm-api.hpi)  
RUN (cd /opt/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/download/plugins/simple-theme-plugin/0.3/simple-
theme-plugin.hpi)  
RUN (cd /opt/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/download/plugins/swarm/1.15/swarm.hpi)  
RUN (cd /opt/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/download/plugins/checkstyle/3.38/checkstyle.hpi)  
RUN (cd /opt/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/download/plugins/ansicolor/0.3.1/ansicolor.hpi)  
RUN (cd /opt/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-
ci.org/download/plugins/postbuildscript/0.16/postbuildscript.hpi)  
RUN (cd /opt/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/download/plugins/token-macro/1.9/token-
macro.hpi)  
RUN (cd /opt/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/download/plugins/analysis-core/1.54/analysis-
core.hpi)  
RUN (cd /opt/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/download/plugins/dashboard-view/2.9.2/dashboard-
view.hpi)  
RUN (cd /opt/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/download/plugins/maven-plugin/2.3/maven-
plugin.hpi)  
RUN (cd /opt/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/download/plugins/jquery/1.7.2-1/jquery.hpi)  
RUN (cd /opt/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/download/plugins/ghprb/1.12/ghprb.hpi)  
RUN (cd /opt/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/download/plugins/github-api/1.58/github-api.hpi)  
RUN (cd /opt/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/download/plugins/github/1.8/github.hpi)  
RUN (cd /opt/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/download/plugins/github-oauth/0.20/github-
oauth.hpi)  
RUN (cd /opt/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/download/plugins/mailer/1.8/mailer.hpi)  
RUN (cd /opt/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/download/plugins/sidebar-link/1.6/sidebar-
link.hpi)  
RUN (cd /opt/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/download/plugins/ws-cleanup/0.21/ws-cleanup.hpi)  
RUN (cd /opt/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/download/plugins/role-strategy/2.2.0/role-
strategy.hpi)  
RUN (cd /opt/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/download/plugins/slack/1.8/slack.hpi)  
RUN echo "java -Djava.awt.headless=true -jar /usr/share/jenkins/jenkins.war" >
/usr/local/bin/run && chmod +x /usr/local/bin/run  
  
ENV JENKINS_HOME /var/lib/jenkins  
  
##  
# Supervisord.  
##  
ADD ./conf/supervisor/supervisord.conf /etc/supervisord.conf  
  
##  
# Startup scripts.  
##  
ADD ./scripts/start.sh /root/start.sh  
RUN chmod 755 /root/start.sh  
  
EXPOSE 8080 22  
VOLUME /var/lib/jenkins  
  
CMD ["/root/start.sh"]  

