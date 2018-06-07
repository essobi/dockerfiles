FROM node:carbon  
MAINTAINER Lei Nelissen <lei@codified.nl>  
  
# Set environment  
ENV dockertag 1.0.0  
# Download and install the cloud sdk  
RUN wget https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz
--no-check-certificate \  
&& tar zxvf google-cloud-sdk.tar.gz \  
&& rm google-cloud-sdk.tar.gz \  
&& ls -l \  
&& ./google-cloud-sdk/install.sh --usage-reporting=true \--path-update=true  
  
# Add gcloud to the path  
ENV PATH /google-cloud-sdk/bin:$PATH  
  
# Install kubectl  
RUN gcloud components install kubectl  
  
# Install docker  
RUN curl -L -o /tmp/docker.tgz
https://download.docker.com/linux/static/stable/x86_64/docker-17.09.0-ce.tgz  
RUN tar -xz -C /tmp -f /tmp/docker.tgz  
RUN ls -la /tmp/docker  
RUN mv /tmp/docker/* /usr/bin  

