FROM talenddev/python  
MAINTAINER talenddev <leo@talenddev.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get install -qy --force-yes python-cheetah python-openssl  
  
RUN git clone https://github.com/SiCKRAGETV/SickRage.git /opt/sickrage  
RUN chown share:users -R /opt/sickrage  
# Add sickrage to runit  
RUN mkdir /etc/service/sickrage  
ADD start.sh /etc/service/sickrage/run  
RUN chmod +x /etc/service/sickrage/run  
  
EXPOSE 8081  

