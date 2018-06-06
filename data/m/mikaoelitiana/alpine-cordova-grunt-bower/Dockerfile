FROM mhart/alpine-node:0.12  
MAINTAINER "Mika Andrianarijaona <mikaoelitiana@gmail.com>"  
RUN apk --update add git && rm -rf /var/cache/apk/* && \  
npm install -g cordova bower grunt-cli && \  
echo '{ "allow_root": true }' > /root/.bowerrc  
  

