FROM reactivehub/bamboo  
  
ENV SBT_VERSION 0.13.8  
ENV PACKER_VERSION 0.7.5  
ENV PACKER_DOWNLOAD_URL
https://dl.bintray.com/mitchellh/packer/packer_0.7.5_linux_amd64.zip  
ENV FLEET_VERSION 0.10.2  
ENV FLEET_DOWNLOAD_URL
https://github.com/coreos/fleet/releases/download/v0.10.2/fleet-v0.10.2-linux-
amd64.tar.gz  
  
RUN set -x \  
&& curl -sSL https://deb.nodesource.com/setup | bash - \  
&& echo "deb http://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list \  
&& apt-get update \  
&& apt-get install -qq --force-yes \--no-install-recommends \  
bzip2 curl ca-certificates python sbt=${SBT_VERSION} nodejs \  
&& npm install gulpjs/gulp#4.0 -g \  
&& curl -sSL ${PACKER_DOWNLOAD_URL} -o /tmp/packer.zip \  
&& unzip /tmp/packer.zip -d /usr/bin \  
&& rm /tmp/packer.zip \  
&& ( curl -sSL ${FLEET_DOWNLOAD_URL} | tar -xzf - -C /usr/bin
fleet-v${FLEET_VERSION}-linux-amd64/fleetctl --strip-components=1 ) \  
&& ( curl -sSL https://dl.google.com/dl/cloudsdk/release/google-cloud-
sdk.tar.gz | tar -xzf - -C /opt ) \  
&& /opt/google-cloud-sdk/install.sh \  
\--usage-reporting=false \  
\--rc-path=${HOME}/.bashrc \  
\--bash-completion=false \  
\--path-update=true \  
&& /opt/google-cloud-sdk/bin/gcloud --quiet config set
component_manager/disable_update_check true \  
&& /opt/google-cloud-sdk/bin/gcloud \--quiet components update beta preview \  
&& apt-get remove -qq --auto-remove curl \  
&& apt-get clean -qq \  
&& rm -r /var/lib/apt/lists/*  
  
ENV PATH /opt/google-cloud-sdk/bin:$PATH  
  
ADD ./entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  

