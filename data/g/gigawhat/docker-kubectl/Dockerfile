FROM alpine  
  
ENV KUBECTL_VERSION='v1.6.4'  
RUN apk add --update ca-certificates \  
&& apk add --update -t deps curl \  
&& curl -L https://storage.googleapis.com/kubernetes-
release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl -o
/usr/local/bin/kubectl \  
&& chmod +x /usr/local/bin/kubectl \  
&& apk del --purge deps \  
&& rm /var/cache/apk/*  
  
COPY start.sh /start.sh  
ENTRYPOINT ["/start.sh"]  
CMD ["help"]  

