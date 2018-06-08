# vim: set ts=4 sw=4 sts=4 colorcolumn=80 expandtab:  
FROM ubuntu:trusty  
MAINTAINER Jason Meredith <jason.meredith@makerbot.com>  
  
RUN apt-get update \  
&& apt-get install -y memcached \  
supervisor \  
vim-tiny nano-tiny \  
&& mkdir /var/log/memcached \  
&& rm -rf /var/lib/apt/lists/* \  
/var/log/apt/* \  
/var/cache/apt/* \  
/var/log/dpkg.log \  
/var/log/alternatives.log \  
/usr/share/doc \  
/usr/share/man  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 11211  
  
CMD ["/usr/bin/supervisord"]  

