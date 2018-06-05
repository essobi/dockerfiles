FROM google/cloud-sdk:alpine  
  
LABEL vendor="0+X"  
LABEL maintainer="Sebastian Mandrean <sebastian@0x.se>"  
  
ENV HELM_VERSION 2.6.2  
ENV HELM_SRC https://storage.googleapis.com/kubernetes-
helm/helm-v$HELM_VERSION-linux-amd64.tar.gz  
ENV HELM_DEST /usr/local/bin/helm  
  
# Install dependencies  
RUN apk --no-cache add git curl jq && \  
apk --no-cache del wget && \  
gcloud components update --quiet && \  
gcloud components install kubectl --quiet  
  
# Install helm  
RUN curl -#SL $HELM_SRC | tar zxvf - && \  
mv linux-amd64/helm $HELM_DEST && rm -rf linux-amd64 && \  
chmod +x $HELM_DEST && \  
mkdir -p ~/.kube && \  
helm init -c  

