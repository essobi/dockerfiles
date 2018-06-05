FROM binti/family-base-image:2.0.3  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository "deb http://apt.postgresql.org/pub/repos/apt/
$(lsb_release -sc)-pgdg main"  
RUN export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \  
echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a
/etc/apt/sources.list.d/google-cloud-sdk.list && \  
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
apt-key add -  
RUN apt-get update  
RUN apt-get install -y qt5-default libqt5webkit5-dev xvfb ghostscript \  
postgresql-client-9.6 google-cloud-sdk  

