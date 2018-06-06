FROM alpine:3.3  
COPY ./remove-po.sh /remove-po.sh  
RUN chmod +x /remove-po.sh  
  
ENV KUBE_LATEST_VERSION="v1.6.4"  
RUN apk add --update ca-certificates \  
&& apk add --update -t deps curl \  
&& curl -L https://storage.googleapis.com/kubernetes-
release/release/${KUBE_LATEST_VERSION}/bin/linux/amd64/kubectl -o
/usr/local/bin/kubectl \  
&& chmod +x /usr/local/bin/kubectl \  
&& apk del --purge deps \  
&& rm /var/cache/apk/*  
  
ENV CONSUL_TEMPLATE_VERSION=0.18.5  
RUN apk add --update curl && \  
curl -LO http://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \  
apk del openssl ca-certificates curl libssh2 && \  
rm -rf /var/lib/apt/lists/* && \  
unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \  
mv consul-template /usr/local/bin/consul-template && \  
rm consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip  
  
ENTRYPOINT ["/usr/local/bin/consul-template"]  

