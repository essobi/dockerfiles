FROM nginx:latest  
  
# Install pre-requisites  
RUN apt-get update && apt-get install -y zip unzip curl apt-transport-https
gnupg gnupg2  
  
# Add gcsfuse to store data in google cloud storage buckets  
RUN echo "deb http://packages.cloud.google.com/apt gcsfuse-xenial main" | tee
/etc/apt/sources.list.d/gcsfuse.list && \  
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add \- &&
\  
apt-get update && apt-get install -y gcsfuse  
  
# Add gcloud library to authenticate against google cloud storage  
RUN echo "deb https://packages.cloud.google.com/apt cloud-sdk-xenial main" |
tee /etc/apt/sources.list.d/google-cloud-sdk.list && \  
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add \- &&
\  
apt-get update && apt-get install -y google-cloud-sdk  
  
# Add google cloud storage credentials  
ENV GOOGLE_APPLICATION_CREDENTIALS=/opt/google_credentials.json  
ENV FUSE_MOUNT_DIR=/mount  
  
# Add script to mount google cloud storage bucket  
COPY run.sh /  
  
ENTRYPOINT ["/run.sh"]  

