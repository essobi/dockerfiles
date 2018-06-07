FROM ubuntu  
  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install language-pack-ja-base language-pack-ja ibus-mozc && \  
update-locale LANG=ja_JP.UTF-8 LANGUAGE=ja_JP:ja && \  
apt-get autoremove && \  
apt-get autoclean && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/apt/* && \  
rm -rf /var/log/*  
  
ENV LANG ja_JP.UTF-8  
ENV LC_ALL ja_JP.UTF-8  
ENV LC_CTYPE ja_JP.UTF-8  

