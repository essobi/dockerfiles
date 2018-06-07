FROM ubuntu:14.04  
MAINTAINER Kouyou.Arima <arimakouyou@gmail.com>  
  
RUN echo "Asia/Tokyo" > /etc/timezone \  
&& dpkg-reconfigure -f noninteractive tzdata \  
&& apt-get install -y language-pack-ja \  
&& update-locale LANG=ja_JP.UTF-8 \  
&& apt-get update \  
&& apt-get install -y software-properties-common vim wget curl unzip zip
build-essential python git git-svn subversion bash-completion \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*  
ENV LANG ja_JP.UTF-8  

