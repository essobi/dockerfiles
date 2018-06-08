FROM marcelmaatkamp/alpine-base  
  
MAINTAINER Marcel Maatkamp <m.maatkamp@gmail.com>  
  
# Let's get serf  
RUN apk update  
RUN apk-install git supervisor unzip  
ADD https://dl.bintray.com/mitchellh/serf/0.6.4_linux_amd64.zip
/projects/0.6.4_linux_amd64.zip  
RUN unzip 0.6.4_linux_amd64.zip  
RUN rm 0.6.4_linux_amd64.zip  
RUN mv serf /usr/bin/  
ADD /start-serf.sh /start-serf.sh  
ADD /run.sh /run.sh  
ADD /supervisord-serf.conf /etc/supervisor.d/supervisord-serf.conf  
RUN chmod 755 /*.sh  
  
EXPOSE 7946 7373  
CMD ["/run.sh"]  

