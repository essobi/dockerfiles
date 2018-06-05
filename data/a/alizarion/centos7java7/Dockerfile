FROM alizarion/centos7base:latest  
  
MAINTAINER Selim BENSENOUCI "selim@openlinux.fr"  
RUN yum update -y  
  
RUN cd /tmp  
RUN wget --no-cookies --no-check-certificate --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-
cookie" "http://download.oracle.com/otn-
pub/java/jdk/7u79-b15/jdk-7u79-linux-x64.rpm"  
RUN yum -y localinstall jdk-7u79-linux-x64.rpm  
RUN rm -f jdk-7u79-linux-x64.rpm  
ENV JAVA_HOME /usr/java/jdk1.7.0_79/jre  
# Define default command.  
CMD ["bash"]  

