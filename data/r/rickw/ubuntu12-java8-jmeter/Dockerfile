# We base our image on Ubuntu 12.04 (Precise Pangolin) with Java 8 and Maven
installed  
FROM rickw/ubuntu12-java8  
  
ENV JMETER_VERSION 2.11  
# Fetch and unpack JMeter  
RUN wget -q http://archive.apache.org/dist/jmeter/binaries/apache-
jmeter-$JMETER_VERSION.tgz  
RUN tar zxf apache-jmeter-$JMETER_VERSION.tgz  
  
# Add JMeter to the PATH  
ENV PATH /apache-jmeter-$JMETER_VERSION/bin:$PATH  
  
# Expose the control port of JMeter  
EXPOSE 4445  
# Add scripts and configurations and use that directory  
ADD . /performance  
WORKDIR /performance  
  
# Default runs with server and config.yml arguments  
CMD ["200", "60", "localhost"]  
ENTRYPOINT ["./runner.sh"]

