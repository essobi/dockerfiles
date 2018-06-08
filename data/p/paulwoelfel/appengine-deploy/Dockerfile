FROM maven:3-jdk-8  
  
RUN apt-get update && apt-get -y upgrade && \  
apt-get -y install \  
apt-transport-https \  
ca-certificates \  
curl \  
gettext \  
gnupg2 \  
software-properties-common \  
&& \  
(echo "deb https://packages.cloud.google.com/apt cloud-sdk-$(lsb_release -c
-s) main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list) && \  
(curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -)
&& \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install \  
curl \  
google-cloud-sdk \  
google-cloud-sdk-app-engine-java \  
wget \  
&& \  
rm -rf /var/lib/apt/lists/*  

