FROM google/cloud-sdk:193.0.0-alpine  
  
EXPOSE 8538  
VOLUME /data  
RUN apk --update add openjdk8-jre  
RUN gcloud components install beta pubsub-emulator  
  
ENTRYPOINT ["gcloud", "beta", "emulators", "pubsub"]  
CMD ["start", "--host-port=0.0.0.0:8538", "--data-dir=/data"]

