FROM ubuntu:trusty  
MAINTAINER Daniel Yokomizo <daniel.yokomizo@gmail.com>  
  
RUN apt-get update \  
&& apt-get install --yes \  
nano \  
openjdk-7-jre \  
wget  
  
COPY Jubler-5.1-generic.jar.sha512 /opt/Jubler-5.1-generic.jar.sha512  
COPY Jubler-5.1-generic.jar.xml /opt/Jubler-5.1-generic.jar.xml  
  
RUN wget --quiet --directory-prefix=/opt
https://ufpr.dl.sourceforge.net/project/jubler/Jubler%20Binary%20Releases/5.1/Jubler-5.1-generic.jar
\  
&& sha512sum --check /opt/Jubler-5.1-generic.jar.sha512 \  
&& java -jar /opt/Jubler-5.1-generic.jar /opt/Jubler-5.1-generic.jar.xml \  
&& rm /opt/Jubler-5.1-generic.jar /opt/Jubler-5.1-generic.jar.sha512
/opt/Jubler-5.1-generic.jar.xml  
  
CMD ["/usr/bin/java", "-jar", "/opt/Jubler-5.1/Jubler.jar"]  

