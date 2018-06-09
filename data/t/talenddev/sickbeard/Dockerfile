FROM talenddev/python  
MAINTAINER talenddev <leo@talenddev.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get install -qy --force-yes git-core python-cheetah python-openssl  
  
RUN git clone https://github.com/midgetspy/Sick-Beard.git /opt/sickbeard  
  
# Add sickbeard to runit  
RUN mkdir /etc/service/sickbeard  
ADD start.sh /etc/service/sickbeard/run  
RUN chmod +x /etc/service/sickbeard/run  
  
EXPOSE 8081  

