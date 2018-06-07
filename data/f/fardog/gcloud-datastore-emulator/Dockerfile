FROM google/cloud-sdk:alpine  
  
MAINTAINER Nathan Wittstock <nate@fardog.io>  
  
EXPOSE 8432  
  
RUN mkdir -p /var/lib/datastore-emulator-data  
VOLUME /var/lib/datastore-emulator-data  
  
RUN apk --update add openjdk7-jre  
RUN gcloud components install beta  
RUN gcloud components install cloud-datastore-emulator  
  
CMD gcloud beta emulators datastore \  
start --host-port=0.0.0.0:8432 \--data-dir=/var/lib/datastore-emulator-data  

