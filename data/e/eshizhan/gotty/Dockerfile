FROM debian:latest  
LABEL maintainer="eshizhan <eshizhan@126.com>"  
  
EXPOSE 8080  
RUN apt-get -y update && \  
apt-get install -y curl && \  
VERSION=v1.0.1 && \  
curl -sLk
https://github.com/yudai/gotty/releases/download/$VERSION/gotty_linux_amd64.tar.gz
\  
| tar xzC /usr/local/bin && \  
apt-get purge --auto-remove -y curl && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists*  
  
ENTRYPOINT ["/usr/local/bin/gotty"]  
  
CMD ["--permit-write","--random-url","--reconnect","/bin/bash"]  

