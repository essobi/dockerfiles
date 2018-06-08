FROM podbox/debian  
  
# ------------------------------------------------------------------------
java8  
RUN (curl -L -k -b "oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-pub/java/jdk/8u60-b27/server-
jre-8u60-linux-x64.tar.gz | gunzip -c | tar x) \  
&& mv /jdk1.8.0_60 /jdk  
  
ENV JAVA_HOME /jdk  
ENV JRE_HOME $JAVA_HOME/jre  
ENV PATH $PATH:$JAVA_HOME/bin  

