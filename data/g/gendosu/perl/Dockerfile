# ruby  
#  
# VERSION 0.0.1  
  
FROM perl:latest  
  
MAINTAINER Gen Takahashi "gendosu@gmail.com"  
  
RUN apt-get update \  
&& apt-get install -y --force-yes \  
locales \  
&& apt-get clean \  
&& rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
# defaultのlocaleをja_JP.UTF-8にする  
ENV LANG=ja_JP.UTF-8  
RUN echo "ja_JP.UTF-8 UTF-8" > /etc/locale.gen \  
&& locale-gen \  
&& update-locale LANG=ja_JP.UTF-8 \  
# Timezone変更  
  
&& if [ -e /etc/localtime ]; then rm /etc/localtime; fi \  
&& ln -s /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \  
&& dpkg-reconfigure -f noninteractive tzdata  
  

