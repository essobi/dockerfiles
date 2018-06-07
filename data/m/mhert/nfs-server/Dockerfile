FROM alpine:3.5  
ENTRYPOINT ["/sbin/tini", "--", "/usr/local/bin/docker-entrypoint.sh"]  
CMD ["/usr/local/bin/nfs.sh"]  
  
EXPOSE 2049/tcp \  
20048/tcp  
  
ENV EXPORTS="/data"  
ENV
EXPORT_OPTIONS="rw,sync,subtree_check,no_acl,all_squash,anonuid=1000,anongid=1000,insecure"  
RUN apk add --no-cache \  
tini \  
nfs-utils  
  
COPY bin/ /usr/local/bin/  
COPY docker-entrypoint.d/ /etc/docker-entrypoint.d/  

