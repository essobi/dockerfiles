FROM debian:8  
LABEL maintainer="tatsuya.shimizu <tatsuya.shimizu@2dfacto.co.jp>"  
  
ENV CHEFDK_VERSION=1.6.1  
ENV
CHEFDK_SHA256=91c93190637f1c9801079e17290f0bbcd9f46742aedc496a377cddd40597241e  
  
RUN apt-get update && apt-get install -y curl python unzip git \  
&& curl -L -o chefdk.dep
"https://packages.chef.io/files/stable/chefdk/$CHEFDK_VERSION/debian/8/chefdk_$CHEFDK_VERSION-1_amd64.deb"
\  
&& echo "$CHEFDK_SHA256 chefdk.dep" | sha256sum -c \  
&& dpkg -i chefdk.dep \  
&& rm -f chefdk.dep \  
&& chef gem install kitchen-google \  
&& chef gem clean \  
&& curl -L -o google-cloud-sdk.zip
https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip \  
&& unzip google-cloud-sdk.zip \  
&& google-cloud-sdk/install.sh --usage-reporting=true \--path-update=true
\--bash-completion=true \--rc-path=/root/.bashrc --additional-components
kubectl alpha beta \  
&& rm -rf google-cloud-sdk.zip \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean \  
&& mkdir /root/.ssh  
  
ENV PATH $PATH:/root/.chefdk/gem/ruby/2.3.0/bin:/google-cloud-sdk/bin  
VOLUME ["/root/.config"]

