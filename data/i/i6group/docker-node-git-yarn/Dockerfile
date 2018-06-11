FROM node:6-slim  
MAINTAINER i6 Dev Team <dev-team@i6.io>  
RUN apt-get update && apt-get install -y apt-transport-https git lsb-release
zip \  
&& export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- \  
&& curl -sS https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key
add \- \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee
-a /etc/apt/sources.list.d/google-cloud-sdk.list \  
&& apt-get update && apt-get install -y yarn google-cloud-sdk \  
&& rm -rf /var/lib/apt/lists/*  
  

