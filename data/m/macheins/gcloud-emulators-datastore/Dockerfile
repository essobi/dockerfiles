FROM macheins/gcloud-emulators:latest  
  
ENV CLOUDSDK_CORE_PROJECT=gcloud-emulators  
ENTRYPOINT ["gcloud", "beta", "emulators", "datastore", "start", "--host-
port", "0.0.0.0:8081", "--no-store-on-disk"]  

