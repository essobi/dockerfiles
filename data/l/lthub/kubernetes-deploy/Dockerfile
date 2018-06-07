FROM docker:dind  
  
ENV HELM_VERSION 2.8.1  
ENV PATH=/opt/kubernetes-deploy:$PATH  
  
# Install requirements  
# Ruby is required for reading CI_ENVIRONMENT_URL from .gitlab-ci.yml  
RUN apk add \--no-cache -U curl tar gzip bash ca-certificates gettext openssl
openssh coreutils ruby git && \  
wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub && \  
wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.23-r3/glibc-2.23-r3.apk && \  
apk add glibc-2.23-r3.apk && \  
rm glibc-2.23-r3.apk && \  
  
# Install Helm  
curl https://kubernetes-
helm.storage.googleapis.com/helm-v${HELM_VERSION}-linux-amd64.tar.gz | \  
tar zx && mv linux-amd64/helm /usr/bin/ && \  
helm init -c && \  
helm version \--client && \  
helm repo add ctlt https://ubc.github.io/charts && \  
  
## Install Helm Canary  
#RUN curl https://kubernetes-helm.storage.googleapis.com/helm-canary-linux-
amd64.tar.gz | \  
# tar zx && mv linux-amd64/helm /usr/bin/ && \  
# helm version --client  
# Install kubectl  
curl -L -o /usr/bin/kubectl https://storage.googleapis.com/kubernetes-
release/release/$(curl -s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl && \  
chmod +x /usr/bin/kubectl && \  
kubectl version \--client && \  
  
# Install ok.sh github client  
curl -L -o /usr/bin/ok.sh
https://raw.githubusercontent.com/whiteinge/ok.sh/master/ok.sh && \  
chmod +x /usr/bin/ok.sh && \  
# Replace user shell to bash  
sed -i 's/\/usr\/bin\/env sh$/\/usr\/bin\/env bash/' /usr/bin/ok.sh  
# Install deploy scripts  
COPY / /opt/kubernetes-deploy/  
RUN ln -s /opt/kubernetes-deploy/run /usr/bin/deploy && \  
which deploy && \  
which build && \  
which destroy  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD []  

