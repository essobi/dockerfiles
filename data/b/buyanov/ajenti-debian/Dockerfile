FROM python:2.7.10-wheezy  
  
RUN wget http://repo.ajenti.org/debian/key -O- | apt-key add -  
  
RUN echo "deb http://repo.ajenti.org/debian main main debian" >>
/etc/apt/sources.list  
  
RUN rm /etc/apt/apt.conf.d/docker-gzip-indexes  
  
RUN apt-get update && apt-get install -y ajenti  
  
EXPOSE 8000  
ENTRYPOINT ["ajenti-panel"]  

