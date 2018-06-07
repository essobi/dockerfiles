FROM clojure  
COPY . .  
RUN lein clean && lein uberjar  
  
FROM openjdk:jre-alpine  
ENV PORT 1236  
  
COPY \--from=0 /tmp/target/dbas.eauth-0.0.2-SNAPSHOT-standalone.jar
dbas.eauth-0.0.2-SNAPSHOT-standalone.jar  
  
  
EXPOSE $PORT  
CMD ["java", "-jar", "dbas.eauth-0.0.2-SNAPSHOT-standalone.jar"]

