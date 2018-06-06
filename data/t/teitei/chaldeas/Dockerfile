FROM teitei/chrome:latest  
ENV LANG ja_JP.UTF-8  
  
# install ja lang pack.  
RUN apt-get update && apt-get install -y language-pack-ja-base language-pack-
ja  
RUN apt-get update && apt-get install -y npm && npm install n -g && n stable
&& ln -sf /usr/local/bin/node /usr/bin/node  
RUN apt-get purge -y nodejs npm  
  
VOLUME /data  

