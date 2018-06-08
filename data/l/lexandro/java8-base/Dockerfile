FROM lexandro/linux-base  
  
MAINTAINER Robert Stern <lexandro2000@<you know that big search company>.com  
  
RUN wget -qO- --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u45-b14/jdk-8u45-linux-x64.tar.gz|tar xvz  
  
ENV JAVA_HOME /jdk1.8.0_45  
ENV PATH $JAVA_HOME/bin:$PATH  

