FROM blasphemy/alpine-glibc  
ARG HYPERKUBE_VERSION=v1.3.0  
RUN apk --no-cache add ca-certificates wget iptables \  
&& wget
https://github.com/kubernetes/kubernetes/releases/download/${HYPERKUBE_VERSION}/kubernetes.tar.gz
-O kubernetes.tar.gz \  
&& mkdir kube-binaries \  
&& tar xvf kubernetes.tar.gz \  
&& tar xvf kubernetes/server/kubernetes-server-linux-amd64.tar.gz -C kube-
binaries \  
&& cp kube-binaries/kubernetes/server/bin/hyperkube /hyperkube \  
&& cp kube-binaries/kubernetes/server/bin/kubectl /kubectl \  
&& chmod u+x /kubectl \  
&& chmod u+x /hyperkube \  
&& rm -rf kubernetes \  
&& rm -rf kube-binaries \  
&& rm kubernetes.tar.gz \  
&& apk del wget --no-cache  
CMD ["/kubectl"]  

