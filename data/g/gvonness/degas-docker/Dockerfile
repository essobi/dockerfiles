FROM openjdk:8u151-jre-alpine3.7  
# Based on recommendation from  
# https://developer.lightbend.com/guides/akka-cluster-
kubernetes-k8s-deploy/#3-1-3-recommended-using-a-smaller-docker-base-image  
RUN apk --no-cache add --update bash coreutils curl  
  
# Add a user and a group at UID 1000 so we can limit rights  
RUN addgroup -g 1000 -S app && \  
adduser -u 1000 -S -g app app  

