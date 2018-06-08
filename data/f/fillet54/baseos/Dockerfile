FROM centos:7  
  
RUN curl -LO \--insecure \--junk-session-cookies \--location \--remote-name
\--silent \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-pub/java/jdk/8u74-b02/jdk-8u74-linux-x64.rpm &&
\  
yum localinstall -y jdk-8u74-linux-x64.rpm && \  
yum clean all && \  
rm jdk-8u74-linux-x64.rpm  
  
ENV JAVA_HOME /usr/java/default

