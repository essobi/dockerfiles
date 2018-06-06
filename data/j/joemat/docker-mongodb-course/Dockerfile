FROM joemat/mongo:latest  
  
#  
# Install Java 7  
# copied from https://github.com/andreptb/Dockerfiles/blob/master/oracle-
java/jdk-7/Dockerfile  
#  
ENV JAVA_VERSION 7  
# Install Java and Maven  
RUN \  
echo oracle-java$JAVA_VERSION-installer shared/accepted-oracle-license-v1-1
select true | debconf-set-selections && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" | tee
/etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 &&
\  
apt-get update && \  
apt-get -y install augeas-tools curl oracle-java$JAVA_VERSION-installer
oracle-java$JAVA_VERSION-unlimited-jce-policy maven && \  
apt-get clean  
  
# Define working directory.  
WORKDIR /data  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-$JAVA_VERSION-oracle  
  
#  
# Install mongoProc and dependencies  
#  
RUN curl "https://s3.amazonaws.com/edu-
downloads.10gen.com/3.0/mongoProc_3.0_linux_x86_64.tar.gz" | tar -C /opt -zxvf
- && \  
apt-get -y install libglib2.0 libX11-6 libgl1-mesa-glx libqt5gui5
libqt5network5 libqt5widgets5 libx11-xcb1 libgl1-mesa-dev && \  
apt-get clean  

