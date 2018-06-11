FROM wengcan/alpine:latest  
  
MAINTAINER wengcan <wengcanvip@gmail.com>  
  
ENV NODE_VERSION 8.11.2  
RUN apk add --update --no-cache \  
make \  
gcc-doc \  
linux-headers \  
sassc \  
libsass  
  
# download source  
RUN mkdir node \  
&& curl -L -O
https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION.tar.gz \  
&& tar zxvf node-v$NODE_VERSION.tar.gz -C node --strip-components=1  
  
#compiler node & ruby  
RUN mkdir -p /srv/var \  
&& cd node \  
&& ./configure \  
&& make \  
&& make install \  
&& cd ../ \  
&& rm -rf node node-v$NODE_VERSION.tar.gz  
  
# install yarn  
RUN apk add --no-cache curl && curl -o- -L https://yarnpkg.com/install.sh | sh  
ENV PATH /root/.yarn/bin:$PATH  
  
ENTRYPOINT ["zsh"]  

