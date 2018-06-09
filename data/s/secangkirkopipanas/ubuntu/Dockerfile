FROM ubuntu:latest  
MAINTAINER Robertus Lilik Haryanto <robert.djokdja@gmail.com>  
  
# Add webupd8 repository  
RUN \  
echo "### Add 0x mirror (Singapore)" && \  
echo "deb http://mirror.0x.sg/ubuntu/ xenial main" | tee
/etc/apt/sources.list.d/0x-mirror.list && \  
echo "deb-src http://mirror.0x.sg/ubuntu/ xenial main" | tee -a
/etc/apt/sources.list.d/0x-mirror.list && \  
echo "deb http://kambing.ui.ac.id/ubuntu/ xenial main" | tee
/etc/apt/sources.list.d/kambing.ui.ac.id.list && \  
echo "deb-src http://kambing.ui.ac.id/ubuntu/ xenial main" | tee -a
/etc/apt/sources.list.d/kambing.ui.ac.id.list && \  
\  
\  
echo "### Add webupd8 repository..." && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee
/etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys EEA14886 && \  
apt-get update  
  
RUN \  
echo "### Install Oracle Java 8" && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \--allow-downgrades --allow-
remove-essential --allow-change-held-packages oracle-java8-installer oracle-
java8-set-default  
  
RUN \  
echo "### Install few applications" && \  
apt-get install -y nano wget zip telnet  
  
RUN \  
echo "### Clean up..." && \  
rm -rf /var/cache/oracle-jdk8-installer && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV PATH $PATH:$JAVA_HOME/bin  
ENV TZ Asia/Singapore  
  
# Define default command  
CMD ["/bin/bash"]

