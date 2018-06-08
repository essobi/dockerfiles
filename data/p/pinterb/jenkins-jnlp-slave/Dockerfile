FROM jenkinsci/jnlp-slave  
  
MAINTAINER Brad Pinter <brad.pinter@gmail.com>  
  
# Metadata params  
ARG VCS_URL  
ARG VCS_REF  
ARG BUILD_DATE  
ARG VERSION  
  
# Metadata  
LABEL org.label-schema.name="Jenkins JNLP-enabled slave agent" \  
org.label-schema.description="A Jenkins slave agent that is intended to be
used with a Jenkins master that has the kubernernetes plugin installed." \  
org.label-schema.vendor="CDW" \  
org.label-schema.url="https://cdw.com" \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.version=$VERSION \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.schema-version="1.0.0-rc.1"  
  
USER root  
  
RUN apt-get update -y && \  
apt-get install -y --no-install-recommends \  
g++ \  
gcc \  
libc6-dev \  
make \  
jq && \  
rm -rf /var/lib/apt/lists/*  
  
# Google Cloud SDK w/kubectl  
ENV CLOUDSDK_CORE_DISABLE_PROMPTS 1  
ENV PATH /opt/google-cloud-sdk/bin:$PATH  
  
RUN curl https://sdk.cloud.google.com | bash && mv google-cloud-sdk /opt  
RUN gcloud components install kubectl  
  
# Docker  
RUN wget -O /usr/bin/docker --no-check-certificate \  
https://get.docker.com/builds/Linux/x86_64/docker-1.10.3  
RUN chmod a+x /usr/bin/docker  
  
# Helm  
ENV HELM_VERSION v2.0.0  
RUN curl -fsSL "https://storage.googleapis.com/kubernetes-
helm/helm-$HELM_VERSION-linux-amd64.tar.gz" -o helm.tar.gz && \  
tar -C /usr/local/ -xzf helm.tar.gz && \  
cp /usr/local/linux-amd64/helm /usr/local/bin/  
  
# Golang (eventually move this to a container that extends this one?)  
ENV GOLANG_VERSION 1.7.3  
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-
amd64.tar.gz  
ENV GOLANG_DOWNLOAD_SHA256
508028aac0654e993564b6e2014bf2d4a9751e3b286661b0b0040046cf18028e  
  
RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz && \  
echo "$GOLANG_DOWNLOAD_SHA256 golang.tar.gz" | sha256sum -c - && \  
tar -C /usr/local -xzf golang.tar.gz && \  
rm golang.tar.gz  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"  
WORKDIR $GOPATH  
  
RUN go get -u github.com/Masterminds/glide && \  
go get -u github.com/tools/godep && \  
go get github.com/alecthomas/gometalinter && \  
gometalinter --install  

