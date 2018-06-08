FROM node:8-alpine  
  
LABEL maintainer="miry.sof@gmail.com"  
  
RUN apk add --no-cache bash g++ git make openssl-dev python vim \  
&& node --version \  
&& npm --version \  
&& python --version \  
&& npm install --global storjshare-daemon --unsafe \  
&& npm cache clean --force \  
&& apk del git openssl-dev python vim \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /tmp/npm* \  
&& storjshare --version  
  
ADD run.sh /  
RUN chmod 755 /run.sh  
  
ENV STORJ_PAYMENT_ADDRESS ""  
ENV STORJ_NETWORK_PRIVATE_KEY ""  
VOLUME [ "/root/.config/storjshare/" ]  
ENTRYPOINT [ "storjshare" ]  

