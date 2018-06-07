FROM alpine  
  
ARG VCS_REF  
ARG BUILD_DATE  
  
# Metadata  
LABEL org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.name="helm" \  
org.label-schema.url="https://hub.docker.com/r/enbiso/helm/" \  
org.label-schema.vcs-url="https://github.com/enbiso/helm-docker" \  
org.label-schema.build-date=$BUILD_DATE  
  
COPY init.sh helm.sh /scripts/  
  
RUN apk add \--update ca-certificates \  
&& apk add \--update -t deps curl \  
&& apk add bash \  
&& apk add openssl \  
&& curl -L https://storage.googleapis.com/kubernetes-release/release/$(curl -s
https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl
\  
&& chmod +x /usr/local/bin/kubectl \  
&& curl -L
https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get -o
/scripts/get_helm.sh \  
&& chmod +x /scripts/*.sh \  
&& /scripts/get_helm.sh  
  
ENTRYPOINT /scripts/init.sh \  
&& /bin/bash

