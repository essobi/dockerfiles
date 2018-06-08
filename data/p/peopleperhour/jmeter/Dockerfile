FROM peopleperhour/java8  
  
ENV JMETER=http://apache.cc.uoc.gr//jmeter/binaries/apache-jmeter-2.13.tgz \  
JMETER_HOME=/opt/apache-jmeter-2.13 \  
PATH=${PATH}:/opt/apache-jmeter-2.13/bin  
  
RUN apk --update add bash curl ca-certificates tar && \  
curl -Ls -o /tmp/jmeter.tar.gz ${JMETER} && \  
gunzip /tmp/jmeter.tar.gz && \  
tar -C /opt -xf /tmp/jmeter.tar && \  
rm -f /tmp/jmeter.tar* && \  
rm -fr /opt/apache-jmeter-2.13/docs \  
/opt/apache-jmeter-2.13/printable_docs  
  
# Install jmeter-plugins.org  
# http://jmeter-plugins.org/downloads/file/JMeterPlugins-Standard-1.3.1.zip  
RUN curl -Ls -o /tmp/ultimateTG.zip http://jmeter-
plugins.org/downloads/file/JMeterPlugins-Standard-1.3.1.zip && \  
unzip -o -d /opt/apache-jmeter-2.13 /tmp/ultimateTG.zip && \  
rm /tmp/ultimateTG.zip  
  
RUN apk del curl  
  
WORKDIR /opt/apache-jmeter-2.13/bin  
  
RUN chmod 0755 *.sh  
ENTRYPOINT ["jmeter"]

