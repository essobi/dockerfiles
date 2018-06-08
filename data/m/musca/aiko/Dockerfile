# Pull base image.  
FROM williamyeh/java8  
ENV TERM screen  
  
  
# Add application  
RUN AIKO_LATEST_VERSION=$(wget -q -O-
https://dl.bintray.com/neofonie/maven/de/neofonie/aiko/maven-metadata.xml |
grep -oP '(?<=<latest>).*?(?=</latest>)') \  
&& mkdir -p /opt/application/ \  
&& cd /opt/application/ \  
&& wget -q
https://dl.bintray.com/neofonie/maven/de/neofonie/aiko/$AIKO_LATEST_VERSION/aiko-$AIKO_LATEST_VERSION.jar
\  
&& mv aiko-$AIKO_LATEST_VERSION.jar application.jar  
ADD payloads/aiko /usr/local/bin/aiko  
RUN chmod a+x /usr/local/bin/aiko  
  
# Set working dir  
WORKDIR /opt/application  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# Define entrypoint  
CMD ["bash"]  

