FROM phusion/baseimage  
MAINTAINER Jaigouk Kim "ping@jaigouk.kim"  
ENV JENKINS_VER 1.596  
RUN groupadd -r jenkins && useradd -r -g jenkins jenkins  
RUN echo "update system and install needed deps" \  
&& apt-get update -y -qq \  
&& apt-get install -y -qq wget curl daemon psmisc monit git openssh-server
build-essential openjdk-7-jre-headless \  
&& echo "install jenkins" \  
&& curl -s -L -o /tmp/jenkins_${JENKINS_VER}_all.deb http://pkg.jenkins-
ci.org/debian/binary/jenkins_${JENKINS_VER}_all.deb \  
&& dpkg -i /tmp/jenkins_${JENKINS_VER}_all.deb \  
&& apt-get -fy install \  
&& mkdir -p /downloaded_plugins \  
&& chown -R jenkins /downloaded_plugins \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# grab gosu for easy step-down from root  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
ENV JENKINS_HOME /data/jenkins  
ENV JENKINS_JAVA_ARGS '-Djava.awt.headless=true'  
ENV JENKINS_MAXOPENFILES 8192  
ENV JENKINS_PREFIX /data/jenkins  
ENV JENKINS_ARGS '--webroot=/var/cache/jenkins/war --httpPort=8080
--ajp13Port=-1'  
ENV DEBIAN_FRONTEND noninteractive  
EXPOSE 8080 2812 22 36562 33848/udp  
  
ADD ./scripts /scripts  
ADD ./scripts/jenkins-entrypoint.sh /entrypoint.sh  
ADD ./config.xml $JENKINS_HOME/config.xml  
RUN /scripts/download_plugins.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["/usr/bin/java", "-jar", "/usr/share/jenkins/jenkins.war"]

