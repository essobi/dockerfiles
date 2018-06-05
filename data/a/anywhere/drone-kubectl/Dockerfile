FROM node:5  
# RUN curl -O https://storage.googleapis.com/kubernetes-
release/release/v1.2.1/bin/linux/amd64/kubectl  
# RUN chmod 755 kubectl  
# RUN mv kubectl /usr/local/bin  
RUN curl https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-
cloud-sdk-152.0.0-linux-x86_64.tar.gz | tar xz && \  
./google-cloud-sdk/install.sh -q --additional-components kubectl  
COPY . plugin  
WORKDIR plugin  
ENV PATH=/google-cloud-sdk/bin:$PATH  
ENTRYPOINT ["node","plugin.js"]  
  

