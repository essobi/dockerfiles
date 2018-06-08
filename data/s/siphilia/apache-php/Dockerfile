#--------------------------------------------------#  
# base  
#--------------------------------------------------#  
FROM phusion/baseimage:0.9.17  
  
RUN apt-get update && apt-get upgrade -y  
  
#--------------------------------------------------#  
# apt-getでのインタラクティブな動作を無効化  
#--------------------------------------------------#  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#--------------------------------------------------#  
# apache 2.4のインストール  
#--------------------------------------------------#  
# 本体及びmkvhostに必要なパッケージ  
RUN apt-get install -y apache2 libapache2-mod-php5 postfix  
  
# daemon起動スクリプト  
RUN mkdir -p /etc/service/apache2  
COPY service/apache2/run /etc/service/apache2/run  
RUN chmod +x /etc/service/apache2/run  
# modの有効化  
RUN a2enmod proxy  
RUN a2enmod proxy_http  
RUN a2enmod headers  
  
# vhost設定ファイルのコピー  
COPY etc/apache2/sites-available/000-default.conf /etc/apache2/sites-
available/000-default.conf  
  
#--------------------------------------------------#  
# Postfixのインストール  
#--------------------------------------------------#  
RUN apt-get install -y postfix  
  
# daemon起動スクリプト  
RUN mkdir -p /etc/service/postfix  
COPY service/postfix/run /etc/service/postfix/run  
RUN chmod +x /etc/service/postfix/run  
# 設定  
COPY service/postfix/main.cf /etc/postfix/main.cf  
RUN cp /etc/services /var/spool/postfix/etc/services  
  
#--------------------------------------------------#  
# EXPOSE  
#--------------------------------------------------#  
  
EXPOSE 80

