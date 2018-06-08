FROM alpine:3.4  
RUN apk --no-cache add curl graphviz openjdk8-jre ttf-dejavu && \  
mkdir -p /opt/plantuml && \  
curl -L https://sourceforge.net/projects/plantuml/files/plantuml.jar/download
-o /opt/plantuml/plantuml.jar && \  
apk del --purge curl  
  
ENTRYPOINT ["java", "-jar", "/opt/plantuml/plantuml.jar"]  
  
CMD ["-p"]  

