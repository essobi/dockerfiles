FROM alpine:latest  
  
ARG PLUGIN_NETSHARE_VERSION=0.34  
ARG PLUGIN_NETSHARE_ARCH=amd64  
ENV PLUGIN_NETSHARE_RELEASE=https://github.com/ContainX/docker-volume-
netshare/releases/download/v${PLUGIN_NETSHARE_VERSION}/docker-volume-
netshare_${PLUGIN_NETSHARE_VERSION}_linux_${PLUGIN_NETSHARE_ARCH}-bin  
  
RUN apk add --update wget nfs-utils ca-certificates &&\  
rm -rf /var/cache/apk/* &&\  
update-ca-certificates  
  
RUN wget -O /usr/bin/docker-volume-netshare ${PLUGIN_NETSHARE_RELEASE} \  
&& chmod +x /usr/bin/docker-volume-netshare  
  
ENTRYPOINT ["/usr/bin/docker-volume-netshare"]  
CMD ["efs", "--verbose"]  

