FROM debian  
  
ENV HOME /root  
  
RUN apt-get update \  
&& apt-get install -y curl  
  
ENV JDK_URL 'http://download.oracle.com/otn-
pub/java/jdk/7u79-b15/jdk-7u79-linux-x64.tar.gz'  
RUN cd /opt && \  
curl -L -O -H "Cookie: oraclelicense=accept-securebackup-cookie" -k $JDK_URL
&& \  
tar -xzf jdk-*.tar.gz && rm -f jdk-*.tar.gz && \  
mv jdk* jdk && \  
AUTO_ADDED_PACKAGES=`apt-mark showauto` && \  
apt-get remove --purge -y curl $AUTO_ADDED_PACKAGES && \  
rm -rf /var/lib/apt/lists/*  
  
ENV JAVA_HOME /opt/jdk  
  
ENV PATH $PATH:$JAVA_HOME/bin  

