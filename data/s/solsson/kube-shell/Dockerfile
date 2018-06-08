FROM debian:stretch-slim  
  
ENV KUBERNETES_VERSION=1.8.2  
RUN set -e; \  
export DEBIAN_FRONTEND=noninteractive; \  
runDeps='python python-wheel python-yaml'; \  
buildDeps='python-pip python-setuptools curl ca-certificates'; \  
apt-get update && apt-get install -y $runDeps $buildDeps \--no-install-
recommends; \  
\  
curl -o /tmp/k.tgz -SLs "https://dl.k8s.io/v$KUBERNETES_VERSION/kubernetes-
client-linux-amd64.tar.gz"; \  
tar -xvzf /tmp/k.tgz --strip-components=1 -C /tmp; \  
mv -v /tmp/client/bin/kubectl /usr/local/bin/; \  
chmod a+x /usr/local/bin/kubectl; \  
rm -rf /tmp/*; \  
\  
pip install kube-shell; \  
\  
apt-get purge -y --auto-remove $buildDeps; \  
rm -rf /var/lib/apt/lists/*; \  
rm -rf /var/log/dpkg.log /var/log/alternatives.log /var/log/apt  
  
RUN groupadd --gid 1000 k \  
&& useradd --uid 1000 --gid k --shell /bin/bash --create-home k \  
&& mkdir /home/k/.kube && chown k:k /home/k/.kube  
  
USER k:k  
  
ENV KUBECONFIG=/home/k/.kube/config  
  
ENTRYPOINT [ "kube-shell" ]  

