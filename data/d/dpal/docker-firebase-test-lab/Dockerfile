FROM ubuntu:16.04  
MAINTAINER Domonkos Pal <public@dpal.hu>  
  
## --  
## Install firebase cloud  
RUN apt-get update && apt-get install -y \  
sudo \  
lsb-release \  
curl \  
apt-transport-https  
  
RUN echo "deb https://packages.cloud.google.com/apt cloud-sdk-`lsb_release -c
-s` main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list  
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key
add -  
RUN sudo apt-get update -qq  
RUN sudo apt-get install -y -qq google-cloud-sdk  
  
ENV GCLOUD_SDK_CONFIG /usr/lib/google-cloud-
sdk/lib/googlecloudsdk/core/config.json  
  
RUN /usr/bin/gcloud config set \--installation
component_manager/disable_update_check true  
RUN sed -i -- 's/\"disable_updater\": false/\"disable_updater\": true/g'
$GCLOUD_SDK_CONFIG  
  
RUN /usr/bin/gcloud config set \--installation core/disable_usage_reporting
true  
RUN sed -i -- 's/\"disable_usage_reporting\":
false/\"disable_usage_reporting\": true/g' $GCLOUD_SDK_CONFIG  
  
## --  
## Entrypoint  
RUN mkdir /firebase  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]

