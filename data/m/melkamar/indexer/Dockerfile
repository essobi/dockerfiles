FROM openjdk:8-jdk  
COPY ./ /indexer-build  
WORKDIR /indexer-build  
RUN cp /indexer-build/docker/application.properties /indexer-
build/src/main/resources/application.properties && \  
./gradlew bootJar && \  
rm -rf /root/.gradle && \  
mkdir -p /indexer && \  
mv build/libs/indexer*.jar /indexer/ && \  
mv /indexer-build/docker-entrypoint.sh /  
  
WORKDIR /indexer  
CMD ["/docker-entrypoint.sh"]  

