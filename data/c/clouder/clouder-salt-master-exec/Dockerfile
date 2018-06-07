FROM clouder/clouder-base  
MAINTAINER Yannick Buron yburon@goclouder.net  
  
RUN wget -O -
https://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest/SALTSTACK-GPG-KEY.pub
| sudo apt-key add -  
RUN echo "deb http://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest xenial
main" > /etc/apt/sources.list.d/saltstack.list  
RUN apt-get -qq update && DEBIAN_FRONTEND=noninteractive apt-get -y -qq
install salt-master salt-api salt-ssh supervisor python-pip  
  
RUN pip install --upgrade pip cherrypy  
  
ADD sources/salt-api.conf /etc/salt/master.d/salt-api.conf  
ADD sources/reactor.conf /etc/salt/master.d/reactor.conf  
  
RUN echo "[supervisord]" >> /etc/supervisor/conf.d/supervisord.conf  
RUN echo "nodaemon=true" >> /etc/supervisor/conf.d/supervisord.conf  
RUN echo "" >> /etc/supervisor/conf.d/supervisord.conf  
RUN echo "[program:salt]" >> /etc/supervisor/conf.d/supervisord.conf  
RUN echo "command=salt-master" >> /etc/supervisor/conf.d/supervisord.conf  
RUN echo "[program:salt-api]" >> /etc/supervisor/conf.d/supervisord.conf  
RUN echo "command=salt-api" >> /etc/supervisor/conf.d/supervisord.conf  
  
CMD ["/usr/bin/supervisord"]  

