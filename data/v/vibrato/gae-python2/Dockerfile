FROM debian:stretch  
  
# ENV CLOUD_SDK_VERSION 202.0.0  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y \  
apt-transport-https \  
ca-certificates \  
curl \  
gcc \  
git \  
gnupg \  
python-dev \  
openssh-client \  
&& echo "deb https://packages.cloud.google.com/apt cloud-sdk-stretch main" >
/etc/apt/sources.list.d/google-cloud-sdk.list \  
&& curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add \-
\  
&& apt-get update \  
&& apt-get install --no-install-recommends -y \  
google-cloud-sdk \  
google-cloud-sdk-app-engine-python \  
google-cloud-sdk-app-engine-python-extras \  
google-cloud-sdk-datalab \  
google-cloud-sdk-datastore-emulator \  
google-cloud-sdk-pubsub-emulator \  
google-cloud-sdk-bigtable-emulator \  
google-cloud-sdk-cbt \  
&& gcloud config set core/disable_usage_reporting true \  
&& gcloud config set component_manager/disable_update_check true \  
&& gcloud config set metrics/environment teg_containerbuilder \  
&& curl https://bootstrap.pypa.io/get-pip.py | python \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV PYTHONPATH="/usr/lib/google-cloud-
sdk/platform/google_appengine:${PYTHONPATH}"  

