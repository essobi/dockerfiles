FROM philippwaller/debian:latest  
  
LABEL org.label-schema.schema-version="1.0" \  
org.label-schema.name="Java" \  
org.label-schema.description="Java"  
  
ENV JAVA_HOME=/opt/java \  
JAVA_URL=https://www.azul.com/downloads/zulu/zdk-8-ga-linux_x64.tar.gz  
  
RUN mkdir -p $JAVA_HOME \  
&& curl -L -o /tmp/java.tar.gz $JAVA_URL \  
&& tar -xzf /tmp/java.tar.gz \--strip-components=1 -C $JAVA_HOME \  
&& update-alternatives --install /usr/bin/java java $JAVA_HOME/bin/java 50 \  
&& update-alternatives --install /usr/bin/javac javac $JAVA_HOME/bin/javac 50
\  
&& rm -rf /tmp/* $JAVA_HOME/demo $JAVA_HOME/man $JAVA_HOME/readme.txt \  
&& rm -rf $JAVA_HOME/sample $JAVA_HOME/src.zip $JAVA_HOME/Welcome.html  
  
CMD /bin/bash  

