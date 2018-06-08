FROM rhche/centos_jdk8  
  
USER root  
RUN cd /tmp  
  
# START - copied from https://github.com/fabric8io/builder-clients  
RUN curl --retry 999 --retry-max-time 0 -sSL
https://github.com/openshift/origin/releases/download/v1.5.0/openshift-origin-
client-tools-v1.5.0-031cbe4-linux-64bit.tar.gz | tar xzv && \  
mv openshift-origin-*/* /usr/bin/  
  
ENV KUBECTL_VERSION 1.4.8  
RUN curl -O https://storage.googleapis.com/kubernetes-
release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl && \  
chmod +x kubectl && \  
mv kubectl /usr/bin/  
  
RUN mkdir /tmp/gofabric8 && curl --retry 999 --retry-max-time 0 -sSL
https://github.com/fabric8io/gofabric8/releases/download/v0.4.16/gofabric8-0.4.16-linux-
amd64.tar.gz | tar xzv -C /tmp/gofabric8 && \  
chmod +x /tmp/gofabric8/gofabric8 && \  
mv /tmp/gofabric8/* /usr/bin/ && \  
rm -rf /tmp/gofabric8/  
  
RUN curl -L https://github.com/github/hub/releases/download/v2.2.3/hub-linux-
amd64-2.2.3.tgz | tar xzv && \  
mv hub-linux-amd64-2.2.3/bin/hub /usr/bin/ && \  
rm -rf hub-linux-amd64-2.2.3  
  
# END - copied from https://github.com/fabric8io/builder-clients  
ENV FUNKTION_VERSION 1.0.13  
RUN curl -O --retry 999 --retry-max-time 0 -sSL
https://github.com/funktionio/funktion/releases/download/v$FUNKTION_VERSION/funktion-
linux-amd64 && \  
chmod +x funktion-linux-amd64 && \  
mv funktion-linux-amd64 /usr/bin/funktion  
  
USER user

