FROM ofayau/busybox-jvm  
  
MAINTAINER Olivier Fayau  
  
#  
# Download and install java : OpenJDK - java-se-8u40-ri.  
# About Compact Profiles (JEP 161) : http://openjdk.java.net/jeps/161  
# Official depo : https://jdk8.java.net/java-se-8-ri/  
#  
RUN mkdir /usr/lib/jvm \  
&& cd /usr/lib/jvm \  
&& wget
http://download.java.net/openjdk/jdk8u40/ri/jre_ri-8u40-b25-linux-i586-10_feb_2015.tar.gz
-O - | gunzip | tar x \  
&& ln -s /usr/lib/jvm/java-se-8u40-ri /usr/lib/jvm/jre  
  
CMD ["java", "-version"]  
  

