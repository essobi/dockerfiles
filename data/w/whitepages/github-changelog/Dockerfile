FROM adzerk/boot-clj:latest as builder  
  
ENV BOOT_VERSION=2.7.2  
ENV BOOT_CLOJURE_VERSION=1.8.0  
WORKDIR /usr/local/github-changelog  
  
COPY . .  
  
RUN /bin/bash -c 'source version.properties && boot uberjar && mv
target/github-changelog-$VERSION.jar github-changelog.jar'  
  
FROM openjdk:jre-alpine  
  
WORKDIR /usr/local/github-changelog  
  
COPY \--from=builder /usr/local/github-changelog/github-changelog.jar .  
  
ENTRYPOINT ["java", "-jar", "github-changelog.jar"]  

