# Builder (stage 0)  
FROM golang:1.9  
RUN git clone https://github.com/kubernetes-incubator/external-storage.git \  
/go/src/github.com/kubernetes-incubator/external-storage  
RUN cd /go/src/github.com/kubernetes-incubator/external-storage/nfs && make  
  
# Update the nfs-provsioner executable in the upstream image  
FROM quay.io/kubernetes_incubator/nfs-provisioner:v1.0.8  
COPY \--from=0 /go/src/github.com/kubernetes-incubator/external-
storage/nfs/nfs-provisioner /nfs-provisioner  

