FROM centos:6.6  
MAINTAINER Jimmy The Dog <jimmythedog@kgibbs.co.uk>  
  
WORKDIR /opt  
  
RUN yum install -y tar  
  
RUN curl --insecure --junk-session-cookies --location --remote-name --silent \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-pub/java/jdk/7u75-b13/jdk-7u75-linux-x64.tar.gz  
  
RUN tar -xvf jdk-7u75-linux-x64.tar.gz  
RUN rm jdk-7u75-linux-x64.tar.gz  
RUN ln -s jdk1.7.0_75 java  
  
ENV JAVA_HOME /opt/java  
ENV PATH $PATH:$JAVA_HOME/bin  

