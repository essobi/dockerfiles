FROM andreptb/oracle-java:8-alpine  
  
ONBUILD COPY $FILE $FILE  
ONBUILD COPY $ENTRYPOINT $ENTRYPOINT  
EXPOSE 8080  
ONBUILD RUN chmod +x $ENTRYPOINT  
ONBUILD ENTRYPOINT ["/bin/sh","-c","test -e $ENTRYPOINT && $ENTRYPOINT java
-Djava.security.egd=file:/dev/./urandom $JAVA_OPTS -jar $FILE"]  

