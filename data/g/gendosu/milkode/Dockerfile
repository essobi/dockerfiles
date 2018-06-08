# 本体  
#  
# VERSION 0.0.1  
FROM gendosu/ubuntu-ruby:2.2.2  
  
MAINTAINER Gen Takahashi "gendosu@gmail.com"  
  
ENV PATH=$PATH:/usr/local/rbenv/shims  
  
RUN apt-get update \  
&& apt-get -y install software-properties-common \  
&& add-apt-repository -y universe  
RUN add-apt-repository -y ppa:groonga/ppa \  
&& apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y --force-yes install \  
ttf-kochi-gothic \  
imagemagick \  
language-pack-ja \  
fonts-migmix \  
software-properties-common \  
libgroonga-dev \  
groonga-tokenizer-mecab \  
redis-tools  
  
RUN mkdir -p /products  
WORKDIR /products  
  
ADD Gemfile /products/Gemfile  
ADD Gemfile.lock /products/Gemfile.lock  
  
# ENV MILKODE_DEFAULT_DIR=/products  
RUN eval "$(rbenv init -)"; bundle  

