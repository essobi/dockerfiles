FROM lgsd/diamond  
MAINTAINER Maxime Tricoire <max.tricoire@gmail.com> (@maxleiko)  
  
ENV JAVA_HOME /usr/lib/jvm/java-se-8-ri-compact2  
ENV PATH $PATH:$JAVA_HOME/bin  
  
ADD java-se-8-ri-compact2 $JAVA_HOME/  
  
ADD lib/ld-linux.so.2 /lib/  
ADD lib32 /lib/  
RUN chmod +x /lib/*  
  
ADD cacerts ${JAVA_HOME}/lib/security/  

