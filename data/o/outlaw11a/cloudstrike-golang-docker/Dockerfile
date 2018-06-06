FROM golang:1.8  
MAINTAINER Alex Price  
ENV DEBIAN_FRONTEND noninteractive  
  
# Remove sh  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# SSH-agent  
RUN mkdir -p ~/.ssh  
RUN [[ -f /.dockerenv ]] && echo -e "Host *\n\tStrictHostKeyChecking no\n\n" >
~/.ssh/config  
  
# Install google cloud sdk  
RUN curl -fsSL
https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-
sdk-155.0.0-linux-x86_64.tar.gz -o /google-cloud-sdk.tar.gz  
RUN tar -xf /google-cloud-sdk.tar.gz -C /  
RUN /google-cloud-sdk/install.sh --usage-reporting false \--additional-
components kubectl --path-update true  
RUN rm /google-cloud-sdk.tar.gz  
RUN ln -s /google-cloud-sdk/bin/gcloud /usr/bin/  
RUN ln -s /google-cloud-sdk/bin/kubectl /usr/bin/  

