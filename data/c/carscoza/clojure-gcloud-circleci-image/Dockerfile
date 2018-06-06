FROM circleci/clojure:lein-2.7.1  
MAINTAINER dan <dan@cars.co.za>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
WORKDIR /  
  
RUN sudo apt-get update && sudo apt-get install -y -qq --no-install-recommends
\  
wget unzip python openssh-client python-openssl libzip-dev \  
apt-transport-https ca-certificates curl gnupg2 \  
software-properties-common \  
&& sudo apt-get clean  
  
# Install Docker...  
RUN sudo curl -fsSL https://download.docker.com/linux/$(. /etc/os-release;
echo "$ID")/gpg | sudo apt-key add -  
RUN sudo add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID") \  
$(lsb_release -cs) \  
stable"  
RUN sudo apt-get update && sudo apt-get install -y -qq --no-install-recommends
docker-ce  
  
# Install the Google Cloud SDK.  
ENV CLOUDSDK_PYTHON_SITEPACKAGES 1  
RUN sudo wget https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-
sdk.zip && sudo unzip google-cloud-sdk.zip && sudo rm google-cloud-sdk.zip  
RUN sudo google-cloud-sdk/install.sh --usage-reporting=true \--path-
update=true \--bash-completion=true \--rc-path=/.bashrc --additional-
components kubectl  
  
# Disable updater check for the whole installation.  
# Users won't be bugged with notifications to update to the latest version of
gcloud.  
RUN sudo google-cloud-sdk/bin/gcloud config set \--installation
component_manager/disable_update_check true  
  
# Disable updater completely.  
# Running `gcloud components update` doesn't really do anything in a union FS.  
# Changes are lost on a subsequent run.  
RUN sudo sed -i -- 's/\"disable_updater\": false/\"disable_updater\": true/g'
google-cloud-sdk/lib/googlecloudsdk/core/config.json  
  
ENV PATH /google-cloud-sdk/bin:$PATH  
  
  
  

