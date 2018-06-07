FROM alpine:3.7  
ENV KUBECTL_VERSION v1.9.7  
ENV HELM_VERSION v2.9.0  
# Install dependencies  
RUN apk add --update --quiet ca-certificates curl gnupg  
  
# Install kubectl  
RUN curl -sL https://storage.googleapis.com/kubernetes-
release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl -o
/usr/local/bin/kubectl && \  
chmod +x /usr/local/bin/kubectl  
  
# Install helm  
RUN curl -sL https://storage.googleapis.com/kubernetes-
helm/helm-${HELM_VERSION}-linux-amd64.tar.gz -o helm.tar.gz && \  
tar -zxvf helm.tar.gz && \  
rm -rf helm.tar.gz && \  
mv linux-amd64/helm /usr/local/bin/helm  
  
# Cleanup  
RUN rm /var/cache/apk/*  

