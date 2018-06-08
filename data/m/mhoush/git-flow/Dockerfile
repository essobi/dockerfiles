FROM alpine:3.3  
RUN apk add --no-cache \  
git \  
curl \  
perl \  
util-linux && \  
cd /tmp && \  
curl -OL https://raw.github.com/nvie/gitflow/develop/contrib/gitflow-
installer.sh && \  
sed -i '1s/#!\/bin\/bash/#!\/bin\/sh/' /tmp/gitflow-installer.sh && \  
chmod +x /tmp/gitflow-installer.sh && \  
sh /tmp/gitflow-installer.sh && \  
rm -rf /var/tmp/* /tmp/* /var/cache/apk/*  
  
COPY entrypoint.sh /  
  
VOLUME /repo  
  
WORKDIR /repo  
  
ENTRYPOINT ["/entrypoint.sh"]  
  

