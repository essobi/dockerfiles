FROM fedora  
  
ENV JDK_VERSION 1.8.0  
ENV JMETER_VERSION 3.1  
  
RUN /usr/bin/dnf install -y tar java-$JDK_VERSION-openjdk-devel.x86_64 && rm
-rf /var/cache/{yum,dnf}  
  
RUN cd /var/lib && \  
curl --silent http://ftp.fau.de/apache/jmeter/binaries/apache-
jmeter-$JMETER_VERSION.tgz -o /var/lib/jmeter-$JMETER_VERSION.tgz && \  
tar xzf jmeter-$JMETER_VERSION.tgz && \  
mv apache-jmeter* apache-jmeter && \  
rm -rf jmeter-$JMETER_VERSION.tgz  
  
ADD jmeter.properties /var/lib/apache-jmeter/bin/  
ADD user.properties /var/lib/apache-jmeter/bin/  
COPY lib/ /var/lib/apache-jmeter/lib/  
COPY lib/ext/ /var/lib/apache-jmeter/lib/ext/  

