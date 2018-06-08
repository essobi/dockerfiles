FROM ubuntu:14.04  
MAINTAINER david.siaw@mobingi.com  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
ADD provision.sh /provision.sh  
  
RUN bash /provision.sh  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY config /config  
COPY sudoers /etc/sudoers  
  
COPY Gemfile /root/bootstrapgems/Gemfile  
  
ADD run.sh /run.sh  
ADD startup.sh /startup.sh  
RUN chmod 755 /*.sh  
  
EXPOSE 80  
CMD ["/run.sh"]  

