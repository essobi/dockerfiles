FROM alpine:3.6  
  
RUN set -ex && \  
apk add --no-cache ansible ca-certificates git openssl openssh-client && \  
wget -qO /usr/local/bin/semaphore https://github.com/ansible-
semaphore/semaphore/releases/download/v2.4.1/semaphore_linux_amd64 && \  
chmod +x /usr/local/bin/semaphore  
  
EXPOSE 3000  
  
ENTRYPOINT ["semaphore"]  
  
CMD ["-config", "/etc/semaphore/semaphore_config.json"]  

