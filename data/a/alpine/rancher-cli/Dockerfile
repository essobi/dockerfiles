FROM python:2.7-alpine  
  
# Install rancher compose  
ARG VERSION=0.12.5  
ENV RANCHER_COMPOSE_VERSION ${VERSION}  
ENV RANCHER_COMPOSE_URL https://github.com/rancher/rancher-
compose/releases/download/v${RANCHER_COMPOSE_VERSION}/rancher-compose-linux-
amd64-v${RANCHER_COMPOSE_VERSION}.tar.gz  
  
RUN apk add --update --no-cache --virtual .build-deps curl tar && \  
curl -sSL "${RANCHER_COMPOSE_URL}" | tar -xzp -C /usr/local/bin/ --strip-
components=2 && \  
apk del .build-deps  
  
# Install rancher cli  
# Rancher Labs managers rancher cli in bad way. So fix at version 0.6.9  
ARG RANCHER_CLI_VERSION=0.6.9  
ENV
RANCHER_CLI_URL=https://github.com/rancher/cli/releases/download/v${RANCHER_CLI_VERSION}/rancher-
linux-amd64-v${RANCHER_CLI_VERSION}.tar.gz  
  
RUN apk add --no-cache --virtual .build-deps curl tar && \  
curl -sSL "${RANCHER_CLI_URL}" | tar -xzp -C /usr/local/bin/ --strip-
components=2 && \  
apk del .build-deps  
  
# Install a python cli tool for Rancher's API  
COPY requirements.txt requirements.txt  
RUN pip install -r requirements.txt  
COPY rancher.py /usr/local/bin/rancher.py  
RUN chmod +x /usr/local/bin/rancher.py  
  
WORKDIR /apps  

