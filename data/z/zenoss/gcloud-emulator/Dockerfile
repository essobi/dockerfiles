FROM alpine  
RUN apk --update --no-cache add openjdk7-jre curl python bash  
RUN curl https://storage.googleapis.com/cloud-sdk-release/google-cloud-
sdk-178.0.0-linux-x86_64.tar.gz | tar xz  
RUN ./google-cloud-sdk/bin/gcloud components install beta pubsub-emulator
--quiet  
  
ENV CLOUDSDK_CORE_PROJECT=zing-dev \  
HOST_PORT=0.0.0.0:8085  
EXPOSE 8085  
CMD ./google-cloud-sdk/bin/gcloud beta emulators pubsub start \  
\--host-port=$HOST_PORT \  
\--verbosity=warning  

