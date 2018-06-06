FROM alpine:3.6  
MAINTAINER Ali Bengali <ali-beng-ali@users.noreply.github.com>  
  
COPY configure-exports.bash start-container.bash /  
  
# Install bash & nfs-utils  
RUN apk add --update bash nfs-utils && \  
rm -rf /var/cache/apk/* && \  
chmod 755 /*.bash  
  
EXPOSE 111/tcp 111/udp 2049/tcp 2049/udp 32765/tcp 32765/udp 32766/tcp
32766/udp 32767/tcp 32767/udp  
  
ENTRYPOINT ["/start-container.bash"]  

