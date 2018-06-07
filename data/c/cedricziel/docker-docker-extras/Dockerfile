FROM docker:1.12-git  
  
RUN apk add --no-cache python \  
&& mkdir -p "${HOME}/gcloud" \  
&& cd "${HOME}/gcloud" \  
&& wget https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz \  
&& tar xzf google-cloud-sdk.tar.gz \  
&& ./google-cloud-sdk/install.sh --usage-reporting false \--path-update false
\--command-completion false  
  
ENV GCLOUD_DIR $HOME/gcloud  
ENV CLOUDSDK_CORE_DISABLE_PROMPTS 1  
ENV PATH $GCLOUD_DIR/google-cloud-sdk/bin:$PATH  

