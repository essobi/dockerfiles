FROM node:boron-alpine  
  
ENV GAIANYSUS_MEANSHOP=20170421 \  
BUILD_PACKAGES='bash curl-dev ruby-dev build-base git libpng-dev' \  
RUBY_PACKAGES='ruby-rdoc ruby ruby-io-console ruby-bundler'  
RUN apk update && apk upgrade && \  
apk add $BUILD_PACKAGES && \  
apk add $RUBY_PACKAGES && \  
rm -rf /var/cache/apk/* && \  
mkdir -p /home/meanshop && \  
adduser -S meanshop && \  
chown -R meanshop. /home/meanshop && \  
echo 'gem is complaining but still successfully installs sass' && \  
gem install sass 2>/dev/null; echo 0 && \  
npm install -g bower grunt-cli  
  
COPY . /meanshop  
RUN chown -R meanshop. /meanshop  
WORKDIR /meanshop  
  
RUN npm install && \  
bower install && \  
grunt build  
  
COPY node/start.sh /start.sh  
CMD ["/start.sh"]  

