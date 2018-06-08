# Centos based container with Java  
# use the centos base image 6.6  
FROM centos:6.6  
MAINTAINER Sourish Dutta  
  
# Prepare environment  
ENV JAVA_HOME /usr/java/latest  
ENV PATH $PATH:$JAVA_HOME/bin  
  
ENV JAVA_VERSION 8u60  
ENV BUILD_VERSION b27  
  
# Upgrading system  
RUN yum -y upgrade && yum clean all  
  
# Installing utilities  
RUN yum -y install sudo wget tar vim sed which openssh openssh-server openssh-
clients && yum clean all  
  
# Downloading Java  
RUN wget --no-cookies --no-check-certificate --header "Cookie:
oraclelicense=accept-securebackup-cookie" \  
"http://download.oracle.com/otn-
pub/java/jdk/$JAVA_VERSION-$BUILD_VERSION/jdk-$JAVA_VERSION-linux-x64.rpm" \  
-O /tmp/jdk-8-linux-x64.rpm  
  
# Installing Java  
RUN yum -y install /tmp/jdk-8-linux-x64.rpm  
  
RUN alternatives --install /usr/bin/java java /usr/java/latest/bin/java 200000  
RUN alternatives --install /usr/bin/javaws javaws /usr/java/latest/bin/javaws
200000  
RUN alternatives --install /usr/bin/javac javac /usr/java/latest/bin/javac
200000  
RUN alternatives --install /usr/bin/jar jar /usr/java/latest/bin/jar 200000  
  
# Java version check  
CMD ["java", "-version"]  
  
# expose ports for ssh  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]

