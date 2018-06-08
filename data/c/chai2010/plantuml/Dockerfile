FROM frolvlad/alpine-oraclejdk8  
  
LABEL maintainer="chaishushan@gmil.com"  
  
ENV PLANTUML_VERSION=1.2018.0  
RUN \  
apk add --no-cache graphviz wget ca-certificates && \  
wget
"http://downloads.sourceforge.net/project/plantuml/${PLANTUML_VERSION}/plantuml.${PLANTUML_VERSION}.jar"
-O plantuml.jar && \  
apk del wget ca-certificates  
  
ENV LANG en_US.UTF-8  
ENTRYPOINT ["java", "-Djava.awt.headless=true", "-jar", "plantuml.jar", "-p",
"-charset", "utf-8"]  
  
CMD ["-tsvg"]  

