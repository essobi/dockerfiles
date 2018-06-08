# kubectl v1.5  
# docker run --rm pottava/kubectl version  
# docker run --rm -it -v $HOME/.kube/:/root/.kube/ pottava/kubectl get pods  
FROM alpine:3.5  
ENV KUBECTL_VERSION=1.5.6  
RUN apk --no-cache add ca-certificates  
  
RUN apk --no-cache add --virtual build-dependencies curl \  
&& curl -LO https://storage.googleapis.com/kubernetes-
release/release/v$KUBECTL_VERSION/bin/linux/amd64/kubectl \  
&& mv kubectl /usr/bin/ \  
&& chmod +x /usr/bin/kubectl \  
&& apk del --purge -r build-dependencies  
  
ENTRYPOINT ["/usr/bin/kubectl"]  
CMD ["help"]  

