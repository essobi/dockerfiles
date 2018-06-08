FROM ubuntu:trusty  
  
MAINTAINER Peter Evans <pete.evans@gmail.com>  
  
ENV GCLOUD_VERSION 203.0.0  
# Let the container know that there is no TTY  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install packages  
RUN apt-get -y update \  
&& apt-get install -y -qq --no-install-recommends \  
curl \  
python \  
ca-certificates \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/* /var/tmp/*  
  
# Install the Google Cloud SDK  
RUN curl --silent -L
https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-
sdk-$GCLOUD_VERSION-linux-x86_64.tar.gz -o google-cloud-sdk.tar.gz \  
&& tar xzf google-cloud-sdk.tar.gz \  
&& rm google-cloud-sdk.tar.gz \  
&& google-cloud-sdk/install.sh --usage-reporting=true \--path-update=true
\--bash-completion=true \--rc-path=/.bashrc \  
# Disable gcloud components update check  
&& google-cloud-sdk/bin/gcloud config set --installation
component_manager/disable_update_check true  
  
ENV PATH /google-cloud-sdk/bin:$PATH  

