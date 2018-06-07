FROM alpine:latest  
  
ENV PLUGIN_NETSHARE_VERSION 0.19  
RUN apk add --update wget nfs-utils ca-certificates &&\  
rm -rf /var/cache/apk/* &&\  
update-ca-certificates  
  
RUN wget -O /usr/bin/docker-volume-netshare
https://github.com/ContainX/docker-volume-
netshare/releases/download/v${PLUGIN_NETSHARE_VERSION}/docker-volume-
netshare_${PLUGIN_NETSHARE_VERSION}_linux_amd64-bin &&\  
chmod +x /usr/bin/docker-volume-netshare  
  
ENTRYPOINT ["/usr/bin/docker-volume-netshare"]  
CMD ["efs"]  

