FROM scoutapp/docker-scout  
MAINTAINER Oliver Soell <oliver@soell.net>  
  
RUN apt-get install -y gettext-base  
ADD scoutd.yml.tmpl /etc/scout/scoutd.yml.tmpl  
ADD start.sh /start.sh  
  
ENTRYPOINT ["/start.sh"]  
CMD ["/usr/bin/scoutd", "start"]  

