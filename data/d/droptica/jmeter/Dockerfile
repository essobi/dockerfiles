FROM java:8  
WORKDIR /app  
  
ENV JMETER_VERSION 3.1  
ENV JMETER_PATH /usr/share/jmeter  
  
RUN curl -L -o apache-jmeter-$JMETER_VERSION.zip
http://ftp.ps.pl/pub/apache//jmeter/binaries/apache-jmeter-$JMETER_VERSION.zip
\  
&& unzip apache-jmeter-$JMETER_VERSION.zip \  
&& mv apache-jmeter-$JMETER_VERSION $JMETER_PATH \  
&& rm apache-jmeter-$JMETER_VERSION.zip  
  
ENV PATH ${PATH}:$JMETER_PATH/bin/  
  
ENTRYPOINT ["jmeter"]  
  
CMD []

