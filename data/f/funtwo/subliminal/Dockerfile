FROM lsiobase/alpine.python  
MAINTAINER <https://github.com/FuntwoX>  
  
ENV PYTHONIOENCODING="UTF-8"  
RUN \  
git clone -b develop https://github.com/Diaoul/subliminal.git
/opt/subliminaldev  
  
# Install subliminal  
RUN cd /opt/subliminaldev/ && python /opt/subliminaldev/setup.py install  
  
#Language as IETF code  
ENV LANG="-l en -l fr"  
#Each X minutes  
ENV LOOK_TIME=5  
COPY htpasswd /etc/.htpasswd  
  
# Directory for user video files  
VOLUME ["/downloads"]  
  
COPY cronUserAndStart.sh /  
COPY cron_subliminal_user /  
  
RUN chmod +x cronUserAndStart.sh  
CMD ["/cronUserAndStart.sh", "/etc/.htpasswd"]  

