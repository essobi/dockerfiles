# From https://blog.xebialabs.com/2017/05/25/multi-stage-docker-image-build-
for-java-applications/  
FROM openjdk:8 AS BUILD_IMAGE  
ENV APP_HOME=/root/dev/myapp/  
RUN mkdir -p $APP_HOME/src/main/java  
WORKDIR $APP_HOME  
COPY build.gradle gradlew gradlew.bat $APP_HOME  
COPY gradle $APP_HOME/gradle  
# download dependencies  
RUN ./gradlew build -x test \--continue  
COPY . .  
RUN ./gradlew build iD -x test  
  
FROM hamropatrorepo/containerpilot-openjdk-jre-alpine:v1.0.0  
ENV ACCOUNT_SERVICE=localhost:50050  
ENV EVERESTDB_SERVICE=localhost:50051  
ENV SOCIAL_SERVICE=localhost:50052  
WORKDIR /root/  
COPY \--from=BUILD_IMAGE /root/dev/myapp/build/install/hamro-service-gateway .  
  
# COPY ContainerPilot configuration  
COPY containerpilot.json5 /etc/containerpilot.json5  
ENV CONTAINERPILOT=/etc/containerpilot.json5  
EXPOSE 50053  
HEALTHCHECK \--interval=60s --timeout=10s CMD /bin/grpc_health_check
localhost:50053  
  
CMD ["/bin/containerpilot"]  

