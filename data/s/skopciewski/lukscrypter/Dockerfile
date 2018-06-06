FROM alpine:3.7  
RUN apk add --no-cache bash cryptsetup file e2fsprogs  
  
COPY data/entrypoint /entrypoint  
RUN chmod 755 /entrypoint  
  
ENV VOLUME_DIR=/mnt  
ENV VOLUME_NAME=volume  
VOLUME ${VOLUME_DIR}  
  
ENTRYPOINT ["/entrypoint"]  
CMD ["start"]  

