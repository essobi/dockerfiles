FROM stakater/base-alpine:3.7  
ARG GUID=2342  
ARG USER=helm  
  
ARG HELM_VERSION=v2.7.2  
ARG HELM_FILENAME=helm-${HELM_VERSION}-linux-amd64.tar.gz  
ARG HELM_URL=http://storage.googleapis.com/kubernetes-helm/${HELM_FILENAME}  
  
ARG LANDSCAPER_VERSION=1.0.12  
ARG LANDSCAPER_FILENAME=landscaper-${LANDSCAPER_VERSION}-linux-amd64.tar.gz  
ARG
LANDSCAPER_URL=https://github.com/Eneco/landscaper/releases/download/${LANDSCAPER_VERSION}/${LANDSCAPER_FILENAME}  
  
ARG KUBECTL_VERSION=v1.9.1  
ARG KUBECTL_URL=https://storage.googleapis.com/kubernetes-
release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl  
  
ARG KOPS_VERSION=1.8.0  
ARG
KOPS_URL=https://github.com/kubernetes/kops/releases/download/${KOPS_VERSION}/kops-
linux-amd64  
  
ENV HOME=/home/${USER}/  
  
# Install git and enable SSL  
RUN apk add --update --no-cache ca-certificates git  
  
# Install helm  
RUN curl -L ${HELM_URL} | tar zxv -C /tmp \  
&& cp /tmp/linux-amd64/helm /bin/helm \  
&& rm -rf /tmp/*  
  
# Install landscaper  
RUN curl -L ${LANDSCAPER_URL} | tar zxv -C /tmp \  
&& cp /tmp/landscaper /bin/landscaper \  
&& rm -rf /tmp/*  
  
# Install kubectl  
ADD ${KUBECTL_URL} /usr/local/bin/kubectl  
  
# Install kops  
ADD ${KOPS_URL} /usr/local/bin/kops  
  
# Set executable permissions and verify that installed tools work  
RUN set -x \  
&& chmod +x /usr/local/bin/kubectl \  
&& chmod +x /usr/local/bin/kops \  
&& adduser helm -Du ${GUID} -h ${HOME} \  
&& kubectl version --client \  
&& helm version --client \  
&& landscaper version \  
&& kops version  
  
USER ${USER}  
  
CMD [ "/bin/bash", "-c" ]

