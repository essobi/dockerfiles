FROM ubuntu:16.04  
# Отключаем настройку webadmin.  
RUN echo courier-base courier-base/webadmin-configmode boolean false |
debconf-set-selections  
  
# Устанавливаем нужные пакеты  
RUN apt-get update && apt-get install --assume-yes --no-install-recommends \  
courier-authdaemon \  
courier-authlib-mysql \  
courier-imap \  
courier-pop \  
exim4-daemon-heavy \  
supervisor \  
&& rm -r /var/lib/apt/lists/*  
  
COPY supervisord.conf /etc/supervisor/supervisord.conf  
COPY docker-exim-entrypoint /usr/local/bin/  
  
EXPOSE 25 2525 587 143 110  
ENTRYPOINT ["docker-exim-entrypoint"]  
CMD ["supervisord","-c","/etc/supervisor/supervisord.conf"]  

