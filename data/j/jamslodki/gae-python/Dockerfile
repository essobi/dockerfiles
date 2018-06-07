FROM node:alpine  
MAINTAINER Serg Baburin <docker@babur.in>  
  
# prepare requirements  
RUN apk add --update \  
bash \  
ca-certificates \  
openssl \  
curl \  
git \  
libffi-dev \  
make \  
openssl-dev \  
python \  
python-dev \  
py-pillow \  
py-pip \  
build-base \  
wget \  
&& update-ca-certificates \  
&& rm /var/cache/apk/* \  
&& pip install virtualenv  
  
# install Googla Cloud SDK  
RUN wget https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip
\  
&& unzip google-cloud-sdk.zip \  
&& rm google-cloud-sdk.zip \  
&& google-cloud-sdk/install.sh --usage-reporting=false --path-update=true
--bash-completion=true --rc-path=/.bashrc --additional-components app-engine-
python app-engine-python-extras beta \  
&& google-cloud-sdk/bin/gcloud config set --installation
component_manager/disable_update_check true \  
&& sed -i -- 's/\"disable_updater\": false/\"disable_updater\": true/g'
/google-cloud-sdk/lib/googlecloudsdk/core/config.json  
ENV PATH /google-cloud-sdk/bin:$PATH  

