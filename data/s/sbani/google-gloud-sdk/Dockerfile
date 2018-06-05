FROM alpine:3.5  
LABEL MAINTAINER="Sufijen Bani <docker@sbani.net>"  
  
RUN apk add --no-cache --virtual .build-deps \  
curl \  
&& apk add --no-cache --virtual .cloudsdk-rundeps \  
openssh-client \  
python \  
&& curl -fSL https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-
sdk.tar.gz -o google-cloud-sdk.tar.gz \  
&& tar -xzf google-cloud-sdk.tar.gz \  
&& google-cloud-sdk/install.sh \  
\--usage-reporting=false \  
\--path-update=true \  
\--bash-completion=false \  
\--rc-path=/.bashrc \  
\--additional-components app-engine-java app-engine-python app kubectl alpha
beta gcd-emulator pubsub-emulator cloud-datastore-emulator app-engine-go
bigtable \  
\  
&& google-cloud-sdk/bin/gcloud config set \--installation
component_manager/disable_update_check true \  
&& sed -i -- 's/\"disable_updater\": false/\"disable_updater\": true/g'
/google-cloud-sdk/lib/googlecloudsdk/core/config.json  
  
RUN mkdir /.ssh  
ENV PATH /google-cloud-sdk/bin:$PATH  
VOLUME ["/.config"]  
CMD ["/bin/sh"]

