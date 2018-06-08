FROM centos:6  
RUN yum install -y wget  
  
WORKDIR /opt/  
  
RUN wget --no-cookies --no-check-certificate --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-
cookie" "http://download.oracle.com/otn-
pub/java/jdk/8u121-b13/e9e7ea248e2c4826b92b3f075a80e441/jdk-8u121-linux-x64.tar.gz"  
RUN tar xzf jdk-8u121-linux-x64.tar.gz  
RUN cd /opt/jdk1.8.0_121/  
RUN alternatives --install /usr/bin/java java /opt/jdk1.8.0_121/bin/java 2  
RUN alternatives --set java /opt/jdk1.8.0_121/bin/java  
  
RUN alternatives --install /usr/bin/jar jar /opt/jdk1.8.0_121/bin/jar 2 &&
alternatives --install /usr/bin/javac javac /opt/jdk1.8.0_121/bin/javac 2  
RUN alternatives --set jar /opt/jdk1.8.0_121/bin/jar && alternatives --set
javac /opt/jdk1.8.0_121/bin/javac  
CMD /bin/bash  

