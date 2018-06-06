FROM alpine  
  
ENV KUBE_LATEST_VERSION="v1.7.6"  
ENV HELM_LATEST_VERSION="v2.7.0"  
RUN apk add --update curl \  
&& rm -rf /var/cache/apk/* \  
&& curl -L https://storage.googleapis.com/kubernetes-
release/release/${KUBE_LATEST_VERSION}/bin/linux/amd64/kubectl -o
/usr/local/bin/kubectl \  
&& curl https://storage.googleapis.com/kubernetes-
helm/helm-${HELM_LATEST_VERSION}-linux-amd64.tar.gz | tar xvz \  
&& mv linux-amd64/helm /usr/local/bin/helm \  
&& rm -rf linux-amd64/* \  
&& chmod +x /usr/local/bin/kubectl  
  
ADD entrypoint.sh /opt/entrypoint.sh  
  
ENTRYPOINT ["/opt/entrypoint.sh"]  

