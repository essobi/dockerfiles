FROM debian:jessie  
  
RUN \  
apt-get update && \  
apt-get install -y curl && \  
apt-get install unzip  
  
# add webupd8 repository  
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
DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes oracle-
java8-installer oracle-java8-set-default && \  
\  
\  
echo "===> clean up..." && \  
rm -rf /var/cache/oracle-jdk8-installer && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Define working directory.  
WORKDIR /icy  
  
# Install Icy.  
RUN \  
cd /icy && \  
wget -O icy.zip
http://www.icy.bioimageanalysis.org/downloadIcy/icy_1.9.5.2b.zip && \  
#wget http://www.icy.bioimageanalysis.org/downloadIcy/icy.zip && \  
unzip icy.zip  
  
#ADD icy_patch.jar /icy/icy.jar  
# Add icy to the PATH  
ENV PATH $PATH:/icy  
  
RUN mkdir /icy/data  
RUN mkdir /icy/data/in  
RUN mkdir /icy/protocols  

