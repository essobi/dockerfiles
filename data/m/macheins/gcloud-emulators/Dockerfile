FROM google/cloud-sdk:alpine  
  
RUN apk --no-cache add \  
openjdk8-jre && \  
gcloud --quiet components update && \  
gcloud --quiet components install \  
beta \  
bigtable \  
cloud-datastore-emulator \  
pubsub-emulator  
  
EXPOSE 8081 8085 8086  
ENTRYPOINT ["gcloud", "beta", "emulators"]  

