From alpine  
LABEL maintainer="Flo S"  
  
COPY java/Compression/dist/Compression.jar /root/Compression.jar  
RUN apk --update add openjdk8-jre  
  
CMD ["/usr/bin/java", "-jar", "/root/Compression.jar"]  

