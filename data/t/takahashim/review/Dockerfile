# original: https://github.com/vvakame/docker-review/blob/master/Dockerfile  
FROM debian:jessie  
MAINTAINER takahashim  
  
ENV LANG en_US.UTF-8  
# setup  
RUN apt-get update  
RUN apt-get install -y locales  
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen  
RUN locale-gen en_US.UTF-8  
RUN update-locale en_US.UTF-8  
RUN apt-get install -y git-core zip  
  
# install Re:VIEW environment  
RUN apt-get install -y texlive-lang-cjk texlive-fonts-recommended  
RUN gem install review rake --no-rdoc --no-ri  
RUN gem install dropbox-sdk --no-rdoc --no-ri  
  
# install node.js environment  
RUN apt-get install -y nodejs npm  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
# install calibre  
RUN apt-get install -y calibre  
  
# copy build scripts and define workdir  
COPY scripts /review/scripts  
WORKDIR /review  

