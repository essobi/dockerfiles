FROM jenkins:2.7.1  
USER root  
  
# Java 8 and fakeroot for javafx builds  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee /etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 &&
\  
apt-get update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get --no-install-recommends -y install oracle-java8-installer && \  
apt-get --no-install-recommends -y install fakeroot && \  
apt-get purge -y openjdk-8-jdk && \  
apt-get purge -y openjdk-8-jre && \  
apt-get purge -y openjdk-8-jre-headless && \  
rm -rf /var/lib/apt/lists/*  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle/  
  
  
# Let Jenkins be sudoer  
RUN apt-get update && \  
apt-get --no-install-recommends -y install sudo && \  
echo "jenkins ALL = (ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
rm -rf /var/lib/apt/lists/*  
  
# For (Web) UI Test install xvnc to provide virtual display  
RUN apt-get update && \  
apt-get -y install vnc4server && \  
rm -rf /var/lib/apt/lists/*  
  
RUN echo 'deb http://downloads.sourceforge.net/project/ubuntuzilla/mozilla/apt
all main' > /etc/apt/sources.list.d/ubuntuzilla.list && \  
apt-key adv --recv-keys --keyserver keyserver.ubuntu.com C1289A29 && \  
apt-get update && \  
apt-get install firefox &&\  
apt-get --no-install-recommends -y install libgtk-3-0&&\  
rm -rf /var/lib/apt/lists/*  
  
ADD passwd /usr/share/jenkins/ref/.vnc/passwd  
ADD xstartup /usr/share/jenkins/ref/.vnc/xstartup  
ADD dotXauthority /usr/share/jenkins/ref/.Xauthority  
RUN chown jenkins:jenkins /usr/share/jenkins/ref/.vnc/passwd  
RUN chown jenkins:jenkins /usr/share/jenkins/ref/.vnc/xstartup  
RUN chown jenkins:jenkins /usr/share/jenkins/ref/.Xauthority  
RUN chmod 0600 /usr/share/jenkins/ref/.vnc/passwd  
RUN chmod 0600 /usr/share/jenkins/ref/.Xauthority  
  
USER jenkins  
  
COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/executors.groovy  
COPY plugins.txt /usr/share/jenkins/plugins.txt  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  
  
ENV DOCKER_GID_ON_HOST ""  
COPY jenkins.sh /usr/local/bin/jenkins.sh  
  

