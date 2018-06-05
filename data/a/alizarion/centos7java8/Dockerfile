FROM alizarion/centos7base:latest  
  
MAINTAINER Selim BENSENOUCI "selim@openlinux.fr"  
RUN yum update -y  
  
RUN cd /tmp  
RUN wget --no-cookies --no-check-certificate --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-
cookie" "http://download.oracle.com/otn-
pub/java/jdk/8u60-b27/jdk-8u60-linux-x64.rpm"  
RUN yum -y localinstall jdk-8u60-linux-x64.rpm  
RUN rm -f jdk-8u60-linux-x64.rpm  
ENV JAVA_HOME /usr/java/jdk1.8.0_60/jre  
# Define default command.  
CMD ["bash"]  

