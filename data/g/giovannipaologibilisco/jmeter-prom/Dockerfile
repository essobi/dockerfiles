# Use JDK-8 on alpine.  
FROM openjdk:8-alpine  
ENV JMETER_VERSION 3.2  
# Install Pre-requisite Packages like wget  
RUN apk update && apk add wget unzip  
# Installing jmeter  
RUN mkdir /jmeter \  
&& cd /jmeter/ \  
&& wget https://archive.apache.org/dist/jmeter/binaries/apache-
jmeter-$JMETER_VERSION.tgz \  
&& tar -xzf apache-jmeter-$JMETER_VERSION.tgz \  
&& rm apache-jmeter-$JMETER_VERSION.tgz  
# Settingt Jmeter Home  
ENV JMETER_HOME /jmeter/apache-jmeter-$JMETER_VERSION  
# Finally Adding Jmeter to the Path  
ENV PATH $JMETER_HOME/bin:$PATH  
COPY ./plugins/lib $JMETER_HOME/lib  
EXPOSE 1099 60000 9270  
ENTRYPOINT jmeter -n -t /tmp/data/$SCRIPT_NAME -R $REMOTE_SERVERS
-Djava.rmi.server.hostname=$HOST_IP -Jurl=$SERVER_IP  

