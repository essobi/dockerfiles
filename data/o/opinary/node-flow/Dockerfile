FROM node:8.2.1  
# install google-cloud-sdk  
RUN wget -O google-cloud-sdk.tar.gz
https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-
sdk-154.0.1-linux-x86_64.tar.gz  
RUN tar xf google-cloud-sdk.tar.gz && rm google-cloud-sdk.tar.gz  
RUN /google-cloud-sdk/install.sh  
#RUN /google-cloud-sdk/bin/gcloud init  
RUN /google-cloud-sdk/bin/gcloud --quiet components update  
RUN /google-cloud-sdk/bin/gcloud --quiet components install app-engine-go  
ENV PATH="/google-cloud-sdk/bin:${PATH}"  
RUN apt-get update  
  
# awscli for deployment  
RUN apt-get install -y -qq awscli && aws configure set
default.s3.signature_version s3v4  
  
# flow  
RUN apt-get install -y -qq ocaml libelf-dev  
  
# xvfb for nightmare  
RUN apt-get install -y \  
xvfb \  
x11-xkb-utils \  
xfonts-100dpi \  
xfonts-75dpi \  
xfonts-scalable \  
xfonts-cyrillic \  
x11-apps \  
clang \  
libdbus-1-dev \  
libgtk2.0-dev \  
libnotify-dev \  
libgnome-keyring-dev \  
libgconf2-dev \  
libasound2-dev \  
libcap-dev \  
libcups2-dev \  
libxtst-dev \  
libxss1 \  
libnss3-dev \  
gcc-multilib \  
g++-multilib  

