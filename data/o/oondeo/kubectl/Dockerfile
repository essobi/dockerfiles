FROM busybox:glibc  
  
ENV K8S_VERSION=v1.2.4  
ADD https://storage.googleapis.com/kubernetes-
release/release/${K8S_VERSION}/bin/linux/amd64/kubectl /kubectl  
  
RUN chmod +x /kubectl  
  
ENTRYPOINT ["/kubectl"]  
  

