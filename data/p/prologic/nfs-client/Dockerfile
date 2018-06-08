FROM alpine  
  
ENV FSTYPE nfs4  
ENV MOUNTOPTIONS nfsvers=4  
ENV MOUNTPOINT /mnt/nfs  
  
RUN apk -U add nfs-utils && \  
rm -rf /var/cache/apk/*  
  
ADD entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/bin/sh"]  

