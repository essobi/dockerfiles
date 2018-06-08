FROM mhart/alpine-node:4.2.6  
RUN apk add --update build-base python firefox xvfb \  
&& npm install -g selenium-webdriver@2.48.2 \  
&& apk del build-base python \  
&& rm -rf /tmp/* /var/cache/apk/* /root/*  
  
ADD xvfb-run /bin/xvfb-run  

