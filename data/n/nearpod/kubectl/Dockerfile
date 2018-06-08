FROM frolvlad/alpine-glibc:alpine-3.7  
ARG KUBECTL_VERSION=stable  
ARG KUBECTL_USER=kubectl  
ENV KUBECTL_VERSION=$KUBECTL_VERSION  
  
ENV HOME=/config  
  
RUN set -ex; \  
apk add --no-cache bash bash-completion curl ca-certificates; \  
if [ "${KUBECTL_VERSION}"="stable" ]; then \  
curl -q -sSL "https://storage.googleapis.com/kubernetes-release/release/$(curl
-q -sSL https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl" -o
/usr/local/bin/kubectl; \  
else \  
curl -q -sSL "https://storage.googleapis.com/kubernetes-
release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl" -o
/usr/local/bin/kubectl; \  
fi; \  
chmod +x /usr/local/bin/kubectl  
  
WORKDIR /config  
  
RUN set -ex; \  
WORKDIR="$PWD"; \  
addgroup -g 1000 "$KUBECTL_USER"; \  
adduser -D -h "$WORKDIR" -u 1000 -G "$KUBECTL_USER" "$KUBECTL_USER"; \  
[ `id -u "$KUBECTL_USER"` -eq 1000 ]; \  
[ `id -g "$KUBECTL_USER"` -eq 1000 ]; \  
kubectl version --client; \  
echo 'if [ -f /etc/profile.d/bash_completion.sh ]; then source
/etc/profile.d/bash_completion.sh; source <(kubectl completion bash) ; fi' >>
$WORKDIR/.bashrc  
  
USER kubectl  

