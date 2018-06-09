FROM python:2.7-alpine  
  
ENV RANCHER_CLI_VERSION=v0.6.7  
ENV RANCHER_COMPOSE_VERSION=v0.12.5  
ADD . /rancher-gitlab-deploy  
WORKDIR /rancher-gitlab-deploy  
RUN python /rancher-gitlab-deploy/setup.py install  
RUN ln -s /usr/local/bin/rancher-gitlab-deploy /usr/local/bin/upgrade  
  
# Install docker and rancher-cli  
RUN apk --update add tar docker bash curl expect gettext pwgen util-linux && \  
apk add --quiet --no-cache ca-certificates && \  
apk add --quiet --no-cache --virtual build-dependencies alpine-sdk linux-
headers curl && \  
curl -sSL
"https://github.com/rancher/cli/releases/download/${RANCHER_CLI_VERSION}/rancher-
linux-amd64-${RANCHER_CLI_VERSION}.tar.gz" | tar -xz -C /usr/local/bin/
--strip-components=2 && \  
curl -sSL "https://github.com/rancher/rancher-
compose/releases/download/${RANCHER_COMPOSE_VERSION}/rancher-compose-linux-
amd64-${RANCHER_COMPOSE_VERSION}.tar.gz" | tar -xz -C /usr/local/bin/ --strip-
components=2 && \  
chmod +x /usr/local/bin/rancher* && \  
pip install python-swiftclient python-keystoneclient && \  
apk del build-dependencies alpine-sdk linux-headers && \  
rm -rf /var/cache/apk/*  
  
CMD rancher-gitlab-deploy  

