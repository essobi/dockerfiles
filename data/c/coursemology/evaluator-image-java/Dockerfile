FROM coursemology/evaluator-image-base:latest  
MAINTAINER Coursemology <coursemology@googlegroups.com>  
  
# Set HOME variable to a location accessible by the coursemology user  
ENV HOME /home/coursemology  
  
RUN echo 'deb http://http.debian.net/debian jessie-backports main' >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y wget \  
&& cd $HOME \  
&& mkdir lib \  
&& cd lib \  
&& wget http://central.maven.org/maven2/org/testng/testng/6.11/testng-6.11.jar
\  
&& wget
http://central.maven.org/maven2/com/beust/jcommander/1.72/jcommander-1.72.jar
\  
&& apt-get install -t jessie-backports -y openjdk-8-jdk \  
&& update-java-alternatives --set java-1.8.0-openjdk-amd64 \  
&& apt-get install -y ant \  
&& apt-get install -y testng \  
&& apt-get remove -y wget \  
&& apt-get remove -y software-properties-common \  
&& rm -rf /var/lib/apt/lists/*  

