FROM logicify/centos7:latest  
  
# java8  
RUN cd /opt && \  
(curl -L -k -b "oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-pub/java/jdk/8u45-b14/server-
jre-8u45-linux-x64.tar.gz | gunzip -c | tar x) \  
&& ln -s /opt/jdk1.8.0_45 /opt/jdk  
  
ENV JAVA_HOME /opt/jdk  
ENV JRE_HOME $JAVA_HOME/jre  
ENV PATH $PATH:$JAVA_HOME/bin  

