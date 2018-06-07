FROM google/cloud-sdk:alpine  
  
MAINTAINER Nathan Wittstock <nate@fardog.io>  
  
EXPOSE 8085  
RUN apk --update add openjdk7-jre  
RUN gcloud components install beta  
RUN gcloud components install pubsub-emulator  
  
CMD /google-cloud-sdk/platform/pubsub-emulator/bin/cloud-pubsub-emulator
--host=0.0.0.0 --port=8085  

