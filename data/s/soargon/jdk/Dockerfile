FROM ubuntu  
  
MAINTAINER soargon <soargon@gmail.com>  
  
ENV JDK_TGZ_URL http://download.oracle.com/otn-
pub/java/jdk/7u67-b01/jdk-7u67-linux-x64.tar.gz  
  
ENV JAVA_HOME /usr/local/jdk/jdk1.7.0_67  
  
RUN apt-get update && apt-get -y install wget --no-install-recommends && rm
-rf /var/lib/apt/lists/* \  
&& wget -t 3 -nv --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" $JDK_TGZ_URL -O jdk.tar.gz \  
&& apt-get purge -y --auto-remove wget \  
&& mkdir /usr/local/jdk \  
&& tar -zxf jdk.tar.gz -C /usr/local/jdk \  
&& rm jdk.tar.gz* \  
&& rm -rf $JAVA_HOME/src.zip $JAVA_HOME/javafx-src.zip $JAVA_HOME/man  
  
ENV PATH $JAVA_HOME/bin:$PATH  

