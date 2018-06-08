FROM timhaak/base:latest  
MAINTAINER tim@haak.co.uk  
  
RUN echo "deb http://shell.ninthgate.se/packages/debian wheezy main" >
/etc/apt/sources.list.d/plexmediaserver.list && \  
curl http://shell.ninthgate.se/packages/shell-ninthgate-se-keyring.key | apt-
key add - && \  
apt-get -q update && \  
apt-get install -qy --force-yes plexmediaserver && \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
VOLUME ["/config","/Movies","/Shows"]  
  
ADD ./start.sh /start.sh  
RUN chmod u+x /start.sh  
  
ADD ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
ENV RUN_AS_ROOT="true" \  
CHANGE_DIR_RIGHTS="false"  
EXPOSE 32400  
CMD ["/start.sh"]  

