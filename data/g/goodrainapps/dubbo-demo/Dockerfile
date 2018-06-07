FROM goodrainapps/maven:jdk7-alpine  
  
RUN mkdir /app  
  
COPY . /app/  
  
WORKDIR /app  
  
RUN mvn -B -DskipTests=true clean install  
  
ENTRYPOINT ["/app/run.sh"]

