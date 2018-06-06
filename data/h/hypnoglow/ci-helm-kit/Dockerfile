FROM docker:17  
LABEL maintainer="Igor Zibarev <zibarev.i@gmail.com>"  
  
ENV KUBECTL_VERSION v1.8.0  
ENV HELM_VERSION v2.6.1  
ENV HELM_PLUGIN_S3_VERSION v0.2.2  
# download apk index  
RUN apk add --update  
  
# common utils  
RUN apk add --virtual .builtin-utils curl bash  
  
# aws-cli  
RUN apk add --virtual .awscli-runtime-deps python \  
&& apk add --virtual .awscli-build-deps py-pip \  
&& pip install awscli \  
&& apk del --purge .awscli-build-deps  
  
# kubectl  
RUN set -ex \  
&& curl -sSL https://storage.googleapis.com/kubernetes-
release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl -o
/usr/local/bin/kubectl \  
&& chmod +x /usr/local/bin/kubectl  
  
# helm  
RUN set -ex \  
&& curl -sSL https://storage.googleapis.com/kubernetes-
helm/helm-${HELM_VERSION}-linux-amd64.tar.gz | tar xz \  
&& mv linux-amd64/helm /usr/local/bin/helm \  
&& rm -rf linux-amd64 \  
&& helm init --client-only  
  
RUN apk add --virtual .helm-s3-build-deps git make \  
&& helm plugin install https://github.com/hypnoglow/helm-s3.git --version
${HELM_PLUGIN_S3_VERSION} \  
&& apk del --purge .helm-s3-build-deps  
  
# cleanup  
RUN rm -rf /var/cache/apk/*  

