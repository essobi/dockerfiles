FROM node:stretch  
  
ENV TINI_VERSION v0.16.1  
RUN set -ex; \  
curl -fsSL -o /usr/local/bin/tini
https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini; \  
chmod +x /usr/local/bin/tini  
  
RUN yarn global add dathttpd  
  
ENTRYPOINT ["/usr/local/bin/tini", "--", "dathttpd"]  

