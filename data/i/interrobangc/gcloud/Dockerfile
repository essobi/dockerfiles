FROM google/cloud-sdk:alpine  
  
ADD https://storage.googleapis.com/kubernetes-
release/release/v1.9.3/bin/linux/amd64/kubectl /usr/bin/kubectl  
  
RUN set -x && \  
apk add --no-cache \  
curl \  
ca-certificates \  
openssl \  
&& \  
chmod +x /usr/bin/kubectl && \  
curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get >
/tmp/get_helm.sh && \  
chmod +x /tmp/get_helm.sh && \  
/tmp/get_helm.sh  
  
COPY docker-entrypoint.sh /usr/bin/docker-entrypoint.sh  
  
WORKDIR /app  
  
ENTRYPOINT ["/usr/bin/docker-entrypoint.sh"]  
  
CMD ["bash"]

