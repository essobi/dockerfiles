FROM sameersbn/gitlab  
MAINTAINER Stefan Fritsch <fritsch@stat-up.com>  
  
RUN apt-get update \  
&& apt-get -o Dpkg::Options::="--force-confold" install -y zip unzip\  
&& apt-get clean  
  
RUN mkdir /home/git/data/tmp  
# RUN cd /home/git/data/tmp  
# RUN chown git:git .  
# RUN chown git:git /home/git/data  
EXPOSE 22/tcp 80/tcp 443/tcp  
  
ENTRYPOINT ["/sbin/entrypoint.sh"]  
CMD ["app:start"]  

