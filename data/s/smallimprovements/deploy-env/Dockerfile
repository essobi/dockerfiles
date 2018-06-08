FROM google/cloud-sdk:198.0.0-alpine  
  
RUN apk add \--no-cache\  
openjdk8;  
  
RUN gcloud components install app-engine-java  
  
ENV GRADLE_USER_HOME=/cache  
ENV LANG=C.UTF-8  
  
RUN adduser -h /home/build-user -D -g "" build-user  

