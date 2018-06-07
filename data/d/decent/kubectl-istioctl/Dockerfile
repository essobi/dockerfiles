FROM bash:4  
RUN apk update --no-cache  
RUN apk add gettext ca-certificates openssl make  
  
ENV DUMB_VERSION="1.2.1"  
ENV KUBE_VERSION="v1.10.1"  
ENV ISTIO_VERSION="0.7.1"  
RUN wget https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_VERSION}/dumb-init_${DUMB_VERSION}_amd64 -O
/usr/local/bin/dumb-init \  
&& chmod +x /usr/local/bin/dumb-init  
  
RUN wget https://storage.googleapis.com/kubernetes-
release/release/${KUBE_VERSION}/bin/linux/amd64/kubectl -O
/usr/local/bin/kubectl \  
&& chmod +x /usr/local/bin/kubectl  
RUN wget
https://github.com/istio/istio/releases/download/${ISTIO_VERSION}/istio-${ISTIO_VERSION}-linux.tar.gz
\  
&& tar zxvf istio-${ISTIO_VERSION}-linux.tar.gz \  
&& cp istio-${ISTIO_VERSION}/bin/istioctl /usr/local/bin/ \  
&& chmod +x /usr/local/bin/istioctl  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN cat /usr/local/bin/docker-entrypoint.sh >> /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/dumb-init", "--", "/docker-entrypoint.sh"]

