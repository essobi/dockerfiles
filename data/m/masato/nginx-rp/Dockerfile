FROM dockerfile/nginx  
MAINTAINER Masato Shimizu <ma6ato@gmail.com>  
  
ENV HOME /root  
ENV LANG ja_JP.UTF-8  
RUN locale-gen $LANG && update-locale $LANG && \  
ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
ADD default /opt/nginx/templates/default  
ADD run.sh /run.sh  
CMD ["/run.sh"]

