FROM ruby  
MAINTAINER PJ Eby <pje@telecommunity.com>  
  
RUN apt-get -y update && \  
apt-get -y install \  
build-essential \  
git-core \  
libicu-dev \  
libreadline-dev \  
libssl-dev \  
python \  
python-docutils \  
zlib1g-dev  
  
RUN gem install gollum redcarpet org-ruby github-markdown  
  
COPY wrapper.rb /usr/local/bin/gollum-wrapper  
RUN chmod +x /usr/local/bin/gollum-wrapper && \  
mkdir -p /data/wiki && \  
git init /data/wiki && \  
groupadd gollum && useradd -g gollum gollum && \  
chown -R gollum:gollum /data/wiki  
  
USER gollum  
VOLUME /data/wiki  
EXPOSE 4567  
CMD gollum-wrapper $GOLLUM_OPTIONS /data/wiki  
  

