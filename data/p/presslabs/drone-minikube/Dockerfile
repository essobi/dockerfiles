FROM alpine:3.6  
MAINTAINER Presslabs <ping@presslabs.com>  
  
ARG KUBE_VERSION=1.9.0  
ARG MINIKUBE_VERSION=0.25.0  
WORKDIR /root  
  
ENV GOPATH="/usr/bin" \  
GOROOT="/usr/lib/go" \  
KUBERNETES_VERSION="${KUBE_VERSION}" \  
MINIKUBE_WANTUPDATENOTIFICATION="false" \  
MINIKUBE_WANTREPORTERRORPROMPT="false" \  
MINIKUBE_HOME="/root" \  
CHANGE_MINIKUBE_NONE_USER="true"  
RUN apk --update --no-cache add docker sudo bash openrc && \  
apk upgrade --update && \  
apk add --no-cache --virtual=.build-dependencies ca-certificates python2 wget
go make \  
autoconf findutils make pkgconf libtool g++ automake linux-headers git && \  
wget "https://storage.googleapis.com/kubernetes-
release/release/v${KUBERNETES_VERSION}/bin/linux/amd64/kubectl" -O
"/usr/local/bin/kubectl" && \  
mkdir -p /usr/bin/src/k8s.io && cd /usr/bin/src/k8s.io && chmod +x
/usr/local/bin/kubectl && \  
git clone \--depth=1 --branch v${MINIKUBE_VERSION}
https://github.com/kubernetes/minikube && cd minikube && \  
make && mv ./out/minikube /usr/local/bin/minikube && rm -rf
/usr/bin/src/k8s.io && rm -rf /tmp/* && \  
apk del .build-dependencies  
  
RUN sudo minikube start --vm-driver none --kubernetes-version
v${KUBERNETES_VERSION} \--memory 1024 --disk-size 4g  
  
COPY docker-entrypoint.sh /usr/local/bin/  
  
VOLUME /root/.minikube  
EXPOSE 8443  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["start"]  

