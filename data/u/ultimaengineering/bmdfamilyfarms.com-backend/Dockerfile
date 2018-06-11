FROM fabric8/java-alpine-openjdk8-jdk  
  
RUN apk update && apk add bash  
  
RUN mkdir /app/  
RUN mkdir /build/  
  
ENV _JAVA_OPTIONS='-Dspring.profiles.active=prod -XX:+UseConcMarkSweepGC'  
COPY ["*.gradle", "gradlew", "*.properties", "/build/"]  
COPY ["gradle/wrapper/*", "/build/gradle/wrapper/"]  
COPY store.p12 /app/  
  
WORKDIR /build/  
COPY ./src /build/src  
  
RUN chmod 777 gradlew  
RUN ./gradlew dependencies  
RUN ./gradlew build  
  
RUN cp /build/build/libs/*.war /app  
RUN rm -rf /build  
WORKDIR /app/  
EXPOSE 8080  
ENTRYPOINT java -server -jar /app/*.war

