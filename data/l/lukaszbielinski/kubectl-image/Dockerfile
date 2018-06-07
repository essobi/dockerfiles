FROM alpine:3.6  
ENV KUBECTL_VERSION=v1.7.1  
RUN apk add --update --no-cache bash curl vim jq ca-certificates \  
&& rm -rf /var/cache/apk/*  
  
RUN curl -L https://storage.googleapis.com/kubernetes-
release/release/$KUBECTL_VERSION/bin/linux/amd64/kubectl -o /usr/bin/kubectl \  
&& chmod +x /usr/bin/kubectl  
  
COPY provisioners provisioners  
RUN chmod -R +x provisioners  
  
ENV DEPLOYMENT_DIR deployments  
ENV SECRETS_DIR secrets  
ENV CONFIGMAPS_DIR configmaps  
ENV NS_DIR namespaces  
  
  
CMD ["bash", "-c", "/provisioners/script-${PROV_TYPE}.sh"]  

