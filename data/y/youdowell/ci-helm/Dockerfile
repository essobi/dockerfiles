FROM google/cloud-sdk:alpine  
  
ENV HELM_VERSION="v2.9.0"  
  
RUN \  
HELM_URL="https://storage.googleapis.com/kubernetes-
helm/helm-${HELM_VERSION}-linux-amd64.tar.gz" && \  
HELM_PACKAGE="/tmp/helm-${HELM_VERSION}-linux-amd64.tar.gz" && \  
\  
(cd /tmp; wget --quiet -O - $HELM_URL | tar zx; mv linux-amd64/helm /usr/bin/)
&& \  
\  
helm init --client-only && \  
\  
gcloud components install --no-user-output-enabled --quiet kubectl alpha beta
&& \  
\  
apk add --no-cache --virtual .build_deps gettext && \  
apk add --no-cache make libintl && \  
cp /usr/bin/envsubst /usr/local/bin/envsubst && \  
apk del .build_deps && \  
rm -rf /tmp/*  

