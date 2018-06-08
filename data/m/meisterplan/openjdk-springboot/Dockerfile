FROM openjdk:8-jdk  
  
EXPOSE 8080 8081 5005  
ENV SERVICE_JAR /service.jar  
ENV SERVER_PORT 8080  
# Spring Boot 1.x specific  
ENV MANAGEMENT_PORT 8081  
# Spring Boot 2.x specific  
ENV MANAGEMENT_SERVER_PORT 8081  
ENV JMX_CONFIG="-Dcom.sun.management.jmxremote=true \  
-Dcom.sun.management.jmxremote.ssl=false \  
-Dcom.sun.management.jmxremote.authenticate=false \  
-Dcom.sun.management.jmxremote.local.only=false \  
-Dcom.sun.management.jmxremote.port=5005 \  
-Dcom.sun.management.jmxremote.rmi.port=5005 \  
-Djava.rmi.server.hostname=127.0.0.1"  
ENV JAVA_OPTS ""  
# By default 320mb non heap memory is reserved.  
ENV JAVA_NON_HEAP_MEMORY_BYTES 320000000  
ENV JAVA_MAX_METASPACE_SIZE 96m  
ENV JAVA_STACK_SIZE 256k  
ENV JAVA_RESERVED_CODE_CACHE_SIZE 16m  
ENV JAVA_COMPRESSED_CLASS_SPACE_SIZE 16m  
ENV JAVA_MAX_DIRECT_MEMORY_SIZE 16m  
  
ADD "run.sh" "/run.sh"  
  
CMD ["./run.sh"]  

