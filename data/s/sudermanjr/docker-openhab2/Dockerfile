FROM debian:jessie  
  
#Install the openhab apt key  
ADD https://bintray.com/user/downloadSubjectPublicKey?username=openhab
/tmp/openhab.key  
RUN apt-key add /tmp/openhab.key  
  
#Add the OpenHAB Repo  
RUN echo "deb http://dl.bintray.com/openhab/apt-repo2 testing main" >>
/etc/apt/sources.list  
  
#Install dumb-init  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64.deb /tmp/dumb-init.deb  
RUN dpkg -i /tmp/dumb-init.deb && rm /tmp/dumb-init.deb  
  
#Install Java and OpenHAB  
RUN \  
echo "===> add webupd8 repository..." && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee
/etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \  
apt-get update && \  
\  
\  
echo "===> install Java" && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes openhab2-offline
oracle-java8-installer oracle-java8-set-default && \  
\  
\  
echo "===> clean up..." && \  
rm -rf /var/cache/oracle-jdk8-installer && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
#Configure extra stuff for Z-wave  
RUN adduser openhab dialout && adduser openhab tty  
RUN echo 'EXTRA_JAVA_OPTS="-Dgnu.io.rxtx.SerialPorts=/dev/ttyS0"' >
/etc/default/openhab2  
  
ENTRYPOINT ["/usr/bin/dumb-init", "/usr/share/openhab2/start.sh"]  

