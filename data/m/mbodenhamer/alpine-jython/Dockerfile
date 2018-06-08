FROM anapsix/alpine-java:latest  
MAINTAINER Matt Bodenhamer <mbodenhamer@mbodenhamer.com>  
  
ENV JYTHON_VERSION 2.7.0  
RUN apk add --no-cache \  
curl  
  
RUN curl -L "http://search.maven.org/remotecontent?filepath=org/python/jython-
installer/${JYTHON_VERSION}/jython-installer-${JYTHON_VERSION}.jar" -o
jython_installer-${JYTHON_VERSION}.jar && \  
java -jar jython_installer-${JYTHON_VERSION}.jar -s -d
/jython-${JYTHON_VERSION} -i ensurepip && \  
ln -s /jython-${JYTHON_VERSION}/bin/jython /usr/bin && \  
ln -s /jython-${JYTHON_VERSION}/bin/pip /usr/bin && \  
rm jython_installer-${JYTHON_VERSION}.jar  
  
CMD ["jython"]  

