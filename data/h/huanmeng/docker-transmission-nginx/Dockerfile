FROM rastasheep/ubuntu-sshd:16.04  
MAINTAINER huanmeng "imhuanmeng@outlook.com"  
RUN apt-get -yqq update  
RUN apt-get -yqq install transmission-cli transmission-common transmission-
daemon  
RUN apt-get -yqq install nginx  
  
RUN service transmission-daemon stop  
RUN service nginx stop  
  
COPY /settings.json /var/lib/transmission-daemon/info/settings.json  
COPY /entry.sh /usr/local/entry.sh  
COPY /download.conf /etc/nginx/conf.d/download.conf  
  
RUN chmod +x /usr/local/entry.sh  
  
EXPOSE 22  
EXPOSE 80  
EXPOSE 443  
EXPOSE 8081  
EXPOSE 9091  
EXPOSE 51413  
ENTRYPOINT ["/usr/local/entry.sh"]

