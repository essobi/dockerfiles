FROM ruby:2.4.1-alpine  
  
RUN apk update && apk upgrade && \  
apk add --no-cache \  
bash \  
less \  
fontconfig \  
postgresql-client postgresql-dev \  
git \  
alpine-sdk \  
nodejs \  
tzdata && \  
touch ~/.bashrc && \  
curl -o- -L https://yarnpkg.com/install.sh | bash -s -- --version 0.27.5 && \  
curl -Ls
"https://github.com/dustinblackman/phantomized/releases/download/2.1.1a/dockerized-
phantomjs.tar.gz" | tar xz -C /  
  
ENV PATH /root/.yarn/bin:$PATH  

