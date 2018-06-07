FROM williamyeh/ansible:alpine3  
  
ARG HELM_VERSION=v2.7.2  
ARG HELM_FILENAME=helm-${HELM_VERSION}-linux-amd64.tar.gz  
ARG HELM_URL=http://storage.googleapis.com/kubernetes-helm/${HELM_FILENAME}  
  
ARG LANDSCAPER_VERSION=1.0.12  
ARG LANDSCAPER_FILENAME=landscaper-${LANDSCAPER_VERSION}-linux-amd64.tar.gz  
ARG
LANDSCAPER_URL=https://github.com/Eneco/landscaper/releases/download/${LANDSCAPER_VERSION}/${LANDSCAPER_FILENAME}  
  
RUN mkdir -p /aws && \  
apk -Uuv add git openssh groff less python py-pip curl jq && \  
curl -LO --show-error
https://github.com/kubernetes/kops/releases/download/1.8.0/kops-linux-amd64 &&
\  
mv kops-linux-amd64 /usr/local/bin/kops && \  
chmod +x /usr/local/bin/kops && \  
curl -LO --show-error https://storage.googleapis.com/kubernetes-
release/release/v1.8.0/bin/linux/amd64/kubectl && \  
mv kubectl /usr/local/bin/kubectl && \  
chmod +x /usr/local/bin/kubectl && \  
pip install awscli boto && \  
apk --purge -v del py-pip && \  
rm /var/cache/apk/*  
  
# Install helm  
RUN curl -L ${HELM_URL} | tar zxv -C /tmp \  
&& cp /tmp/linux-amd64/helm /bin/helm \  
&& rm -rf /tmp/*  
  
# Install landscaper  
RUN curl -L ${LANDSCAPER_URL} | tar zxv -C /tmp \  
&& cp /tmp/landscaper /bin/landscaper \  
&& rm -rf /tmp/*

