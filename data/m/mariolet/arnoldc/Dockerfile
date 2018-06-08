FROM java:8-jdk  
  
RUN mkdir /arnoldc/  
WORKDIR /arnoldc/  
RUN wget http://lhartikk.github.io/ArnoldC.jar  
  
WORKDIR /src/  
ENTRYPOINT ["java", "-jar", "/arnoldc/ArnoldC.jar", "-run"]  

