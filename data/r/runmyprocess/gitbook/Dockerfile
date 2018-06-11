FROM smebberson/alpine-nodejs  
  
RUN npm install -g gitbook-cli && \  
apk -Uuv add rsync openssh-client lftp py-pip && \  
mkdir -p /aws && \  
pip install awscli && \  
rm /var/cache/apk/*  
  
ENV PATH ${PATH}:/aws  
  
  

