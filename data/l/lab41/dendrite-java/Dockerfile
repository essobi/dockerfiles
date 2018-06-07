FROM lab41/dendrite-build  
MAINTAINER Charlie Lewis <charliel@lab41.org>  
  
# java  
RUN wget --quiet --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" -O jdk-7u51-linux-x64.tar.gz
http://download.oracle.com/otn-pub/java/jdk/7u51-b13/jdk-7u51-linux-x64.tar.gz  
RUN mkdir -p /usr/lib/jvm; \  
mv jdk-7u51-linux-x64.tar.gz /usr/lib/jvm; \  
tar zxvf /usr/lib/jvm/jdk-7u51-linux-x64.tar.gz -C /usr/lib/jvm; \  
rm /usr/lib/jvm/jdk-7u51-linux-x64.tar.gz  
RUN update-alternatives --install /usr/bin/javac javac
/usr/lib/jvm/jdk1.7.0_51/bin/javac 1; \  
update-alternatives --install /usr/bin/java java
/usr/lib/jvm/jdk1.7.0_51/bin/java 1; \  
update-alternatives --set javac /usr/lib/jvm/jdk1.7.0_51/bin/javac; \  
update-alternatives --set java /usr/lib/jvm/jdk1.7.0_51/bin/java  
RUN echo 'JAVA_HOME=/usr/lib/jvm/jdk1.7.0_51' >> /etc/profile; \  
echo 'PATH=$PATH:$JAVA_HOME/bin' >> /etc/profile; \  
echo 'export JAVA_HOME' >> /etc/profile; \  
echo 'export PATH' >> /etc/profile  
ENV JAVA_HOME /usr/lib/jvm/jdk1.7.0_51  
ENV JRE_HOME /usr/lib/jvm/jdk1.7.0_51  
ENV PATH $PATH:$JAVA_HOME/bin  
  
# fix java due to tomcat installing java6  
RUN unlink /usr/lib/jvm/default-java; \  
ln -s /usr/lib/jvm/jdk1.7.0_51 /usr/lib/jvm/default-java  

