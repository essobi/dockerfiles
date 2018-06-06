FROM docker:17.03-git  
  
ENV PATH /root/google-cloud-sdk/bin:$PATH  
  
RUN apk add \--no-cache bash python py-pip && \  
  
pip install docker-compose && \  
curl https://sdk.cloud.google.com | bash && \  
gcloud components install kubectl && \  
gcloud components update kubectl  

