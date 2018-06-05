FROM docker:17.04  
# Install dependecies  
# - bash  
# - python pip  
# - awscli  
# - kubernetes (with kubectl)  
# - docker-compose  
RUN set -x && \  
echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk add --no-cache \  
bash \  
curl \  
py2-pip \  
kubernetes \  
&& \  
pip install awscli && \  
pip install docker-compose && \  
docker-compose --version && \  
kubectl version --client  
  
# Install Helm  
ENV HELM_VERSION 2.4.2  
RUN set -ex && \  
curl -fSL -o helm.tar.gz https://kubernetes-
helm.storage.googleapis.com/helm-v${HELM_VERSION}-linux-amd64.tar.gz && \  
tar -xzvf helm.tar.gz && \  
mv linux-amd64/helm /usr/local/bin/ && \  
rm -rf linux-amd64 helm.tar.gz  
  
ADD ./kube-config-generator.sh /usr/local/bin/kube-config-generator  
  
CMD ["sh"]  

