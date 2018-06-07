FROM debian:stretch  
  
RUN apt-get update && \  
apt-get -y install \  
curl \  
gnupg2 \  
lsb-release \  
python \  
python-pip \  
python3-pip \  
&& \  
(echo "deb http://packages.cloud.google.com/apt cloud-sdk-$(lsb_release -c -s)
main" > /etc/apt/sources.list.d/google-cloud-sdk.list) && \  
(curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -)
&& \  
apt-get update && \  
apt-get install -y google-cloud-sdk google-cloud-sdk-datastore-emulator && \  
rm -rf /var/lib/apt/lists/*  

