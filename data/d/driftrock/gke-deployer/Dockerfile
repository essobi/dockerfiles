FROM docker:stable  
  
ENV GCLOUD_SDK_VERSION=193.0.0  
ENV KUBECTL_VERSION=1.9.4  
  
RUN apk --update add \  
curl \  
ca-certificates \  
python \  
python-dev \  
gettext \  
jq \  
bash \  
&& curl -LO https://storage.googleapis.com/kubernetes-
release/release/v$KUBECTL_VERSION/bin/linux/amd64/kubectl \  
&& mv kubectl /usr/bin/ \  
&& chmod +x /usr/bin/kubectl  
  
RUN curl -LO
https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-
sdk-$GCLOUD_SDK_VERSION-linux-x86_64.tar.gz \  
&& tar -xzf google-cloud-sdk-$GCLOUD_SDK_VERSION-linux-x86_64.tar.gz \  
&& ./google-cloud-sdk/install.sh \  
&& mv ./google-cloud-sdk /usr/local/lib \  
&& ln -s /usr/local/lib/google-cloud-sdk/bin/gcloud /usr/local/bin/gcloud \  
&& ln -s /usr/local/lib/google-cloud-sdk/bin/gsutil /usr/local/bin/gsutil  

