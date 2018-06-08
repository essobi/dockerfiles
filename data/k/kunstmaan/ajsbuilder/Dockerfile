FROM alpine:latest  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
COPY Gemfile /usr/src/app/  
  
RUN echo 'gem: --no-rdoc --no-ri' > /etc/gemrc && \  
apk --update add --virtual build_deps build-base python nasm ruby-dev libc-dev
linux-headers openssl-dev libxml2-dev libxslt-dev && \  
apk --update add git ruby ruby-bundler ruby-io-console nodejs ca-certificates
&& \  
bundle install && \  
npm set progress=false && \  
npm install -g gulp && \  
npm install && \  
rm -f package.json Gemfile && \  
apk del build_deps && \  
rm -rf /var/cache/apk/*  
  
CMD [ "/bin/bash" ]  

