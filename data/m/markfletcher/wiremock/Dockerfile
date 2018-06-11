FROM markfletcher/oracle-java7  
  
RUN mkdir -p /wiremock/mappings && mkdir -p /wiremock/__files  
RUN wget -O /wiremock/wiremock-standalone.jar
http://repo1.maven.org/maven2/com/github/tomakehurst/wiremock/1.57/wiremock-1.57-standalone.jar  
WORKDIR /wiremock  
  
EXPOSE 9999  
ENTRYPOINT ["java", "-jar", "wiremock-standalone.jar", "--port", "9999", "--
verbose"]  
  

