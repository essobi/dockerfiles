FROM nate9/minimaljava8  
RUN apk --update add curl tar  
ENV JMETER_VERSION 2.13  
ENV GROOVY_VERSION 2.4.5  
# Install JMeter  
RUN cd /var/lib && \  
curl http://mirror.ox.ac.uk/sites/rsync.apache.org//jmeter/binaries/apache-
jmeter-$JMETER_VERSION.tgz -o /var/lib/jmeter-$JMETER_VERSION.tgz && \  
tar xf jmeter-$JMETER_VERSION.tgz && \  
rm -f jmeter-$JMETER_VERSION.tgz  
  
#Install groovy scripting plugin  
RUN cd /var/lib && \  
curl http://central.maven.org/maven2/org/codehaus/groovy/groovy-
all/$GROOVY_VERSION/groovy-all-$GROOVY_VERSION.jar -o /var/lib/apache-
jmeter-$JMETER_VERSION/lib/groovy-all-$GROOVY_VERSION.jar  
  
ENV PATH /var/lib/apache-jmeter-$JMETER_VERSION/bin:$PATH

