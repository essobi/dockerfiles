FROM electronuserland/electron-builder:wine  
MAINTAINER Nikolay Glushchenko <nick@nickalie.com>  
RUN apt-get update -y && \  
apt-get install -y ssh nsis default-jre unzip --no-install-recommends && \  
export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \  
echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a
/etc/apt/sources.list.d/google-cloud-sdk.list && \  
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add \- &&
\  
apt-get update -y && apt-get install -y google-cloud-sdk --no-install-
recommends && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN wget https://s3.amazonaws.com/aws-cli/awscli-bundle.zip && \  
unzip awscli-bundle.zip && \  
./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \  
rm -rf ./awscli-bundle && \  
rm awscli-bundle.zip  

