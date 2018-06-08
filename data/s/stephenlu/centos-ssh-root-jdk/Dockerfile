FROM stephenlu/centos-ssh-root  
MAINTAINER stephenlu  
# jdk  
RUN curl -LO 'http://download.oracle.com/otn-
pub/java/jdk/7u71-b14/jdk-7u71-linux-x64.rpm' -H 'Cookie:
oraclelicense=accept-securebackup-cookie'  
RUN rpm -i jdk-7u71-linux-x64.rpm  
RUN rm jdk-7u71-linux-x64.rpm  
ENV JAVA_HOME /usr/java/default  
ENV PATH $JAVA_HOME/bin:$PATH  

