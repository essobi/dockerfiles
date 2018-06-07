FROM openhpi/docker_exec  
MAINTAINER openHPI team <openhpi-info@hpi.de>  
RUN apt-get install -y make wget  
RUN mkdir /usr/java && wget -O java.tar.gz http://download.oracle.com/otn-
pub/java/jdk/8u40-b25/jdk-8u40-linux-x64.tar.gz --header "Cookie:
oraclelicense=accept-securebackup-cookie" && tar xfz java.tar.gz -C /usr/java  
ENV JAVA_HOME /usr/java/jdk1.8.0_40  
ENV PATH $PATH:$JAVA_HOME/bin  
RUN mkdir /usr/java/lib  
ADD hamcrest-core-1.3.jar /usr/java/lib/  
ADD junit-4.11.jar /usr/java/lib/  

