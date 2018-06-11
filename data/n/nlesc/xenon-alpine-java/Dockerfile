FROM nlesc/xenon-alpine-base  
  
RUN apk --no-cache add openjdk8-jre bash  
  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk/jre/  
ENV PATH $JAVA_HOME/bin:$PATH  
  
RUN echo "export JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk/jre" >
/home/xenon/.bashrc && \  
echo "export PATH=$JAVA_HOME/bin:$PATH" >> /home/xenon/.bashrc && \  
chown -R xenon.xenon /home/xenon/.bashrc  
  

