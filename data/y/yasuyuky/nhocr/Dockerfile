FROM ubuntu:latest  
MAINTAINER yasuyuky <yasuyuki.ymd@gmail.com>  
  
RUN apt-get -y update \  
&& apt-get -y install make \  
curl \  
g++ \  
libfreetype6-dev  
RUN mkdir /src \  
&& cd /src \  
&& curl -L
"http://osdn.jp/frs/redir.php?m=iij&f=%2Fnhocr%2F61902%2Fnhocr-0.22.tar.gz" |
tar xzf - \  
&& cd nhocr-0.22 \  
&& ./configure --prefix=/usr/local && make && make install \  
&& cd /src && rm -rf nhocr-0.22  
RUN mkdir images  
WORKDIR images  
CMD ["bash"]  

