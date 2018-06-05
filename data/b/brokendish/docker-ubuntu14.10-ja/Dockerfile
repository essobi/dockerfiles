#Ubuntu14.10をベースにする  
FROM ubuntu:14.10  
  
#作成者  
MAINTAINER brokendish.org  
  
#インストール  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get -y install build-essential  
RUN apt-get -y install git  
RUN apt-get -y install python  
RUN apt-get -y install language-pack-ja-base language-pack-ja ibus-mozc  
RUN apt-get -y install man  
RUN apt-get -y install manpages-ja  
  
#日本語環境設定  
RUN update-locale LANG=ja_JP.UTF-8 LANGUAGE=ja_JP:ja  
ENV LANG ja_JP.UTF-8  
ENV LC_ALL ja_JP.UTF-8  
ENV LC_CTYPE ja_JP.UTF-8  
# ロケールを基本日本語に設定  
#RUN echo 'LC_ALL=ja_JP.UTF-8' > /etc/default/locale && echo
'LANG=ja_JP.UTF-8' >> /etc/default/locale  
#RUN locale-gen ja_JP.UTF-8  
#その他設定  
ADD .alias /  
#ENTRYPOINT source .alias  
  
CMD ["/bin/bash"]  

