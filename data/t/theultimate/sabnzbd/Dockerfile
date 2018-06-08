FROM theultimate/mediabase  
MAINTAINER Maikel Dollé <maikel@itmagix.nl>  
  
RUN git clone \--depth 1 https://github.com/sabnzbd/sabnzbd /sabnzbd --branch
master  
  
ADD ./start.sh /start.sh  
ADD ./server.cert /sabnzbd  
ADD ./server.key /sabnzbd  
ADD ./sabnzbd_config.ini /sabnzbd/sabnzbd_config.ini  
ADD ./configure.env /sabnzbd/configure.env  
RUN chmod u+x /start.sh  
  
EXPOSE 9200 9201  
CMD ["./start.sh"]  

