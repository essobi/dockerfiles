FROM certbot/certbot  
  
LABEL maintainer Kazuhito Yamazawa <yamazawa@supersoftware.co.jp>  
  
ARG KUBECTL_VERSION="v1.9.6"  
ARG RKE_VERSION="v0.1.5"  
ARG STERN_VERSION="1.6.0"  
ARG FAAS_CLI_VERSION="0.6.4"  
ARG KS_VERSION="v0.9.2"  
ARG KOMPOSE_VERSION="v1.11.0"  
ARG ISTIO_VERSION="0.7.1"  
ARG YAML2JSON_VERSION="v1.0"  
ENV KUBECONFIG /work/kube_config_cluster.yml  
  
RUN apk --update add ca-certificates git openssh curl jq bash-completion ruby
ruby-rake ruby-io-console ruby-bundler docker make bash && \  
mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2
&& \  
echo "source /etc/profile.d/bash_completion.sh" >> ~/.bashrc && \  
rm -rf /var/lib/apt/lists/* && \  
rm /var/cache/apk/*  
  
RUN curl -LO https://storage.googleapis.com/kubernetes-
release/release/$KUBECTL_VERSION/bin/linux/amd64/kubectl && \  
chmod +x ./kubectl && \  
mv ./kubectl /usr/local/bin/kubectl && \  
echo "source <(kubectl completion bash)" >> ~/.bashrc  
  
RUN curl -LO
https://github.com/rancher/rke/releases/download/$RKE_VERSION/rke_linux-amd64
&& \  
chmod +x ./rke_linux-amd64 && \  
mv ./rke_linux-amd64 /usr/local/bin/rke  
  
RUN curl -LO
https://github.com/wercker/stern/releases/download/$STERN_VERSION/stern_linux_amd64
&& \  
chmod +x ./stern_linux_amd64 && \  
mv ./stern_linux_amd64 /usr/local/bin/stern && \  
echo "source <(stern --completion=bash)" >> ~/.bashrc  
  
RUN curl -LO https://github.com/openfaas/faas-
cli/releases/download/$FAAS_CLI_VERSION/faas-cli && \  
chmod +x ./faas-cli && \  
mv ./faas-cli /usr/local/bin/faas-cli  
  
RUN curl -LO
https://github.com/ksonnet/ksonnet/releases/download/$KS_VERSION/ks-linux-
amd64 && \  
chmod +x ./ks-linux-amd64 && \  
mv ./ks-linux-amd64 /usr/local/bin/ks  
  
RUN curl -LO
https://github.com/kubernetes/kompose/releases/download/$KOMPOSE_VERSION/kompose-
linux-amd64 && \  
chmod +x ./kompose-linux-amd64 && \  
mv ./kompose-linux-amd64 /usr/local/bin/kompose && \  
echo "source <(kompose completion bash)" >> ~/.bashrc  
  
RUN curl -LO curl -L
https://github.com/istio/istio/releases/download/$ISTIO_VERSION/istio-$ISTIO_VERSION-
linux.tar.gz | tar xz && \  
chmod +x ./istio-$ISTIO_VERSION/bin/istioctl && \  
mv ./istio-$ISTIO_VERSION/bin/istioctl /usr/local/bin/istioctl && \  
echo "source <(istioctl completion)" >> ~/.bashrc  
  
RUN curl -LO
https://github.com/kyamazawa/yaml2json/releases/download/$YAML2JSON_VERSION/yaml2json_linux-
amd64 && \  
chmod +x ./yaml2json_linux-amd64 && \  
mv ./yaml2json_linux-amd64 /usr/local/bin/yaml2json  
  
VOLUME /work  
WORKDIR /work  
  
COPY docker-entrypoint.sh /usr/local/bin/  
COPY scripts /work/scripts  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["bash"]

