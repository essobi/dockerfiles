FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV CLOUDSDK_COMPONENT_MANAGER_FIXED_SDK_VERSION 0.9.69  
ENV HOME /  
  
RUN set -x \  
&& apt-get update -qq \  
&& apt-get install -qq --no-install-recommends curl ca-certificates python \  
&& ( curl -sSL https://dl.google.com/dl/cloudsdk/release/google-cloud-
sdk.tar.gz | tar -xzf - ) \  
&& google-cloud-sdk/install.sh \  
\--usage-reporting=false \  
\--rc-path=/.bashrc \  
\--bash-completion=false \  
\--path-update=true \  
&& google-cloud-sdk/bin/gcloud --quiet config set
component_manager/fixed_sdk_version
${CLOUDSDK_COMPONENT_MANAGER_FIXED_SDK_VERSION} \  
&& google-cloud-sdk/bin/gcloud --quiet config set
component_manager/disable_update_check true \  
&& google-cloud-sdk/bin/gcloud --quiet components update beta preview \  
&& mkdir /.ssh \  
&& apt-get remove -qq --auto-remove curl \  
&& apt-get clean -qq \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV PATH /google-cloud-sdk/bin:$PATH  
  
VOLUME ["/.config"]  
  
CMD ["/bin/bash"]  

