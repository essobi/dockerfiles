FROM alpine  
MAINTAINER Wesley Elfring <hi@wesleyelfring.nl>  
  
COPY entrypoint.sh /entrypoint.sh  
ENV EXPORTED_DIRECTORY /mnt  
ENV EXPORT_SETTINGS
rw,fsid=0,async,no_subtree_check,no_auth_nlm,insecure,no_root_squash,crossmnt  
EXPOSE 2049/tcp  
  
# Install NFS and cleanup  
RUN set -xe \  
&& apk add --update --no-progress nfs-utils \  
&& rm -rf /var/cache/apk/* \  
&& chmod +x /entrypoint.sh  
  
CMD ["/entrypoint.sh"]  

