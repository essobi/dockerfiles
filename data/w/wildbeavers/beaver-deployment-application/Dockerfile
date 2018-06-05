FROM alpine  
  
MAINTAINER Arek Czarnik  
  
# Note: Latest version of kubectl may be found at:  
# https://aur.archlinux.org/packages/kubectl-bin/  
ENV KUBE_LATEST_VERSION="v1.9.2"  
# Note: Latest version of helm may be found at:  
# https://github.com/kubernetes/helm/releases  
ENV HELM_VERSION="v2.8.1"  
ENV FILENAME="helm-${HELM_VERSION}-linux-amd64.tar.gz"  
RUN apk add --update ca-certificates \  
&& apk add --update -t deps curl \  
&& apk add bash \  
&& curl -L https://storage.googleapis.com/kubernetes-
release/release/${KUBE_LATEST_VERSION}/bin/linux/amd64/kubectl -o
/usr/local/bin/kubectl \  
&& chmod +x /usr/local/bin/kubectl \  
&& curl -L http://storage.googleapis.com/kubernetes-helm/${FILENAME} -o
/tmp/${FILENAME} \  
&& tar -zxvf /tmp/${FILENAME} -C /tmp \  
&& mv /tmp/linux-amd64/helm /bin/helm \  
&& apk del --purge deps \  
&& rm /var/cache/apk/* \  
&& rm -rf /tmp/*  
  
RUN helm init --client-only  
RUN helm repo add gitlab https://charts.gitlab.io  
COPY charts /charts  
RUN helm lint /charts/*  
RUN cd / && for chart in charts/*; do helm dep up $chart; done || true  
RUN cd / && helm package /charts/*  
  
WORKDIR /config  
  
EXPOSE 80:80  
ENTRYPOINT /bin/helm serve --address 0.0.0.0:80 --url https://repo.wild-
beavers.com  

