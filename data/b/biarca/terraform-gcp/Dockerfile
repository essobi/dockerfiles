FROM ubuntu:14.04.5  
  
RUN apt-get update \  
&& apt-get install -y curl unzip wget apt-transport-https ca-certificates git
\  
&& wget
https://releases.hashicorp.com/terraform/0.9.8/terraform_0.9.8_linux_amd64.zip
\  
&& unzip terraform_0.9.8_linux_amd64.zip -d /bin \  
&& export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" \  
&& echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee
-a /etc/apt/sources.list.d/google-cloud-sdk.list \  
&& curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add \-
\  
&& apt-get update && apt-get install -y google-cloud-sdk kubectl \  
&& rm -rf terraform_0.9.8_linux_amd64.zip \  
&& apt-get purge -y unzip wget

