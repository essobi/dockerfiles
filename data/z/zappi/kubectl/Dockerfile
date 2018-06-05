FROM alpine:3.7  
LABEL maintainer "Zappistore Devops <devops@zappistore.com>"  
  
ARG BUILD_DEPS="ca-certificates wget"  
ARG KUBECTL_VERSION="v1.8.8"  
ARG KUBECTL_PACKAGE="kubernetes-client-linux-amd64.tar.gz"  
ARG
KUBECTL_SHA="3d1b9c175b2d978f266f0af857153e83e428136bcb981c639f2af06f7d500dff"  
RUN apk update && \  
apk upgrade && \  
apk add $BUILD_DEPS && \  
wget --progress=dot:mega
https://dl.k8s.io/${KUBECTL_VERSION}/${KUBECTL_PACKAGE} && \  
echo "${KUBECTL_SHA} *${KUBECTL_PACKAGE}" | sha256sum -c - && \  
tar --no-same-owner -xzf ${KUBECTL_PACKAGE} && \  
mv /kubernetes/client/bin/kubectl /usr/local/bin/kubectl && \  
chmod +x /usr/local/bin/kubectl && \  
apk del $BUILD_PACKAGES && \  
rm -rf /var/cache/apk/* /kubernetes*  
  
ENTRYPOINT ["kubectl"]  

