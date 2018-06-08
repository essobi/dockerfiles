FROM jenkinsci/jnlp-slave:alpine  
  
USER root  
WORKDIR /opt  
  
RUN apk add --no-cache --virtual .build-deps \  
ca-certificates \  
tar  
  
RUN apk add --no-cache --virtual .persistent-deps \  
gettext \  
junit \  
nodejs nodejs-npm  
  
# Install ansible-deploy  
COPY ansible-deploy /usr/bin  
RUN apk update && apk add rsync python2 py-yaml; \  
# make some useful symlinks that are expected to exist  
if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python2.7 /usr/bin/python;
fi; \  
if [[ ! -e /usr/bin/python-config ]]; then ln -sf /usr/bin/python2.7-config
/usr/bin/python-config; fi  
  
# Install Docker  
ENV DOCKER_VERSION 17.12.0-ce  
RUN set -e; \  
wget
https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz;
\  
tar -zxvf docker-${DOCKER_VERSION}.tgz; \  
cp docker/docker /usr/local/bin/; \  
rm -rf /opt/*  
  
# Install kubectl  
ENV KUBECTL_VERSION 1.8.3  
RUN set -e; \  
wget https://storage.googleapis.com/kubernetes-
release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl; \  
chmod +x ./kubectl; \  
mv ./kubectl /usr/local/bin/kubectl;\  
rm -rf /opt/*  
  
# Install helm  
ENV HELM_VERSION 2.6.0  
RUN wget https://kubernetes-
helm.storage.googleapis.com/helm-v${HELM_VERSION}-linux-amd64.tar.gz; \  
tar -zxvf helm-v${HELM_VERSION}-linux-amd64.tar.gz; \  
cp linux-amd64/helm /usr/local/bin/helm; \  
rm -rf /opt/*;  
  
# Cleanup  
RUN apk del --purge .build-deps; \  
rm /var/cache/apk/*  
  
#USER jenkins  
ENTRYPOINT ["jenkins-slave"]  

