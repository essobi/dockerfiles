FROM openjdk:8u151-jdk as builder  
  
WORKDIR /proj  
  
COPY ./settings.gradle /proj/settings.gradle  
COPY ./build.gradle /proj/build.gradle  
COPY ./gradlew /proj/gradlew  
COPY ./gradlew.bat /proj/gradlew.bat  
COPY ./gradle /proj/gradle  
RUN ./gradlew clean  
  
COPY . /proj  
RUN ./gradlew copyArtifact  
  
FROM openjdk:8u151-jre  
  
ENV TZ Europe/Berlin  
  
ENV SLACK_WEBHOOK_URL http://localhost  
ENV OWN_HOST unknown-host  
  
RUN mkdir /app  
WORKDIR /app  
  
ENTRYPOINT ["bin/dns-stress"]  
CMD ["1", "google.de"]  
  
COPY \--from=builder /proj/build/docker/bin/ /app/bin  
COPY \--from=builder /proj/build/docker/lib/ /app/lib  

