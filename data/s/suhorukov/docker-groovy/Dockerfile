FROM openjdk:10-jdk  
  
EXPOSE 8080  
ENV GROOVY_VERSION=2.4.15  
RUN mkdir "/usr/lib/groovy" && \  
cd "/tmp" && \  
wget "http://repo1.maven.org/maven2/com/github/igor-suhorukov/groovy-grape-
aether/$GROOVY_VERSION/groovy-grape-aether-$GROOVY_VERSION.jar" && \  
mv "/tmp/groovy-grape-aether-$GROOVY_VERSION.jar" /usr/lib/groovy/groovy-
grape-aether.jar  
  
ENTRYPOINT ["java","-jar","/usr/lib/groovy/groovy-grape-aether.jar"]  
  
CMD ["--help"]  

