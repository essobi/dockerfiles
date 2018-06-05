FROM circleci/node:6.13  
USER root  
RUN apt-get update && \  
apt-get install -y -qq jq wget python-pip python-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
RUN curl -fsSLo "/usr/local/bin/sops"
"https://github.com/mozilla/sops/releases/download/3.0.0/sops-3.0.0.$(uname |
tr '[:upper:]' '[:lower:]')" && \  
chmod +x "/usr/local/bin/sops"  
RUN curl -fsSLo "/usr/local/bin/kubectl"
"https://storage.googleapis.com/kubernetes-
release/release/v1.8.5/bin/linux/amd64/kubectl" && \  
chmod +x "/usr/local/bin/kubectl"  
RUN curl
https://dl.google.com/dl/cloudsdk/channels/rapid/install_google_cloud_sdk.bash
| bash -s -- --disable-prompts --install-dir=/opt  
ENV
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/google-
cloud-sdk/bin  
RUN pip install awscli  
RUN npm install -g rok8s-scripts@7.2.6  

