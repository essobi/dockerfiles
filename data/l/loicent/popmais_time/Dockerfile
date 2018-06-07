FROM debian:jessie  
MAINTAINER Loïc ENTRESSANGLE <loic_ent@yahoo.fr>  
  
RUN apt-get update && apt-get -y upgrade && apt-get clean  
RUN apt-get install -y git-core vim python2.7 npm python-urllib3 python-
requests  
  
RUN npm install -g peerflix  
RUN cd /var/ && git clone http://gitlab.com/loic_ent/popmais-time.git && cd
popmais-time && git checkout devel  
  
EXPOSE 8001  
ADD entrypoint.sh /bin/entrypoint.sh  
RUN chmod +x /bin/entrypoint.sh  
  
CMD ["/bin/entrypoint.sh"]  

