FROM ubuntu:xenial  
MAINTAINER Jemstep Dev <dev@jemstep.com>  
  
ENV TERM xterm-color  
  
# Install Oracle Java 8  
ENV JAVA_VER 8  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
RUN echo 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main' >
/etc/apt/sources.list.d/webupd8team-ubuntu-java.list && \  
echo 'deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main' >
/etc/apt/sources.list.d/webupd8team-ubuntu-java-src.list && \  
echo 'deb http://dl.bintray.com/sbt/debian /' > /etc/apt/sources.list.d/sbt-
bintray.list && \  
apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys C2518248EEA14886
99E82A75642AC823 && \  
apt-get update && \  
apt-get install -y \--force-yes --no-install-recommends software-properties-
common sudo openssh-client apt-transport-https \  
gnupg2 gnupg-curl hopenpgp-tools file bash-completion iputils-ping bind9-host
traceroute netcat tcpdump \  
strace psmisc wget curl bzip2 ca-certificates lsof vim bc emacs ruby2.3 ruby-
bundler firefox=45.0.2+build1-0ubuntu1 && \  
curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | sudo apt-key
add \- && \  
echo 'deb https://deb.nodesource.com/node_8.x xenial main' >
/etc/apt/sources.list.d/nodesource.list && \  
echo 'deb-src https://deb.nodesource.com/node_8.x xenial main' >>
/etc/apt/sources.list.d/nodesource.list && \  
apt-get update && \  
apt-get install nodejs -y \--force-yes && \  
npm install npm -g && \  
npm install mustache -g && \  
npm install kongfig -g && \  
wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
&& \  
echo 86dd9a4bf4aee45f1a84c9f61cf1947c1d6dce9b9e8d2a907105da7852460d2f
phantomjs-2.1.1-linux-x86_64.tar.bz2 >
phantomjs-2.1.1-linux-x86_64.tar.bz2.sha256 && \  
sha256sum --check phantomjs-2.1.1-linux-x86_64.tar.bz2.sha256 && \  
mkdir /opt/phantomjs && \  
tar -xf phantomjs-2.1.1-linux-x86_64.tar.bz2 -C /opt/phantomjs/ && \  
sudo ln -s /opt/phantomjs/phantomjs-2.1.1-linux-x86_64/bin/phantomjs
/usr/bin/phantomjs && \  
rm phantomjs-2.1.1-linux-x86_64.tar.bz2
phantomjs-2.1.1-linux-x86_64.tar.bz2.sha256 && \  
apt-add-repository -y ppa:git-core/ppa && \  
apt-get update && \  
echo oracle-java${JAVA_VER}-installer shared/accepted-oracle-license-v1-1
select true | sudo /usr/bin/debconf-set-selections && \  
apt-get install -y \--force-yes --no-install-recommends oracle-
java${JAVA_VER}-installer oracle-java${JAVA_VER}-set-default oracle-
java${JAVA_VER}-unlimited-jce-policy sbt git && \  
apt-mark hold firefox && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists && \  
rm -rf /var/cache/oracle-jdk${JAVA_VER}-installer && \  
rm -rf ${JAVA_HOME}/ct.sym && \  
rm -rf ${JAVA_HOME}/src.zip && \  
rm -rf ${JAVA_HOME}/javafx-src.zip && \  
rm -rf ${JAVA_HOME}/lib/visualvm && \  
rm -rf ${JAVA_HOME}/lib/missioncontrol  

