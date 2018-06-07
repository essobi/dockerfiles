FROM clojure  
COPY . .  
RUN lein clean && lein ring uberjar  
  
FROM openjdk:jre-alpine  
ENV PORT 1235  
  
COPY \--from=0 /tmp/target/dbas-fb-hook-0.1.0-SNAPSHOT-standalone.jar dbas-fb-
hook-0.1.0-SNAPSHOT-standalone.jar  
  
  
EXPOSE $PORT  
CMD ["java", "-jar", "dbas-fb-hook-0.1.0-SNAPSHOT-standalone.jar"]

