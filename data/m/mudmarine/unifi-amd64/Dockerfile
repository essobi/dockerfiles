FROM debian:jessie  
MAINTAINER Matthew Brennan <matt@nannerb.org>  
  
VOLUME ["/var/lib/unifi", "/var/log/unifi", "/var/run/unifi",
"/usr/lib/unifi/work"]  
#VOLUME ["/mnt/pool/docker/unifi:/var/lib/unifi",
"/mnt/pool/docker/unifi/log:/var/log/unifi", "/var/run/unifi",
"/mnt/pool/docker/unifi/work:/usr/lib/unifi/work"]  
  
# Add MongoDB repository and developer gpg key  
RUN echo "deb http://downloads-distro.mongodb.org/repo/debian-sysvinit dist
10gen" > \  
/etc/apt/sources.list.d/mongodb.list && \  
apt-key adv --keyserver keyserver.ubuntu.com \--recv 7F0CEB10  
  
# add unifi repository to sources.list and add developer gpg key  
RUN echo "deb http://www.ubnt.com/downloads/unifi/debian unifi5 ubiquiti" >
/etc/apt/sources.list.d/ubiquiti.list && \  
apt-key adv --keyserver keyserver.ubuntu.com \--recv C0A52C50  
  
# add Oracle Java 8 PPA, accept license and developer gpg key  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee /etc/apt/sources.list.d/webupd8team-java.list &&\  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 boolean true"
| debconf-set-selections && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys EEA14886  
  
# install java, unifi (and MongoDB as dependancy) and clean up apt-get  
RUN apt-get update -qy && \  
apt-get install -qy --force-yes oracle-java8-installer oracle-java8-set-
default unifi && \  
echo "JAVA_HOME=/usr/lib/jvm/java-8-oracle" | tee /etc/default/unifi && \  
apt-get -qy upgrade && \  
apt-get -qy autoclean && \  
apt-get -qy autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
RUN ln -s /var/lib/unifi /usr/lib/unifi/data  
  
EXPOSE 6789/tcp 8080/tcp 8081/tcp 8443/tcp 8843/tcp 8880/tcp 3478/udp  
  
WORKDIR /var/lib/unifi  
  
ENTRYPOINT ["/usr/bin/java", "-Xmx1024M", "-jar",
"/usr/lib/unifi/lib/ace.jar"]  
  
CMD ["start"]  

