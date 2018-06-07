FROM jeejen/ubuntu:16.04  
  
RUN mkdir /usr/lib/jvm && \  
curl -v -j -k -L -H "Cookie: oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.tar.gz
\  
> /usr/lib/jvm/java.tar.gz && \  
cd /usr/lib/jvm && \  
tar -xzvf java.tar.gz && \  
rm -rf /usr/lib/jvm/java.tar.gz && \  
rm -rf /usr/lib/jvm/jdk1.8.0_131/src.zip  
  
ENV JAVA_HOME=/usr/lib/jvm/jdk1.8.0_131  
ENV PATH=$PATH:$JAVA_HOME/bin  

