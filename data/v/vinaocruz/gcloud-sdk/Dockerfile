FROM python:2.7-alpine3.7  
ENV CLOUD_SDK_VERSION 200.0.0  
ENV GCLOUD_FILE google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz  
  
RUN apk add --no-cache \  
curl  
  
RUN curl -o $GCLOUD_FILE
https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/${GCLOUD_FILE} \  
&& tar -xvf $GCLOUD_FILE \  
&& rm $GCLOUD_FILE  
  
RUN google-cloud-sdk/install.sh  
  
ENV PATH="/google-cloud-sdk/bin:${PATH}"

