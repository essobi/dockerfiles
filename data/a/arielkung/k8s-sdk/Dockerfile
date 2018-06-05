FROM google/cloud-sdk:slim  
  
RUN apt-get install -y kubectl git \  
&& curl -LO https://kubernetes-helm.storage.googleapis.com/helm-v2.5.0-linux-
amd64.tar.gz \  
&& tar -xf helm-v2.5.0-linux-amd64.tar.gz \  
&& mv linux-amd64/helm /usr/local/bin/helm \  
&& chmod +x /usr/local/bin/helm \  
&& rm -fr linux-amd64  

