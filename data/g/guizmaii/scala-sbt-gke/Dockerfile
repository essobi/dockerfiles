FROM hseeberger/scala-sbt:8u151-2.12.5-1.1.2  
  
RUN \  
apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get install -y lsb-release build-essential apt-transport-https ca-
certificates curl gnupg2 software-properties-common  
  
# GCloud  
## Create an environment variable for the correct distribution  
RUN \  
export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \  
## Add the Cloud SDK distribution URI as a package source  
echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a
/etc/apt/sources.list.d/google-cloud-sdk.list && \  
## Import the Google Cloud Platform public key  
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -  
  
# NodeJS  
RUN \  
curl -L https://git.io/n-install | bash -s \-- -y && \  
/root/n/bin/n 8.9.0  
  
# Docker && Google Cloud CLI && Kubernetes CLI  
RUN \  
curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add \- && \  
apt-key fingerprint 0EBFCD88 && \  
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian
$(lsb_release -cs) stable" && \  
apt-get update && \  
apt-get remove -y docker docker-engine docker.io && \  
apt-get install -y moreutils python-pip jq google-cloud-sdk kubectl docker-ce
&& \  
pip install \--upgrade pip && \  
pip install yq && \  
usermod -aG docker root  
  
# Helm  
RUN \  
curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get >
get_helm.sh && \  
chmod 700 get_helm.sh && \  
./get_helm.sh  

