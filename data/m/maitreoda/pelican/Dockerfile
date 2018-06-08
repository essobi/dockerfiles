FROM python:2  
MAINTAINER Maitre Oda  
  
ADD ./files /srv  
  
WORKDIR /srv/pelican/  
  
RUN mkdir output content cache  
  
RUN pip install -r requirements.txt  
RUN rm requirements.txt  
RUN chmod +x /srv/develop_server.sh  
  
VOLUME /srv/pelican/  
  
EXPOSE 8000  
CMD /srv/develop_server.sh restart 8000  

