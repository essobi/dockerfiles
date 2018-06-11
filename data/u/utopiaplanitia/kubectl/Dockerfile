  
FROM ubuntu:18.04  
ENV KUBECTL_VERSION "v1.10.3"  
RUN apt-get update -y && \  
apt-get install -y \  
curl \  
gettext && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -L https://storage.googleapis.com/kubernetes-
release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl -o
/usr/local/bin/kubectl \  
&& chmod +x /usr/local/bin/kubectl  
  
CMD ["bash"]  

