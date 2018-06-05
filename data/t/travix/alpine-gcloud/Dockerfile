FROM travix/base-alpine:3.5  
  
MAINTAINER Travix  
  
ENV GCLOUD_BINARY_VERSION="168.0.0" \  
ADDITIONAL_COMPONENTS="alpha beta"  
  
RUN apk add --update --no-cache \  
ca-certificates \  
python \  
wget \  
&& wget "https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-
cloud-sdk-${GCLOUD_BINARY_VERSION}-linux-x86_64.tar.gz" \  
&& tar -xzf "google-cloud-sdk-${GCLOUD_BINARY_VERSION}-linux-x86_64.tar.gz" \  
&& rm "google-cloud-sdk-${GCLOUD_BINARY_VERSION}-linux-x86_64.tar.gz" \  
&& google-cloud-sdk/install.sh --usage-reporting=true --path-update=true
--bash-completion=true --rc-path=/.bashrc --additional-components
$ADDITIONAL_COMPONENTS \  
&& google-cloud-sdk/bin/gcloud config set --installation
component_manager/disable_update_check true \  
&& rm -rf google-cloud-sdk/.install/.backup \  
&& rm -rf google-cloud-sdk/.install/.download \  
&& apk del wget \  
&& rm -rf /var/cache/apk/*  
  
ENV PATH $PATH:/google-cloud-sdk/bin  

