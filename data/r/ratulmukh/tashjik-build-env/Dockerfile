FROM ubuntu:14.04  
# Install Java.  
RUN \  
apt-get update && \  
apt-get install -y openjdk-7-jdk && \  
rm -rf /var/lib/apt/lists/*  
  
# Define working directory.  
WORKDIR /data  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
  
RUN apt-get update && apt-get -y install git  
  
RUN apt-get install -y wget  
  
# Install Scala and SBT  
RUN wget www.scala-lang.org/files/archive/scala-2.11.6.deb  
RUN dpkg -i scala-2.11.6.deb  
RUN apt-get update && apt-get install scala  
RUN wget http://dl.bintray.com/sbt/debian/sbt-0.13.8.deb  
RUN dpkg -i sbt-0.13.8.deb  
RUN apt-get update && apt-get install sbt  
  
# Define default command.  
CMD ["bash"]  
  

