FROM java:8  
MAINTAINER Suparit Krityakien <suparit@wongnai.com>  
  
ENV TZ Asia/Bangkok  
ENV JAVA_OPTS -Xmx7g  
  
RUN wget -q -O data-exporter.jar https://github.com/wongnai/relation-data-
exporter/releases/download/0.1.0/data-exporter-0.1.0.jar  
  
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/data-
exporter.jar"]  
  
CMD ["export", "/tmp/settings.yaml"]  

