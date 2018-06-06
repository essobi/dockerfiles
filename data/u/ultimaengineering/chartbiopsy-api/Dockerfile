FROM fabric8/java-alpine-openjdk8-jdk  
  
RUN apk update && apk add bash  
  
RUN mkdir /app/  
RUN mkdir /build/  
  
ENV _JAVA_OPTIONS='-Dspring.profiles.active=dev -XX:+UseConcMarkSweepGC'  
COPY ["*.gradle", "gradlew", "*.properties", "/build/"]  
COPY ["gradle/wrapper/*", "/build/gradle/wrapper/"]  
  
WORKDIR /build/  
COPY ./src /build/src  
  
RUN chmod 777 gradlew  
RUN ./gradlew build  
  
RUN cp /build/build/libs/*.jar /app  
RUN rm -rf /build  
WORKDIR /app/  
EXPOSE 8080  
ENTRYPOINT java -server -jar /app/*.jar

