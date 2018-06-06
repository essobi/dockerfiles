FROM centos:7  
ENV KUBERNETES_VERSION 1.3.7  
RUN curl -O --retry 999 --retry-max-time 0 -sSL
https://storage.googleapis.com/kubernetes-
release/release/v$KUBERNETES_VERSION/bin/linux/amd64/kubectl && \  
chmod +x kubectl && \  
mv kubectl /usr/bin/  
  
ENV OPENSHIFT_VERSION 1.3.0  
ENV OPENSHIFT_UID 3ab7af3d097b57f933eccef684a714f2368804e7  
RUN curl --retry 999 --retry-max-time 0 -sSL
https://github.com/openshift/origin/releases/download/v$OPENSHIFT_VERSION/openshift-
origin-client-tools-v$OPENSHIFT_VERSION-$OPENSHIFT_UID-linux-64bit.tar.gz |
tar xzv && \  
mv openshift-origin-*/* /usr/bin/ && \  
rm -rf openshift-origin-client-tools-v$OPENSHIFT_VERSION-$OPENSHIFT_UID-
linux-64bit  
  
ENV GOFABRIC8_VERSION 0.4.72  
RUN curl -O --retry 999 --retry-max-time 0 -sSL
https://github.com/fabric8io/gofabric8/releases/download/v$GOFABRIC8_VERSION/gofabric8-linux-
amd64 && \  
chmod +x gofabric8-linux-amd64 && \  
mv gofabric8-linux-amd64 /usr/bin/gofabric8  
  
CMD ["sleep","infinity"]  

