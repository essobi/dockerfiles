FROM openjdk:8  
COPY . /var/opt/SuccessAnalyzer  
WORKDIR /var/opt/SuccessAnalyzer  
RUN ./bin/go bootRepackage  
ENTRYPOINT ["java","-jar","./build/libs/SuccessAnalyzer.jar"]  

