FROM opensuse:leap  
MAINTAINER flanaras  
  
USER root  
ENV USER root  
  
RUN zypper up -y \  
&& zypper in -y wget  
  
RUN wget -q -c --header "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jdk/8u151-b12/e758a0de34e24606bca991d704f6dcbf/jre-8u151-linux-x64.rpm
\  
&& rpm -ivh jre-8u151-linux-x64.rpm \  
&& rm jre-8u151-linux-x64.rpm  
  
RUN zypper rm -y wget  
  
# Setup java path  
ENV JAVA_HOME /usr/java/default  
ENV PATH $PATH:$JAVA_HOME/bin  

