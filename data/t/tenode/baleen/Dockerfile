# Use a Oracle JDK base image  
FROM committed/java  
MAINTAINER Dstl <https://github.com/dstl/baleen>  
  
# Baleen installation and configuration  
ENV BALEEN_VERSION 2.4.0  
  
# Download the (English) OpenNLP Name Entity Recognition models  
RUN mkdir -p /opt/baleen/models \  
&& wget -q -P /opt/baleen/models/
http://opennlp.sourceforge.net/models-1.5/en-ner-date.bin \  
&& wget -q -P /opt/baleen/models/
http://opennlp.sourceforge.net/models-1.5/en-ner-location.bin \  
&& wget -q -P /opt/baleen/models/
http://opennlp.sourceforge.net/models-1.5/en-ner-money.bin \  
&& wget -q -P /opt/baleen/models/
http://opennlp.sourceforge.net/models-1.5/en-ner-organization.bin \  
&& wget -q -P /opt/baleen/models/
http://opennlp.sourceforge.net/models-1.5/en-ner-percentage.bin  \  
&& wget -q -P /opt/baleen/models/
http://opennlp.sourceforge.net/models-1.5/en-ner-person.bin \  
&& wget -q -P /opt/baleen/models/
http://opennlp.sourceforge.net/models-1.5/en-ner-time.bin  
  
# Now create the necessary directories (/baleen used as a volume, /opt/baleen
for the jars):  
  
# Either, download the Jars direct from github releases  
RUN mkdir -p /baleen \  
&& mkdir -p /opt/baleen \  
&& wget -q -O /opt/baleen/baleen.jar
https://github.com/dstl/baleen/releases/download/v${BALEEN_VERSION}/baleen-${BALEEN_VERSION}.jar
\  
&& wget -q -O /opt/baleen/baleen-javadoc.jar
https://github.com/dstl/baleen/releases/download/v${BALEEN_VERSION}/baleen-${BALEEN_VERSION}-javadoc.jar  
# Or, if you have a local version you can comment out the wget above  
# and use the ADD line instead.  
# ADD baleen-${BALEEN_VERSION}.jar /opt/baleen/baleen.jar  
# ADD baleen-${BALEEN_VERSION}-javadoc.jar /opt/baleen/baleen-javadoc.jar  
  
# Mount /baleen as the working directory, expose the Baleen's standard port  
VOLUME /baleen  
WORKDIR /baleen  
EXPOSE 6413  
  
# Always run Baleen  
ENTRYPOINT ["java", "-jar", "/opt/baleen/baleen.jar"]  

