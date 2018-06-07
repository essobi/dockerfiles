FROM frolvlad/alpine-glibc  
  
ENV KUBECTL_VERSION 1.5.2  
# Install kubectl  
RUN apk add --no-cache curl ca-certificates \  
&& curl -sL https://storage.googleapis.com/kubernetes-
release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl -o
/usr/local/bin/kubectl \  
&& chmod +x /usr/local/bin/kubectl  
  
ADD entrypoint.sh /entrypoint.sh  
  
RUN chmod +x /entrypoint.sh  
  
CMD ["/entrypoint.sh"]  

