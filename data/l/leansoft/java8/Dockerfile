FROM phusion/baseimage  
  
ENV JAVA_HOME /usr/jdk1.8.0_91  
  
RUN curl \  
\--silent \  
\--location \  
\--retry 3 \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
"http://download.oracle.com/otn-pub/java/jdk/8u91-b14/server-
jre-8u91-linux-x64.tar.gz" \  
| gunzip \  
| tar x -C /usr/ \  
&& ln -s $JAVA_HOME /usr/java \  
&& rm -rf $JAVA_HOME/man  
  
ENV PATH ${PATH}:${JAVA_HOME}/bin

